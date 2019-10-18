from PySide2.QtCore import QObject, Slot, Property, Signal, QThread

from bean.SettingsBean import SettingsBean
from Settings import Settings
from core.FTPWatcher import FTPWatcher


class SettingsController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__settingsBean: SettingsBean = None

    @Signal
    def settingsBeanChanged(self): pass

    def getSettingsBean(self):
        return self.__settingsBean

    def setSettingsBean(self, bean: SettingsBean):
        self.__settingsBean = bean
        self.settingsBeanChanged.emit()

    pSettingsBean = Property(SettingsBean, getSettingsBean, setSettingsBean, notify=settingsBeanChanged)

    @Slot()
    def initBean(self):
        s = Settings()

        self.__settingsBean.setLaserIp(s.getLaserIp())
        self.__settingsBean.setLaserPort(s.getLaserPort())
        self.__settingsBean.setLaserPollingTimeMs(s.getLaserPollingTime())
        self.__settingsBean.setLaserRemotePath(s.getLaserRemotePath())

        self.__settingsBean.setCameraPollingTimeMs(s.getCameraPollingTimeMs())
        self.__settingsBean.setCameraRemotePath(s.getCameraRemotePath())

        self.__settingsBean.setLocalRowMargin(s.getLocalRowMargin())
        self.__settingsBean.setLocalCsvFilename(s.getLocalCsvFilename())
        self.__settingsBean.setLocalLaserErrorFilename(s.getLocalLaserErrorFilename())
        self.__settingsBean.setLocalLoadingPath(s.getLocalLoadingPath())
        self.__settingsBean.setLocalDownloadingPath(s.getLocalDownloadingPath())

    @Slot(None)
    def saveParameters(self):
        s = Settings()

        s.setLaserIp(self.__settingsBean.getLaserIp())
        s.setLaserPort(self.__settingsBean.getLaserPort())
        s.setLaserPollingTime(self.__settingsBean.getLaserPollingTimeMs())
        s.setLaserRemotePath(self.__settingsBean.getLaserRemotePath())

        s.setCameraPollingTimeMs(self.__settingsBean.getCameraPollingTimeMs())
        s.setCameraRemotePath(self.__settingsBean.getCameraRemotePath())

        s.setLocalRowMargin(self.__settingsBean.getLocalRowMargin())
        s.setLocalCsvFilename(self.__settingsBean.getLocalCsvFilename())
        s.setLocalLaserErrorFilename(self.__settingsBean.getLocalLaserErrorFilename())
        s.setLocalLoadingPath(self.__settingsBean.getLocalLoadingPath())
        s.setLocalDownloadingPath(self.__settingsBean.getLocalDownloadingPath())

        s.saveCurrentParameters()
