import datetime
import errno
import ftplib
import os
import shutil
import time
from enum import IntEnum

from PySide2.QtCore import QThread, QMutexLocker, QMutex, Signal, QWaitCondition
from ftplib import FTP

from core.Logger import Logger


class CSVRegeneratorStepStatus(IntEnum):
    IDLE = 0,
    IN_PROGRESS = 1,
    ENDED_OK = 2,
    ENDED_KO = 3


class CSVRegeneratorStep(IntEnum):
    CLEAN_LOCAL_FOLDER = 0,
    CLEAN_CAMERA_FOLDER = 1,
    RENAME_LASER_ITEMS = 2,
    DOWNLOAD_ITEMS_FROM_LASER = 3,
    CLEAN_LASER_FOLDER = 4,
    CSV_BUILD_PROCESS = 5,
    SEND_CSV_TO_LASER = 6,
    SEND_CSV_TO_CAMERA = 7,
    PROCESS_END = 8


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

    cleanLocalFolderStepSignal = Signal(int)
    cleanCameraFolderStepSignal = Signal(int)
    renameLaserItemsStepSignal = Signal(int)
    downloadItemsFromLaserStepSignal = Signal(int)
    cleanLaserFolderStepSignal = Signal(int)
    csvBuildProcessStepSignal = Signal(int)
    sendCsvToLaserStepSignal = Signal(int)
    sendCsvToCameraStepSignal = Signal(int)
    exitCodeSignal = Signal(int)
    cvsNewFileEmptySignal = Signal(bool)
    threadPausedSignal = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__mutex = QMutex()
        self.__laserFileList: list = None
        self.__rowMargin: int = 0

        self.__laserFTPAddress: str = ""
        self.__laserFTPPort: int = 0
        self.__laserFTPRemotePath: str = ""

        self.__cameraPath: str = ""

        self.__localWaitTimeBeforeStart: int = 1
        self.__localLoadingPath: str = ""
        self.__localDownloadingPath: str = ""

        self.__csvFilename: str = ""
        self.__errorFilename: str = ""
        self.__logFilename: str = ""
        self.__stopRequest: bool = False
        self.__pauseRequest: bool = False
        self.__waitCondition = QWaitCondition()

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

    def getLocalWaitTimeBeforeStart(self):
        locker = QMutexLocker(self.__mutex)
        return self.__localWaitTimeBeforeStart

    def setLocalWaitTimeBeforeStart(self, waitTime: int):
        locker = QMutexLocker(self.__mutex)
        self.__localWaitTimeBeforeStart = waitTime

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
        locker = QMutexLocker(self.__mutex)
        return self.__csvFilename

    def setCsvFilename(self, filename: str):
        locker = QMutexLocker(self.__mutex)
        self.__csvFilename = filename

    def getErrorFilename(self):
        locker = QMutexLocker(self.__mutex)
        return self.__errorFilename

    def setErrorFilename(self, filename: str):
        locker = QMutexLocker(self.__mutex)
        self.__errorFilename = filename

    def getLogFilename(self):
        locker = QMutexLocker(self.__mutex)
        return self.__logFilename

    def setLogFilename(self, filename: str):
        locker = QMutexLocker(self.__mutex)
        self.__logFilename = filename

    def getPauseRequest(self):
        locker = QMutexLocker(self.__mutex)
        return self.__pauseRequest

    def setPauseRequest(self, pause: bool):
        locker = QMutexLocker(self.__mutex)
        self.__pauseRequest = pause
        if not self.__pauseRequest:
            self.__waitCondition.notify_all()

    def getStopRequest(self):
        locker = QMutexLocker(self.__mutex)
        return self.__stopRequest

    def setStopRequest(self, stop: bool):
        locker = QMutexLocker(self.__mutex)
        self.__stopRequest = stop

    def connectFtp(self, ftpController) -> bool:

        isConnected: bool = False
        try:
            Logger().info("Connessione al laser in FTP")
            ftpController.connect()
            ftpController.login()
            isConnected = True

        except ftplib.all_errors as ftpErr:
            Logger().error("Errore connessione FTP: " + str(ftpErr))
            ftpController.close()
            isConnected = False

        return isConnected

    def run(self):

        Logger().info("Start CSV Regenerator")

        self.cleanLocalFolderStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.cleanCameraFolderStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.renameLaserItemsStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.downloadItemsFromLaserStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.cleanLaserFolderStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.sendCsvToLaserStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.sendCsvToCameraStepSignal.emit(CSVRegeneratorStepStatus.IDLE)
        self.cvsNewFileEmptySignal.emit(False)

        locker = QMutexLocker(self.__mutex)

        rowMargin = self.__rowMargin

        laserFileList = self.__laserFileList
        laserFTPAddress = self.__laserFTPAddress
        laserFTPPort = self.__laserFTPPort
        laserFTPRemotePath = self.__laserFTPRemotePath

        cameraPath = self.__cameraPath

        waitTimeBeforeStart = self.__localWaitTimeBeforeStart
        localDownloadingPath = self.__localDownloadingPath

        csvFilename = self.__csvFilename
        csvExpireFilename = self.__csvFilename+".expire"
        errorFilename = self.__errorFilename
        logFilename = self.__logFilename
        csvNewFilename = self.__csvFilename + ".new"

        locker.unlock()

        Logger().debug("Laser FTP Address: " + laserFTPAddress)
        Logger().debug("Laser FTP Port: " + str(laserFTPPort))
        Logger().debug("Laser FTP Remote Path: " + laserFTPRemotePath)
        Logger().debug("Camera Path: " + cameraPath)
        Logger().debug("Local Downloading Path: " + localDownloadingPath)
        Logger().debug("Csv Filename: " + csvFilename)
        Logger().debug("Error Filename: " + errorFilename)
        Logger().debug("Log Filename: " + logFilename)
        Logger().debug("Csv New Filename: " + csvNewFilename)

        Logger().info("Aspetto " + str(waitTimeBeforeStart) + " [s] prima di iniziare")
        self.sleep(waitTimeBeforeStart)
        Logger().info("Inizio il processo")

        # path csv e file di errore
        csvFileLocalPath = localDownloadingPath + "\\" + csvFilename
        csvNewFileLocalPath = localDownloadingPath + "\\" + csvNewFilename
        errorFileLocalPath = localDownloadingPath + "\\" + errorFilename
        localLogPath = localDownloadingPath  + "\\log"
        csvCameraPath = cameraPath + "\\" + csvFilename

        # variabili locali
        itemFounded = 0
        canContinue = False
        errorCode = ThreadExitCode.NO_ERROR
        stepToProcess = CSVRegeneratorStep.CLEAN_LOCAL_FOLDER

        # variabili connessione FTP
        ftpController = FTP()
        ftpController.host = laserFTPAddress
        ftpController.port = laserFTPPort
        isFtpConnected = False

        while stepToProcess != CSVRegeneratorStep.PROCESS_END:

            # controllo se posso continuare
            locker = QMutexLocker(self.__mutex)
            while self.__pauseRequest:
                self.threadPausedSignal.emit(True)
                self.__waitCondition.wait(self.__mutex)

            self.threadPausedSignal.emit(False)
            stopRequest = self.__stopRequest

            locker.unlock()

            if stopRequest:
                break
            # stopRequest = self.getStopRequest()
            # if stopRequest:
            #     break

            if stepToProcess == CSVRegeneratorStep.CLEAN_LOCAL_FOLDER:

                Logger().info("Rimozione files nella cartella download locale")
                self.cleanLocalFolderStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
                try:
                    if os.path.exists(csvFileLocalPath):
                        Logger().info("Rimozione file: "+csvFileLocalPath)
                        os.remove(csvFileLocalPath)

                    if os.path.exists(csvNewFileLocalPath):
                        Logger().info("Rimozione file: " + csvNewFileLocalPath)
                        os.remove(csvNewFileLocalPath)

                    if os.path.exists(errorFileLocalPath):
                        Logger().info("Rimozione file: " + errorFileLocalPath)
                        os.remove(errorFileLocalPath)

                except OSError as err:
                    if err != errno.ENOENT:
                        Logger().error("Rimozione file fallita, errore: " + str(err))
                        self.cleanLocalFolderStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                        self.sleep(1)
                        continue

                stepToProcess += 1
                self.cleanLocalFolderStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                Logger().info("Rimozione files nella cartella download locale OK")

            elif stepToProcess == CSVRegeneratorStep.CLEAN_CAMERA_FOLDER:

                Logger().info("Rimozione file "+csvFilename+" dalla camera")
                self.cleanCameraFolderStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
                try:
                    if os.path.exists(csvCameraPath):
                        Logger().debug("Rimozione file .csv dalla camera")
                        os.remove(csvCameraPath)
                except OSError as err:
                    if err != errno.ENOENT:
                        Logger().error("Rimozione file fallita")
                        self.cleanCameraFolderStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                        self.sleep(1)
                        continue

                stepToProcess += 1
                self.cleanCameraFolderStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                Logger().info("Rimozione file "+csvFilename+" dalla camera OK")

            elif stepToProcess == CSVRegeneratorStep.RENAME_LASER_ITEMS:

                Logger().info("Rinomino file "+csvFilename+" in "+csvExpireFilename)
                self.renameLaserItemsStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)

                if not isFtpConnected:
                    isFtpConnected = self.connectFtp(ftpController)
                    if not isFtpConnected:
                        self.renameLaserItemsStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                        self.sleep(1)
                        continue

                try:
                    Logger().info("Spostamento nella cartella FTP: "+laserFTPRemotePath)
                    ftpController.cwd(laserFTPRemotePath)
                    Logger().info("Rinomino il file "+csvFilename+" in "+csvExpireFilename)
                    ftpController.rename(csvFilename, csvExpireFilename)

                except ftplib.all_errors as ftpErr:
                    Logger().error("Errore connessione FTP: " + str(ftpErr))
                    self.renameLaserItemsStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    ftpController.close()
                    isFtpConnected = False
                    self.sleep(1)
                    continue

                stepToProcess += 1
                self.renameLaserItemsStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                Logger().info("Rinomino file "+csvFilename+" in "+csvExpireFilename+" OK")

            elif stepToProcess == CSVRegeneratorStep.DOWNLOAD_ITEMS_FROM_LASER:

                Logger().info("Download file dal laser")
                self.downloadItemsFromLaserStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)

                if not os._exists(localLogPath):
                    os.mkdir(localLogPath)

                if not isFtpConnected:
                    isFtpConnected = self.connectFtp(ftpController)
                    if not isFtpConnected:
                        self.downloadItemsFromLaserStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                        self.sleep(1)
                        continue

                try:
                    ftpController.cwd(laserFTPRemotePath)

                    # recupero il file lista.csv e lo elimino da ftp
                    Logger().info("Download file: "+csvExpireFilename)
                    cmd = "RETR " + csvExpireFilename
                    Logger().debug("Comando: " + cmd)
                    ftpController.retrbinary(cmd, open(csvFileLocalPath, 'wb').write)

                    # recupero il file error.txt e lo elimino da ftp
                    Logger().info("Download file: " + errorFilename)
                    cmd = "RETR " + errorFilename
                    Logger().debug("Comando: " + cmd)
                    ftpController.retrbinary(cmd, open(errorFileLocalPath, 'wb').write)


                except ftplib.all_errors as ftpErr:
                    Logger().error("Errore download file: " + str(ftpErr))
                    self.downloadItemsFromLaserStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    ftpController.close()
                    isFtpConnected = False
                    self.sleep(1)
                    continue

                try:
                    # recupero il file log
                    ts = time.time()
                    logFilenameTS = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
                    logFilenameTS = localLogPath + "\\" + logFilenameTS
                    Logger().info("Download file: " + logFilename)
                    cmd = "RETR " + logFilename
                    Logger().debug("Comando: " + cmd)
                    ftpController.retrbinary(cmd, open(logFilenameTS, 'wb').write)

                except ftplib.all_errors as ftpErr:
                    Logger().error("Errore download file: " + str(ftpErr))
                    ftpController.close()
                    isFtpConnected = False


                stepToProcess += 1
                self.downloadItemsFromLaserStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                Logger().info("Download file dal laser OK")

            elif stepToProcess == CSVRegeneratorStep.CLEAN_LASER_FOLDER:

                Logger().info("Rimozione file cartella laser")
                self.cleanLaserFolderStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)

                if not isFtpConnected:
                    isFtpConnected = self.connectFtp(ftpController)
                    if not isFtpConnected:
                        self.cleanLaserFolderStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                        self.sleep(1)
                        continue

                try:
                    ftpController.cwd(laserFTPRemotePath)
                    Logger().info("Rimozione file: "+csvExpireFilename)
                    ftpController.delete(csvExpireFilename)
                    Logger().info("Rimozione file: " + errorFilename)
                    ftpController.delete(errorFilename)

                except ftplib.all_errors as ftpErr:
                    Logger().error("Errore rimozione file: " + str(ftpErr))
                    self.cleanLaserFolderStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    ftpController.close()
                    isFtpConnected = False
                    self.sleep(1)
                    continue

                stepToProcess += 1
                self.cleanLaserFolderStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                Logger().info("Rimozione file cartella laser OK")

            elif stepToProcess == CSVRegeneratorStep.CSV_BUILD_PROCESS:

                Logger().info("Generazione nuovo file csv")
                self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)

                # apro il file error in lettura per vedere l'indice dell'ultima stringa stampata
                fp = None
                try:
                    Logger().info("Recupero informazioni dal file: "+errorFileLocalPath)
                    fp = open(errorFileLocalPath)
                    lineStr = fp.readline()
                    lastPrintedString = fp.readline()
                    Logger().debug("Line: " + lineStr)
                    Logger().debug("LastPrintedString: " + lastPrintedString)
                    lineToSeek = int(lineStr)
                    lineToSeek += rowMargin

                except OSError:
                    Logger().error("Errore apertura file "+errorFileLocalPath)
                    self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    fp.close()
                    self.sleep(1)
                    continue

                except ValueError:
                    Logger().error("Errore conversione indice riga a intero")
                    self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    fp.close()
                    self.sleep(1)
                    continue

                fp.close()

                # creo la lista di stringhe scartando quelle gia' stampate
                streamFile = None
                Logger().info("Lettura file locale "+csvFilename+" escludendo le stringhe stampate")
                try:
                    fp = open(csvFileLocalPath, newline="\r\n", encoding="utf-8")
                    for rowCounter in range(lineToSeek):
                        readLine = fp.readline()
                        if readLine == "":
                            break
                    streamFile = fp.read()
                except OSError:
                    Logger().error("Errore apertura file: "+csvFileLocalPath)
                    self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    fp.close()
                    self.sleep(1)
                    continue

                fp.close()

                # se file vuoto, allora ho finito, devo far caricare al cliente un nuovo file csv
                if streamFile == None or len(streamFile) == 0:
                    Logger().info("Lista vuota")
                    self.cvsNewFileEmptySignal.emit(True)
                    stepToProcess = CSVRegeneratorStep.PROCESS_END
                    self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                    continue

                # creo il nuovo file csv con la nuova lista
                Logger().info("Scrittura file "+csvNewFilename+" senza le stringhe stampate")
                try:
                    fp = open(csvNewFileLocalPath, "wb")
                    bytes2send = bytearray(streamFile, "utf-8")
                    fp.write(bytes2send)
                except OSError:
                    Logger().error("Errore apertura file: "+csvNewFileLocalPath)
                    self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    fp.close()
                    self.sleep(1)
                    continue

                fp.close()

                stepToProcess += 1
                self.csvBuildProcessStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                Logger().info("Generazione nuovo file csv OK")

            elif stepToProcess == CSVRegeneratorStep.SEND_CSV_TO_LASER:

                Logger().info("Invio file "+csvNewFilename+" al laser")
                self.sendCsvToLaserStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)

                if not isFtpConnected:
                    isFtpConnected = self.connectFtp(ftpController)
                    if not isFtpConnected:
                        self.sendCsvToLaserStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                        self.sleep(1)
                        continue

                try:
                    ftpController.cwd(laserFTPRemotePath)
                    Logger().info("Upload file: "+csvFilename)
                    cmd = "STOR " + csvFilename
                    Logger().debug("Comando: " + cmd)
                    fp = open(csvNewFileLocalPath, "rb")
                    ftpController.storbinary(cmd, fp)

                except ftplib.all_errors as ftpErr:
                    Logger().error("Error on FTP:" + str(ftpErr))
                    self.sendCsvToLaserStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    ftpController.close()
                    isFtpConnected = False
                    self.sleep(1)
                    continue

                stepToProcess += 1
                self.sendCsvToLaserStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                Logger().info("Invio file "+csvNewFilename+" al laser OK")

            elif stepToProcess == CSVRegeneratorStep.SEND_CSV_TO_CAMERA:

                Logger().info("Invio nuovo file "+csvFilename+" alla camera")
                self.sendCsvToCameraStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)

                try:
                    shutil.copy(csvNewFileLocalPath, csvCameraPath)
                except:
                    Logger().error("Impossibile copiare il nuovo fil csv in camera: " + csvNewFileLocalPath)
                    self.sendCsvToCameraStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
                    self.sleep(1)
                    continue

                self.sendCsvToCameraStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
                stepToProcess += 1
                Logger().info("Invio nuovo file " + csvFilename + " alla camera OK")


        Logger().info("Processo terminato correttamente")
        if isFtpConnected:
            ftpController.close()

        self.exit(0)


        ########################################################################################################
        ########################################################################################################
        ########################################################################################################

        #
        # # controllo che ci siano i file da scaricare nella cartella del laser (lista passata)
        # Logger().info("Controllo esistenza file error.txt e lista.csv nel laser")
        # for item in laserFileList:
        #     if item.lower() == errorFilename.lower():
        #         itemFounded += 1
        #         Logger().debug(errorFilename+" OK")
        #     if item.lower() == csvFilename.lower():
        #         itemFounded += 1
        #         Logger().debug(csvFilename+" OK")
        #     canContinue = itemFounded == 2
        #     if canContinue:
        #         break
        #
        # if not canContinue:
        #     Logger().error("Uno o entrambi i file non sono presenti")
        #     errorCode = ThreadExitCode.FILES_NOT_FOUNDED
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " +str(errorCode))
        #     return
        #
        #
        # # mi collego in FTP al laser
        # Logger().info("Connessione FTP al laser")
        # self.downloadStepSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        # ftpController = FTP()
        # ftpController.host = laserFTPAddress
        # ftpController.port = laserFTPPort
        # try:
        #     ftpController.connect()
        #     ftpController.login()
        # except ftplib.all_errors as ftpErr:
        #     Logger().error("Errore connesione FTP: " + str(ftpErr))
        #     errorCode = ThreadExitCode.FTP_LASER_CONNECTION_ERROR
        #     self.downloadStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        #
        # # scarico i file dal laser (rinominando quello appena usato)
        # Logger().info("Download file dal laser")
        # try:
        #     ftpController.cwd(laserFTPRemotePath)
        #
        #     # recupero il file lista.csv e lo elimino da ftp
        #     cmd = "RETR " + csvFilename
        #     Logger().debug("Comando: " + cmd)
        #     ftpController.retrbinary(cmd, open(CSVFileLocalPath, 'wb').write)
        #
        #     # recupero il file error.txt e lo elimino da ftp
        #     cmd = "RETR " + errorFilename
        #     Logger().debug("Comando: " + cmd)
        #     ftpController.retrbinary(cmd, open(errorFileLocalPath, 'wb').write)
        #
        # except ftplib.all_errors as ftpErr:
        #     Logger().error("Errore download file: " + str(ftpErr))
        #     errorCode = ThreadExitCode.FTP_LASER_DOWNLOAD_FILES_ERROR
        #     ftpController.close()
        #     self.downloadStepSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        #
        # # se ho scaricato il file csv, lo elimino dal laser
        # Logger().info("Rimozione file lista.csv dal laser")
        # try:
        #     Logger().debug("Eliminazione file \"" + csvFilename + "\" da laser")
        #     res = ftpController.delete(csvFilename)
        #
        # except ftplib.all_errors as ftpErr:
        #     Logger().error("Errore rimozione file lista.csv dal laser; errore: " + str(ftpErr))
        #     errorCode = ThreadExitCode.FTP_LASER_REMOVING_FILES_ERROR
        #     ftpController.close()
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        # self.downloadStepSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
        #
        #
        # # apro il file in error in lettura per vedere l'indice dell'ultima stringa stampata
        # self.creationCsvSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        # Logger().info("Lettura file errore per capire ultima stringa stampata")
        # lineToSeek = 0
        # fp = None
        # try:
        #     fp = open(errorFileLocalPath)
        #     lineStr = fp.readline()
        #     lastPrintedString = fp.readline()
        #     Logger().debug("Line: "+lineStr)
        #     Logger().debug("LastPrintedString: " + lastPrintedString)
        #     lineToSeek = int(lineStr)
        #     lineToSeek += rowMargin
        # except OSError:
        #     canContinue = False
        #     errorCode = ThreadExitCode.ERROR_LOCAL_FILE_OPENING_ERROR
        #     Logger().error("Impossibile aprire il file: " + errorFileLocalPath)
        # except ValueError:
        #     canContinue = False
        #     errorCode = ThreadExitCode.ERROR_LOCAL_FILE_READING_ERROR
        #     Logger().error("Impossibile convertire da string a intero il numero di riga stampata")
        # finally:
        #     fp.close()
        #
        # if not canContinue:
        #     self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        #
        # # creo la lista di stringhe scartando quelle gia' stampate
        # streamFile = None
        # Logger().info("Lettura file locale " + csvFilename + " escludendo le stringhe stampate")
        # try:
        #     fp = open(CSVFileLocalPath, newline="\r\n", encoding="utf-8")
        #     for rowCounter in range(lineToSeek):
        #         fp.readline()
        #     streamFile = fp.read()
        # except OSError:
        #     canContinue = False
        #     Logger().error("Impossibile aprire il file: " + CSVFileLocalPath)
        # finally:
        #     fp.close()
        #
        # if not canContinue:
        #     errorCode = ThreadExitCode.CSV_LOCAL_FILE_OPENING_ERROR
        #
        # if streamFile==None or len(streamFile)==0:
        #     Logger().error("Lista vuota")
        #     errorCode = ThreadExitCode.CSV_LOCAL_FILE_EMPTY
        #
        # if errorCode != ThreadExitCode.NO_ERROR:
        #     self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        #
        # # creo il nuovo file csv con la nuova lista
        # Logger().info("Scrittura file "+ csvNewFilename + " senza le stringhe stampate")
        # try:
        #     fp = open(CSVNewFileLocalPath, "wb")
        #     bytes2send = bytearray(streamFile, "utf-8")
        #     fp.write(bytes2send)
        # except OSError:
        #     canContinue = False
        #     Logger().error("Impossibile aprire il file: " + CSVNewFileLocalPath)
        #     errorCode = ThreadExitCode.CSV_NEW_LOCAL_FILE_WRITING_ERROR
        # finally:
        #     fp.close()
        #
        # if errorCode != ThreadExitCode.NO_ERROR:
        #     self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        # self.creationCsvSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
        #
        #
        # # invio il nuovo file csv al laser
        # Logger().info("Invio file "+csvNewFilename+" al laser")
        # self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        # try:
        #     ftpController.cwd(laserFTPRemotePath)
        #     cmd = "STOR " + csvFilename
        #     Logger().debug("Comando: "+cmd)
        #     fp = open(CSVNewFileLocalPath, "rb")
        #     ftpController.storbinary(cmd, fp)
        #
        # except ftplib.all_errors as ftpErr:
        #     Logger().error("Error on FTP:" + str(ftpErr))
        #     errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
        #     ftpController.close()
        #
        # if errorCode != ThreadExitCode.NO_ERROR:
        #     self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        #
        # # rimuovo il file error dal laser solo se tutto e' andato a buon fine
        # Logger().info("Rimozione error.txt dal laser")
        # try:
        #     Logger().debug("Eliminazione file \"" + errorFilename + "\" dal laser")
        #     res = ftpController.delete(errorFilename)
        #
        # except ftplib.all_errors as ftpErr:
        #     Logger().error("Error on FTP:" + str(ftpErr))
        #     ftpController.close()
        #     errorCode = ThreadExitCode.FTP_LASER_REMOVING_FILES_ERROR
        #     self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        # self.sendingLaserSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
        #
        #
        # # cancello il file csv dalla camera
        # Logger().info("Rimozione file "+csvFilename+" dalla camera")
        # self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.IN_PROGRESS)
        # csvCameraPath = cameraPath + "\\" + csvFilename
        # try:
        #     if os.path.exists(csvCameraPath):
        #         Logger().debug("Rimozione vecchio file .csv dalla camera")
        #         os.remove(csvCameraPath)
        # except OSError as ex:
        #     errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
        #     Logger().error("Impossibile rimuovere il file: " + csvCameraPath)
        #
        # if errorCode != ThreadExitCode.NO_ERROR:
        #     self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #     self.exitCodeSignal.emit(errorCode)
        #     Logger().error("Codice uscita: " + str(errorCode))
        #     return
        #
        #
        # # invio il nuovo file csv alla camera
        # Logger().info("Invio nuovo file lista.csv alla camera")
        # try:
        #     shutil.copy(CSVNewFileLocalPath, csvCameraPath)
        # except:
        #     errorCode = ThreadExitCode.FTP_LASER_SENDING_FILE_ERROR
        #     Logger().error("Impossibile copiare il nuovo fil csv in camera: " + CSVNewFileLocalPath)
        #
        # if errorCode != ThreadExitCode.NO_ERROR:
        #     self.exitCodeSignal.emit(errorCode)
        #     self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.ENDED_KO)
        #
        # Logger().info("Processo terminato correttamente")
        # self.sendingCameraSignal.emit(CSVRegeneratorStepStatus.ENDED_OK)
        # self.exitCodeSignal.emit(errorCode)
        # Logger().error("Codice uscita: " + str(errorCode))
        # return
