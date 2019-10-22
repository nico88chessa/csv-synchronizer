import ftplib
import os
import shutil
from ftplib import FTP

from PySide2.QtCore import QObject, Slot, Property, Signal, QDir, QUrl, QThread, QMetaObject

from bean.SettingsBean import SettingsBean
from bean.ProcessBean import ProcessBean
from Settings import Settings
from core.CSVRegenerator import CSVRegenerator
from core.FSWatcher import FSWatcher
from core.FTPWatcher import FTPWatcher
from core.Logger import Logger
from core.SSHWatcher import SSHWatcher


class ProcessController(QObject):

    processBeanChanged = Signal()
    settingsBeanChanged = Signal()
    closingApplicationSignal = Signal()
    showDialogSignal = Signal(str, arguments=['message'])
    # laserFolderWatcherConnectedSignal = Signal(bool, arguments=['isConnected'])

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__processBean: ProcessBean = None
        self.__settingsBean: SettingsBean = None
        self.__ftpWatcherThread: QThread = None
        self.__ftpWatcher: FTPWatcher = None
        self.__sshWatcher: SSHWatcher = None
        self.__fsWatcher: FSWatcher = None
        self.__fsWatcherThread: QThread = None
        self.__csvRegeneratorThread = CSVRegenerator()
        self.setupSignalsAndSlots()

    def getProcessBean(self):
        return self.__processBean

    def setProcessBean(self, bean: ProcessBean):
        self.__processBean = bean
        self.processBeanChanged.emit()

    def getSettingsBean(self):
        return self.__settingsBean

    def setSettingsBean(self, bean: SettingsBean):
        self.__settingsBean = bean
        self.settingsBeanChanged.emit()

    pProcessBean = Property(ProcessBean, getProcessBean, setProcessBean, notify=processBeanChanged)
    pSettingsBean = Property(SettingsBean, getSettingsBean, setSettingsBean, notify=settingsBeanChanged)

    def setupSignalsAndSlots(self):
        self.closingApplicationSignal.connect(self.freeResources)

    @Slot()
    def freeResources(self):
        if isinstance(self.__ftpWatcherThread, QThread):
            if self.__processBean.isLaserWatcherRunning():
                Logger().debug("Stop laser watcher thread")
                QMetaObject.invokeMethod(self.__ftpWatcher, "stopProcess")

        if isinstance(self.__fsWatcherThread, QThread):
            if self.__processBean.isCameraWatcherRunning():
                Logger().debug("Stop camera watcher thread")
                QMetaObject.invokeMethod(self.__fsWatcher, "stopProcess")

    @Slot()
    def initBean(self):
        pass

    @Slot(None)
    def saveParameters(self):
        s = Settings()
        s.saveCurrentParameters()

    @Slot(str)
    def setLocalLoadingPath(self, path: str):
        path = self.handleUrlPath(path)
        Logger().debug("Impostato loading path: " + path)
        self.__settingsBean.setLocalLoadingPath(path)

    @Slot(str)
    def setLocalDownloadingPath(self, path: str):
        path = self.handleUrlPath(path)
        Logger().debug("Impostato downloading path: " + path)
        self.__settingsBean.setLocalDownloadingPath(path)

    @Slot(str)
    def setCameraRemotePath(self, path: str):
        path = self.handleUrlPath(path)
        Logger().debug("Impostato camera path: " + path)
        self.__settingsBean.setCameraRemotePath(path)

    def handleUrlPath(self, path: str) -> str:
        url = QUrl(path)
        pathOk=""
        if url.isLocalFile():
            pathOk = QDir.toNativeSeparators(url.toLocalFile())
        else:
            pathOk = path
        return pathOk

    @Slot(str, result=str)
    def getUrlFromNativePath(self, path: str):
        path = QDir.fromNativeSeparators(path)
        url = QUrl.fromLocalFile(path)
        res = str(url.toString())
        return res

    @Slot(None)
    def startLaserWatcher(self):
        Logger().debug("Start laser watcher thread")

        self.__ftpWatcherThread = QThread()
        self.__ftpWatcherThread.setObjectName("CSVWatcherThread")
        self.__ftpWatcher = FTPWatcher(remotePath=self.__settingsBean.getLaserRemotePath(),
                                       ftpAddress=self.__settingsBean.getLaserIp(),
                                       intervalMs=self.__settingsBean.getLaserPollingTimeMs(),
                                       ftpPort=self.__settingsBean.getLaserPort())
        self.__ftpWatcher.moveToThread(self.__ftpWatcherThread)

        self.__ftpWatcherThread.started.connect(self.__ftpWatcher.startProcess)
        self.__ftpWatcher.itemsPathUpdatedSignal.connect(
            lambda items: (
                self.__processBean.setLaserFolderItems(items),
                self.analizeFolderItems()
            )
        )
        # self.__csvWatcher.isConnectedSignal.connect(self.laserFolderWatcherConnectedSignal)
        self.__ftpWatcher.isConnectedSignal.connect(
            lambda isConnected: self.__processBean.setLaserConnectionUp(isConnected)
        )

        self.__ftpWatcher.startedSignal.connect(
            lambda: self.__processBean.setLaserWatcherRunning(True)
        )
        self.__ftpWatcher.stoppedSignal.connect(
            lambda: self.__processBean.setLaserWatcherRunning(False)
        )

        self.__ftpWatcher.stoppedSignal.connect(self.__ftpWatcherThread.quit)
        self.__ftpWatcherThread.finished.connect(self.__ftpWatcherThread.deleteLater)
        self.__ftpWatcherThread.finished.connect(self.__ftpWatcher.deleteLater)

        Logger().debug("Laser watcher thread avviato")

        self.__ftpWatcherThread.start()

    @Slot(None)
    def stopLaserWatcher(self):
        Logger().debug("Stop laser watcher thread")
        QMetaObject.invokeMethod(self.__ftpWatcher, "stopProcess")

    @Slot(None)
    def startCameraWatcher(self):
        Logger().debug("Start camera watcher thread")

        self.__fsWatcherThread = QThread()
        self.__fsWatcherThread.setObjectName("FSWatcherThread")
        self.__fsWatcher = FSWatcher(path=self.__settingsBean.getCameraRemotePath(),
                                     intervalMs=self.__settingsBean.getCameraPollingTimeMs())
        self.__fsWatcher.moveToThread(self.__fsWatcherThread)

        self.__fsWatcherThread.started.connect(self.__fsWatcher.startProcess)
        self.__fsWatcher.itemsPathUpdatedSignal.connect(
            lambda items: self.__processBean.setCameraFolderItems(items)
        )
        self.__fsWatcher.isConnectedSignal.connect(
            lambda isConnected: self.__processBean.setCameraConnectionUp(isConnected)
        )
        self.__fsWatcher.startedSignal.connect(
            lambda: self.__processBean.setCameraWatcherRunning(True)
        )
        self.__fsWatcher.stoppedSignal.connect(
            lambda: self.__processBean.setCameraWatcherRunning(False)
        )

        self.__fsWatcher.stoppedSignal.connect(self.__fsWatcherThread.quit)
        self.__fsWatcherThread.finished.connect(self.__fsWatcherThread.deleteLater)
        self.__fsWatcherThread.finished.connect(self.__fsWatcher.deleteLater)

        Logger().debug("Camera watcher thread avviato")

        self.__fsWatcherThread.start()

    @Slot(None)
    def stopCameraWatcher(self):
        Logger().debug("Stop camera watcher thread")
        QMetaObject.invokeMethod(self.__fsWatcher, "stopProcess")

    @Slot(None)
    def sendCsvFileToDevices(self):

        localloadingPath = self.__settingsBean.getLocalLoadingPath()
        csvFilename = self.__settingsBean.getLocalCsvFilename()
        csvLocalPath = localloadingPath + "\\" + csvFilename
        cameraPath = self.__settingsBean.getCameraRemotePath()
        csvCameraPath = cameraPath + "\\" + csvFilename

        if not os.path.exists(csvLocalPath):
            Logger().error("File "+csvLocalPath+" non trovato")
            self.showDialogSignal.emit("Nessun file trovato nella cartella locale")
            return

        # invio file csv al laser
        Logger().info("Invio file " + csvFilename + " al laser")

        ftpController = FTP()
        ftpController.host = self.__settingsBean.getLaserIp()
        ftpController.port = self.__settingsBean.getLaserPort()
        laserFTPRemotePath = self.__settingsBean.getLaserRemotePath()

        try:
            ftpController.connect()
            ftpController.login()
            ftpController.cwd(laserFTPRemotePath)
            cmd = "STOR " + csvFilename
            Logger().debug("Comando: " + cmd)
            fp = open(csvLocalPath, "rb")
            ftpController.storbinary(cmd, fp)

        except ftplib.all_errors as ftpErr:
            Logger().error("Error on FTP:" + str(ftpErr))
            ftpController.close()
            self.showDialogSignal.emit("Errore invio file csv al laser")
            return

        # invio il file csv alla camera
        Logger().info("Invio file " + csvFilename + " alla camera")
        try:
            shutil.copy(csvLocalPath, csvCameraPath)
        except:
            Logger().error("Impossibile copiare il file csv in camera")
            self.showDialogSignal.emit("Errore invio file csv alla camera")
            return

        self.__processBean.setCsvRegThreadCsvNewEmpty(False)
        self.showDialogSignal.emit("Invio completato correttamente")

    @Slot(bool)
    def changeStopRequestValue(self, stop: bool):
        self.__csvRegeneratorThread.setStopRequest(stop)
        self.__processBean.setStopRegThread(stop)

    def analizeFolderItems(self):


        # Logger().debug("Analisi lista file laser")

        items = self.getProcessBean().getLaserFolderItems()
        isErrorFounded = False
        isCsvFounded = False

        for item in items:
            if item.lower() == self.__settingsBean.getLocalLaserErrorFilename().lower():
                # Logger().debug("Trovato error file: "+self.__settingsBean.getLocalLaserErrorFilename().lower())
                isErrorFounded = True
            if item.lower() == self.__settingsBean.getLocalCsvFilename().lower():
                # Logger().debug("Trovato csv file: "+self.__settingsBean.getLocalCsvFilename().lower())
                isCsvFounded = True
            if isCsvFounded and isErrorFounded:
                break

        self.__processBean.setErrorFileFounded(isErrorFounded)

        if self.__csvRegeneratorThread.isRunning():
            return

        if self.__processBean.isStopRegThread():
            return

        if isCsvFounded and isErrorFounded:

            Logger().debug("Trovato error file: "+self.__settingsBean.getLocalLaserErrorFilename().lower())
            Logger().debug("Trovato csv file: "+self.__settingsBean.getLocalCsvFilename().lower())

            Logger().debug("Avvio thread per rigenerazione file")
            self.__csvRegeneratorThread.setLaserFileList(items)
            self.__csvRegeneratorThread.setLaserConnectionParameters(self.__settingsBean.getLaserIp(),
                                                                    self.__settingsBean.getLaserPort(),
                                                                    self.__settingsBean.getLaserRemotePath())

            self.__csvRegeneratorThread.setLocalLoadingPath(self.__settingsBean.getLocalLoadingPath())
            self.__csvRegeneratorThread.setLocalDownloadingPath(self.__settingsBean.getLocalDownloadingPath())

            self.__csvRegeneratorThread.setCameraConnectionParameters(self.__settingsBean.getCameraRemotePath())

            self.__csvRegeneratorThread.setCsvFilename(self.__settingsBean.getLocalCsvFilename())
            self.__csvRegeneratorThread.setErrorFilename(self.__settingsBean.getLocalLaserErrorFilename())

            self.__csvRegeneratorThread.setRowMargin(self.__settingsBean.getLocalRowMargin())

            self.__csvRegeneratorThread.cleanLocalFolderStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadCleanLocalFolderStatus(value))

            self.__csvRegeneratorThread.cleanCameraFolderStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadCleanCameraFolderStatus(value))

            self.__csvRegeneratorThread.renameLaserItemsStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadRenameLaserItemsStatus(value))

            self.__csvRegeneratorThread.downloadItemsFromLaserStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadDownloadItemsStatus(value))

            self.__csvRegeneratorThread.cleanLaserFolderStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadCleanLaserFolderStatus(value))

            self.__csvRegeneratorThread.csvBuildProcessStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadCsvCreationProcessStatus(value))

            self.__csvRegeneratorThread.sendCsvToLaserStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadSendCsvToLaserStatus(value))

            self.__csvRegeneratorThread.sendCsvToCameraStepSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadSendCsvToCameraStatus(value))

            self.__csvRegeneratorThread.exitCodeSignal.connect(
                lambda value: self.__processBean.setCsvRegThreadExitCode(value))

            self.__csvRegeneratorThread.started.connect(
                lambda: self.__processBean.setCsvRegThreadRunning(True))

            self.__csvRegeneratorThread.finished.connect(
                lambda: self.__processBean.setCsvRegThreadRunning(False))

            self.__csvRegeneratorThread.cvsNewFileEmptySignal.connect(
                lambda isEmpty: self.__processBean.setCsvRegThreadCsvNewEmpty(isEmpty))

            self.__csvRegeneratorThread.start()
