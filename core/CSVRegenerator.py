import ftplib
import os
import shutil
from enum import IntEnum

from PySide2.QtCore import QThread, QMutexLocker, QMutex, Signal
from ftplib import FTP

from core.Logger import Logger


class CSVRegeneratorStepStatus(IntEnum):
    IDLE = 0,
    IN_PROGRESS = 1,
    ENDED_OK = 2,
    ENDED_KO = 3


class ThreadExitCode(IntEnum):
    NO_ERROR = 0,
    FILES_NOT_FOUNDED = 1,
    FTP_LASER_CONNECTION_ERROR = 2,
    FTP_LASER_DOWNLOAD_FILES_ERROR = 3,
    FTP_LASER_REMOVING_FILES_ERROR = 4,
    ERROR_LOCAL_FILE_OPENING_ERROR = 5,
    ERROR_LOCAL_FILE_READING_ERROR = 6,
    CSV_LOCAL_FILE_OPENING_ERROR = 7,
    CSV_LOCAL_FILE_EMPTY = 8,
    CSV_NEW_LOCAL_FILE_WRITING_ERROR = 9,
    FTP_LASER_SENDING_FILE_ERROR = 10,
    CAMERA_REMOVING_FILE_ERROR = 11,
    CAMERA_SENDING_FILE_ERROR = 12


class CSVRegenerator(QThread):

    downloadStepSignal = Signal(int)
    creationCsvSignal = Signal(int)
    sendingLaserSignal = Signal(int)
    sendingCameraSignal = Signal(int)
    exitCodeSignal = Signal(int)


    def __init__(self, parent=None):
        super().__init__(parent)

        self.__mutex = QMutex()
        self.__laserFileList: list = None
        self.__rowMargin: int = 0

        self.__laserFTPAddress: str = ""
        self.__laserFTPPort: int = 0
        self.__laserFTPRemotePath: str = ""

        self.__cameraPath: str = ""

        self.__localLoadingPath: str = ""
        self.__localDownloadingPath: str = ""

        self.__csvFilename: str = ""
        self.__errorFilename: str = ""

    def setLaserFileList(self, fileList: list):
        locker = QMutexLocker(self.__mutex)
        self.__laserFileList = fileList

    def getLaserFileList(self):
        locker = QMutexLocker(self.__mutex)
        return self.__laserFileList

    def getRowMargin(self):
        return self.__rowMargin

    def setRowMargin(self, rowMargin: int):
        self.__rowMargin = rowMargin

    def setLaserConnectionParameters(self, ftpAddress, ftpPort, ftpRemotePath=""):
        locker = QMutexLocker(self.__mutex)
        self.__laserFTPAddress = ftpAddress
        self.__laserFTPPort = ftpPort
        self.__laserFTPRemotePath = ftpRemotePath

    def getLaserConnectionParameters(self):
        locker = QMutexLocker(self.__mutex)
        return self.__laserFTPAddress, self.__laserFTPPort, self.__laserFTPRemotePath

    def setCameraConnectionParameters(self, cameraPath: str):
        locker = QMutexLocker(self.__mutex)
        self.__cameraPath = cameraPath

    def getCameraConnectionParameters(self):
        locker = QMutexLocker(self.__mutex)
        return self.__cameraPath

    def setLocalLoadingPath(self, path: str):
        locker = QMutexLocker(self.__mutex)
        self.__localLoadingPath = path

    def getLocalLoadingPath(self):
        locker = QMutexLocker(self.__mutex)
        return self.__localLoadingPath

    def setLocalDownloadingPath(self, path: str):
        locker = QMutexLocker(self.__mutex)
        self.__localDownloadingPath = path

    def getLocalDownloadingPath(self):
        locker = QMutexLocker(self.__mutex)
        return self.__localDownloadingPath

    def getCsvFilename(self):
        return self.__csvFilename

    def setCsvFilename(self, filename: str):
        self.__csvFilename = filename

    def getErrorFilename(self):
        return self.__errorFilename

    def setErrorFilename(self, filename: str):
        self.__errorFilename = filename

    def run(self):

        Logger().info("Start CSV Regenerator")
        self.downloadStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.creationCsvSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.IDLE)

        locker = QMutexLocker(self.__mutex)

        rowMargin = self.__rowMargin

        laserFileList = self.__laserFileList
        laserFTPAddress = self.__laserFTPAddress
        laserFTPPort = self.__laserFTPPort
        laserFTPRemotePath = self.__laserFTPRemotePath

        cameraPath = self.__cameraPath

        localDownloadingPath = self.__localDownloadingPath

        csvFilename = self.__csvFilename
        errorFilename = self.__errorFilename
        csvNewFilename = self.__csvFilename + ".new"

        Logger().debug("Laser FTP Address: " + laserFTPAddress)
        Logger().debug("Laser FTP Port: " + str(laserFTPPort))
        Logger().debug("Laser FTP Remote Path: " + laserFTPRemotePath)
        Logger().debug("Camera Path: " + cameraPath)
        Logger().debug("Local Downloading Path: " + localDownloadingPath)
        Logger().debug("Csv Filename: " + csvFilename)
        Logger().debug("Error Filename: " + errorFilename)
        Logger().debug("Csv New Filename: " + csvNewFilename)

        locker.unlock()

        itemFounded = 0
        canContinue = False
        errorCode = ThreadExitCode.NO_ERROR


        # controllo che ci siano i file da scaricare nella cartella del laser (lista passata)
        Logger().info("Controllo esistenza file error.txt e lista.csv nel laser")
        for item in laserFileList:
            if item.lower() == errorFilename.lower():
                itemFounded += 1
                Logger().debug(errorFilename+" OK")
            if item.lower() == csvFilename.lower():
                itemFounded += 1
                Logger().debug(csvFilename+" OK")
            canContinue = itemFounded == 2
            if canContinue:
                break

        if not canContinue:
            Logger().error("Uno o entrambi i file non sono presenti")
            errorCode = ThreadExitCode.FILES_NOT_FOUNDED
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " +str(errorCode))
            return


        # mi collego in FTP al laser
        Logger().info("Connessione FTP al laser")
        self.downloadStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        ftpController = FTP()
        ftpController.host = laserFTPAddress
        ftpController.port = laserFTPPort
        try:
            ftpController.connect()
            ftpController.login()
        except ftplib.all_errors as ftpErr:
            Logger().error("Errore connesione FTP: " + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_CONNECTION_ERROR
            self.downloadStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return

        CSVFileLocalPath = localDownloadingPath + "\\" + csvFilename
        CSVNewFileLocalPath = localDownloadingPath + "\\" + csvNewFilename
        errorFileLocalPath = localDownloadingPath + "\\" + errorFilename


        # scarico i file dal laser (rinominando quello appena usato)
        Logger().info("Download file dal laser")
        try:
            ftpController.cwd(laserFTPRemotePath)

            # recupero il file lista.csv e lo elimino da ftp
            cmd = "RETR " + csvFilename
            Logger().debug("Comando: " + cmd)
            ftpController.retrbinary(cmd, open(CSVFileLocalPath, 'wb').write)

            # recupero il file error.txt e lo elimino da ftp
            cmd = "RETR " + errorFilename
            Logger().debug("Comando: " + cmd)
            ftpController.retrbinary(cmd, open(errorFileLocalPath, 'wb').write)

        except ftplib.all_errors as ftpErr:
            Logger().error("Errore download file: " + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_DOWNLOAD_FILES_ERROR
            ftpController.close()
            self.downloadStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return


        # se ho scaricato il file csv, lo elimino dal laser
        Logger().info("Rimozione file lista.csv dal laser")
        try:
            Logger().debug("Eliminazione file \"" + csvFilename + "\" da laser")
            res = ftpController.delete(csvFilename)

        except ftplib.all_errors as ftpErr:
            Logger().error("Errore rimozione file lista.csv dal laser; errore: " + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_REMOVING_FILES_ERROR
            ftpController.close()
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return

        self.downloadStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)


        # apro il file in error in lettura per vedere l'indice dell'ultima stringa stampata
        self.creationCsvSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        Logger().info("Lettura file errore per capire ultima stringa stampata")
        lineToSeek = 0
        fp = None
        try:
            fp = open(errorFileLocalPath)
            lineStr = fp.readline()
            lastPrintedString = fp.readline()
            Logger().debug("Line: "+lineStr)
            Logger().debug("LastPrintedString: " + lastPrintedString)
            lineToSeek = int(lineStr)
            lineToSeek += rowMargin
        except OSError:
            canContinue = False
            errorCode = ThreadExitCode.ERROR_LOCAL_FILE_OPENING_ERROR
            Logger().error("Impossibile aprire il file: " + errorFileLocalPath)
        except ValueError:
            canContinue = False
            errorCode = ThreadExitCode.ERROR_LOCAL_FILE_READING_ERROR
            Logger().error("Impossibile convertire da string a intero il numero di riga stampata")
        finally:
            fp.close()

        if not canContinue:
            self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return


        # creo la lista di stringhe scartando quelle gia' stampate
        streamFile = None
        Logger().info("Lettura file locale " + csvFilename + " escludendo le stringhe stampate")
        try:
            fp = open(CSVFileLocalPath, newline="\r\n", encoding="utf-8")
            for rowCounter in range(lineToSeek):
                fp.readline()
            streamFile = fp.read()
        except OSError:
            canContinue = False
            Logger().error("Impossibile aprire il file: " + CSVFileLocalPath)
        finally:
            fp.close()

        if not canContinue:
            errorCode = ThreadExitCode.CSV_LOCAL_FILE_OPENING_ERROR

        if streamFile==None or len(streamFile)==0:
            Logger().error("Lista vuota")
            errorCode = ThreadExitCode.CSV_LOCAL_FILE_EMPTY

        if errorCode != ThreadExitCode.NO_ERROR:
            self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return


        # creo il nuovo file csv con la nuova lista
        Logger().info("Scrittura file "+ csvNewFilename + " senza le stringhe stampate")
        try:
            fp = open(CSVNewFileLocalPath, "wb")
            bytes2send = bytearray(streamFile, "utf-8")
            fp.write(bytes2send)
        except OSError:
            canContinue = False
            Logger().error("Impossibile aprire il file: " + CSVNewFileLocalPath)
            errorCode = ThreadExitCode.CSV_NEW_LOCAL_FILE_WRITING_ERROR
        finally:
            fp.close()

        if errorCode != ThreadExitCode.NO_ERROR:
            self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return

        self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)


        # invio il nuovo file csv al laser
        Logger().info("Invio file "+csvNewFilename+" al laser")
        self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        try:
            ftpController.cwd(laserFTPRemotePath)
            cmd = "STOR " + csvFilename
            Logger().debug("Comando: "+cmd)
            fp = open(CSVNewFileLocalPath, "rb")
            ftpController.storbinary(cmd, fp)

        except ftplib.all_errors as ftpErr:
            Logger().error("Error on FTP:" + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
            ftpController.close()

        if errorCode != ThreadExitCode.NO_ERROR:
            self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return


        # rimuovo il file error dal laser solo se tutto e' andato a buon fine
        Logger().info("Rimozione error.txt dal laser")
        try:
            Logger().debug("Eliminazione file \"" + errorFilename + "\" dal laser")
            res = ftpController.delete(errorFilename)

        except ftplib.all_errors as ftpErr:
            Logger().error("Error on FTP:" + str(ftpErr))
            ftpController.close()
            errorCode = ThreadExitCode.FTP_LASER_REMOVING_FILES_ERROR
            self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return

        self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)


        # cancello il file csv dalla camera
        Logger().info("Rimozione file "+csvFilename+" dalla camera")
        self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        csvCameraPath = cameraPath + "\\" + csvFilename
        try:
            if os.path.exists(csvCameraPath):
                Logger().debug("Rimozione vecchio file .csv dalla camera")
                os.remove(csvCameraPath)
        except OSError as ex:
            errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
            Logger().error("Impossibile rimuovere il file: " + csvCameraPath)

        if errorCode != ThreadExitCode.NO_ERROR:
            self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
            self.exitCodeSignal.emit(errorCode)
            Logger().error("Codice uscita: " + str(errorCode))
            return


        # invio il nuovo file csv alla camera
        Logger().info("Invio nuovo file lista.csv alla camera")
        try:
            shutil.copy(CSVNewFileLocalPath, csvCameraPath)
        except:
            errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
            Logger().error("Impossibile copiare il nuovo fil csv in camera: " + CSVNewFileLocalPath)

        if errorCode != ThreadExitCode.NO_ERROR:
            self.exitCodeSignal.emit(errorCode)
            self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)

        Logger().info("Processo terminato correttamente")
        self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
        self.exitCodeSignal.emit(errorCode)
        Logger().error("Codice uscita: " + str(errorCode))
        return
