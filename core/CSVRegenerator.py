import ftplib
import os
import shutil
from enum import IntEnum

from PySide2.QtCore import QThread, QMutexLocker, QMutex
from ftplib import FTP


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

        locker.unlock()

        itemFounded = 0
        canContinue = False
        errorCode = ThreadExitCode.NO_ERROR


        # controllo che ci siano i file da scaricare nella cartella del laser (lista passata)
        for item in laserFileList:
            if item.lower() == errorFilename.lower():
                itemFounded += 1
            if item.lower() == csvFilename.lower():
                itemFounded += 1
            canContinue = itemFounded == 2
            if canContinue:
                break

        if not canContinue:
            self.exit(ThreadExitCode.FILES_NOT_FOUNDED)


        # mi collego in FTP al laser
        ftpController = FTP()
        ftpController.host = laserFTPAddress
        ftpController.port = laserFTPPort
        try:
            ftpController.connect()
            ftpController.login()
        except ftplib.all_errors as ftpErr:
            print("Error on FTP: " + ftpErr)
            self.exit(ThreadExitCode.FTP_LASER_CONNECTION_ERROR)

        CSVFileLocalPath = localDownloadingPath + "\\" + csvFilename
        CSVNewFileLocalPath = localDownloadingPath + "\\" + csvNewFilename
        errorFileLocalPath = localDownloadingPath + "\\" + errorFilename


        # scarico i file dal laser
        try:
            ftpController.cwd(laserFTPRemotePath)

            # recupero il file lista.csv e lo elimino da ftp
            cmd = "RETR " + csvFilename
            ftpController.retrbinary(cmd, open(CSVFileLocalPath, 'wb').write)

            # recupero il file error.txt e lo elimino da ftp
            cmd = "RETR " + errorFilename
            ftpController.retrbinary(cmd, open(errorFileLocalPath, 'wb').write)

        except ftplib.all_errors as ftpErr:
            print("Error on FTP:" + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_DOWNLOAD_FILES_ERROR
            ftpController.close()
            self.exit(errorCode)


        # se ho scaricato il file csv, lo elimino dal laser
        try:
            res = ftpController.delete(csvFilename)
            print("Eliminazione file \"" + csvFilename + "\" da laser: " + res)

        except ftplib.all_errors as ftpErr:
            print("Error on FTP:" + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_REMOVING_FILES_ERROR
            ftpController.close()
            self.exit(errorCode)


        # apro il file in error in lettura per vedere l'indice dell'ultima stringa stampata
        lineToSeek = 0
        fp = None
        try:
            fp = open(errorFileLocalPath)
            lineStr = fp.readline()
            lastPrintedString = fp.readline()
            print("Line: "+lineStr)
            print("LastPrintedString: " + lastPrintedString)
            lineToSeek = int(lineStr)
            lineToSeek += rowMargin
        except OSError:
            canContinue = False
            errorCode = ThreadExitCode.ERROR_LOCAL_FILE_OPENING_ERROR
            print("Impossibile aprire il file: " + errorFileLocalPath)
        except ValueError:
            canContinue = False
            errorCode = ThreadExitCode.ERROR_LOCAL_FILE_READING_ERROR
            print("Impossibile convertire da string a intero")
        finally:
            fp.close()

        if not canContinue:
            self.exit(errorCode)


        # creo la lista di stringhe scartando quelle gia' stampate
        streamFile = None
        print("Lettura file " + csvFilename + " escludendo le stringhe stampate")
        try:
            fp = open(CSVFileLocalPath, newline="\r\n", encoding="utf-8")
            for rowCounter in range(lineToSeek):
                fp.readline()
            streamFile = fp.read()
        except OSError:
            canContinue = False
            print("Impossibile aprire il file: " + CSVFileLocalPath)
        finally:
            fp.close()

        if not canContinue:
            errorCode = ThreadExitCode.CSV_LOCAL_FILE_OPENING_ERROR

        if streamFile==None or len(streamFile)==0:
            print("Lista vuota")
            errorCode = ThreadExitCode.CSV_LOCAL_FILE_OPENING_ERROR

        if errorCode != ThreadExitCode.NO_ERROR:
            self.exit(errorCode)


        # creo il nuovo file csv con la nuova lista
        print("Scrittura file "+ csvNewFilename + " senza le stringhe stampate")
        try:
            fp = open(CSVNewFileLocalPath, "wb")
            bytes2send = bytearray(streamFile, "utf-8")
            fp.write(bytes2send)
        except OSError:
            canContinue = False
            print("Impossibile aprire il file: " + CSVNewFileLocalPath)
            errorCode = ThreadExitCode.CSV_NEW_LOCAL_FILE_WRITING_ERROR
        finally:
            fp.close()

        if errorCode != ThreadExitCode.NO_ERROR:
            self.exit(errorCode)


        # invio il nuovo file csv al laser
        try:
            ftpController.cwd(laserFTPRemotePath)
            cmd = "STOR " + csvFilename
            fp = open(CSVNewFileLocalPath, "rb")
            ftpController.storbinary(cmd, fp)

        except ftplib.all_errors as ftpErr:
            print("Error on FTP:" + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
            ftpController.close()

        if errorCode != ThreadExitCode.NO_ERROR:
            self.exit(errorCode)


        # rimuovo il file error dal laser solo se tutto e' andato a buon fine
        try:
            res = ftpController.delete(errorFilename)
            print("Eliminazione file \"" + errorFilename + "\" da laser: " + res)

        except ftplib.all_errors as ftpErr:
            print("Error on FTP:" + str(ftpErr))
            errorCode = ThreadExitCode.FTP_LASER_REMOVING_FILES_ERROR
            ftpController.close()
            self.exit(errorCode)


        # cancello il file csv dalla camera
        csvCameraPath = cameraPath + "\\" + csvFilename
        try:
            if os.path.exists(csvCameraPath):
                os.remove(csvCameraPath)
        except OSError as ex:
            errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
            print("Impossibile rimuovere il file: " + csvCameraPath)

        if errorCode != ThreadExitCode.NO_ERROR:
            self.exit(errorCode)


        # invio il nuovo file csv alla camera
        try:
            shutil.copy(CSVNewFileLocalPath, csvCameraPath)
        except:
            errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
            print("Impossibile copiare il nuovo fil csv in camera: " + CSVNewFileLocalPath)

        self.exit(errorCode)