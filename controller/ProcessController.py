from PySide2.QtCore import QObject, Slot, Property, Signal, QDir, QUrl, QByteArray, QThread, QMetaObject, Qt
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide2.QtQml import QQmlApplicationEngine
from pyside2uic.properties import QtCore

from bean.SettingsBean import SettingsBean
from bean.ProcessBean import ProcessBean
from Settings import Settings
from core.CSVWatcher import CSVWatcher


class ProcessController(QObject):

    @Signal
    def processBeanChanged(self): pass

    @Signal
    def settingsBeanChanged(self):
        pass

    @Signal
    def closingApplicationSignal(self): pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__processBean : ProcessBean
        self.__settingsBean : SettingsBean
        self.__watcherThread = None
        self.__csvWatcher = None
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
        if isinstance(self.__watcherThread, QThread):
            QMetaObject.invokeMethod(self.__csvWatcher, "stopProcess")#, Qt.QueuedConnection)

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
        pathOk: str
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
    def startWatcher(self):
        self.__watcherThread = QThread()
        self.__watcherThread.setObjectName("WatcherThread")
        self.__csvWatcher = CSVWatcher(remotePath=self.getSettingsBean().getLaserRemotePath(),
                                       ftpAddress=self.getSettingsBean().getLaserIp(),
                                       intervalMs=self.getSettingsBean().getLaserPollingTimeMs(),
                                       ftpPort=self.getSettingsBean().getLaserPort())
        self.__csvWatcher.moveToThread(self.__watcherThread)

        self.__watcherThread.started.connect(self.__csvWatcher.startProcess)
        self.__csvWatcher.stoppedSignal.connect(self.__watcherThread.quit)
        self.__watcherThread.finished.connect(self.__watcherThread.deleteLater)
        self.__watcherThread.finished.connect(self.__csvWatcher.deleteLater)

        self.__watcherThread.start()
