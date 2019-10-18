from PySide2.QtCore import QObject, Slot, Property, Signal, QDir, QUrl, QThread, QMetaObject

from bean.SettingsBean import SettingsBean
from bean.ProcessBean import ProcessBean
from Settings import Settings
from core.CSVRegenerator import CSVRegenerator
from core.FSWatcher import FSWatcher
from core.FTPWatcher import FTPWatcher
from core.SSHWatcher import SSHWatcher


class ProcessController(QObject):

    processBeanChanged = Signal()
    settingsBeanChanged = Signal()
    closingApplicationSignal = Signal()
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
                QMetaObject.invokeMethod(self.__ftpWatcher, "stopProcess")

        if isinstance(self.__fsWatcherThread, QThread):
            if self.__processBean.isCameraWatcherRunning():
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
        self.__settingsBean.setLocalLoadingPath(path)

    @Slot(str)
    def setLocalDownloadingPath(self, path: str):
        path = self.handleUrlPath(path)
        self.__settingsBean.setLocalDownloadingPath(path)

    @Slot(str)
    def setCameraRemotePath(self, path: str):
        path = self.handleUrlPath(path)
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

        self.__ftpWatcherThread.start()

    @Slot(None)
    def stopLaserWatcher(self):
        QMetaObject.invokeMethod(self.__ftpWatcher, "stopProcess")

    @Slot(None)
    def startCameraWatcher(self):
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

        self.__fsWatcherThread.start()

    @Slot(None)
    def stopCameraWatcher(self):
        QMetaObject.invokeMethod(self.__fsWatcher, "stopProcess")

    @Slot(None)
    def sendCsvFileToDevices(self):
        # TODO
        pass

    def analizeFolderItems(self):

        if self.__csvRegeneratorThread.isRunning():
            return

        items = self.getProcessBean().getLaserFolderItems()
        isCSVExpired = False

        for item in items:
            if item.lower() == 'error.txt'.lower():
                isCSVExpired = True
                break

        if isCSVExpired:
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

            self.__csvRegeneratorThread.downloadStepSignal.connect(
                lambda value: self.__processBean.setCsvRegenerationDownloadStepStatus(value))

            self.__csvRegeneratorThread.creationCsvSignal.connect(
                lambda value: self.__processBean.setCsvRegenerationCreationStepStatus(value))

            self.__csvRegeneratorThread.sendingLaserSignal.connect(
                lambda value: self.__processBean.setCsvRegenerationSendingLaserStatus(value))

            self.__csvRegeneratorThread.sendingCameraSignal.connect(
                lambda value: self.__processBean.setCsvRegenerationSendingCameraStatus(value))

            self.__csvRegeneratorThread.started.connect(
                lambda value: self.__processBean.setCsvRegenerationThreadRunning(True))

            self.__csvRegeneratorThread.finished.connect(
                lambda value: self.__processBean.setCsvRegenerationThreadRunning(False))

            self.__csvRegeneratorThread.start()
