from PySide2.QtCore import QObject, Slot, Property, Signal, QDir, QUrl, QByteArray, QThread, QMetaObject, Qt
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide2.QtQml import QQmlApplicationEngine
from pyside2uic.properties import QtCore

from bean.SettingsBean import SettingsBean
from bean.ProcessBean import ProcessBean
from Settings import Settings
from core.FSWatcher import FSWatcher
from core.CSVWatcher import CSVWatcher
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
        self.__csvWatcherThread: QThread = None
        self.__csvWatcher: CSVWatcher = None
        self.__sshWatcher: SSHWatcher = None
        self.__fsWatcher: FSWatcher = None
        self.__fsWatcherThread: QThread = None
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
        if isinstance(self.__csvWatcherThread, QThread):
            if self.__processBean.isLaserWatcherRunning():
                QMetaObject.invokeMethod(self.__csvWatcher, "stopProcess")

        if isinstance(self.__fsWatcherThread, QThread):
            if self.__processBean.isCameraWatcherRunning():
                QMetaObject.invokeMethod(self.__fsWatcher, "stopProcess")

    @Slot()
    def initBean(self):
        s = Settings()
        self.__processBean.setLocalFolderPath(s.getLocalFolderPath())

    @Slot(None)
    def saveParameters(self):
        s = Settings()

        s.setFolderPath(self.__processBean.getFolderPath())

        s.saveCurrentParameters()

    @Slot(str)
    def handleUrlPath(self, path: str):
        url = QUrl(path)
        pathOk=""
        if url.isLocalFile():
            pathOk = QDir.toNativeSeparators(url.toLocalFile())
        else:
            pathOk = path
        self.__processBean.setFolderPath(pathOk)

    @Slot(str, result=str)
    def getUrlFromNativePath(self, path: str):
        path = QDir.fromNativeSeparators(path)
        url = QUrl.fromLocalFile(path)
        res = str(url.toString())
        return res

    @Slot(None)
    def startLaserWatcher(self):
        self.__csvWatcherThread = QThread()
        self.__csvWatcherThread.setObjectName("CSVWatcherThread")
        self.__csvWatcher = CSVWatcher(remotePath=self.getSettingsBean().getLaserRemotePath(),
                                       ftpAddress=self.getSettingsBean().getLaserIp(),
                                       intervalMs=self.getSettingsBean().getLaserPollingTimeMs(),
                                       ftpPort=self.getSettingsBean().getLaserPort())
        self.__csvWatcher.moveToThread(self.__csvWatcherThread)

        self.__csvWatcherThread.started.connect(self.__csvWatcher.startProcess)
        self.__csvWatcher.itemsPathUpdatedSignal.connect(
            lambda items: self.__processBean.setLaserFolderItems(items)
        )
        # self.__csvWatcher.isConnectedSignal.connect(self.laserFolderWatcherConnectedSignal)
        self.__csvWatcher.isConnectedSignal.connect(
            lambda isConnected: self.__processBean.setLaserConnectionUp(isConnected)
        )

        self.__csvWatcher.startedSignal.connect(
            lambda: self.__processBean.setLaserWatcherRunning(True)
        )
        self.__csvWatcher.stoppedSignal.connect(
            lambda: self.__processBean.setLaserWatcherRunning(False)
        )

        self.__csvWatcher.stoppedSignal.connect(self.__csvWatcherThread.quit)
        self.__csvWatcherThread.finished.connect(self.__csvWatcherThread.deleteLater)
        self.__csvWatcherThread.finished.connect(self.__csvWatcher.deleteLater)

        self.__csvWatcherThread.start()

    @Slot(None)
    def stopLaserWatcher(self):
        QMetaObject.invokeMethod(self.__csvWatcher, "stopProcess")

    @Slot(None)
    def startCameraWatcher(self):
        self.__fsWatcherThread = QThread()
        self.__fsWatcherThread.setObjectName("FSWatcherThread")
        self.__fsWatcher = FSWatcher(path=self.getSettingsBean().getCameraRemotePath(),
                                     intervalMs=self.getSettingsBean().getCameraPollingTimeMs())
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
