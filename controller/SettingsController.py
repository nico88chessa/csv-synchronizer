from PySide2.QtCore import QObject, Slot, Property, Signal, QThread

from bean.SettingsBean import SettingsBean
from Settings import Settings
from core.CSVWatcher import CSVWatcher


class SettingsController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

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

        self.__settingsBean.setCameraIp(s.getCameraIp())
        self.__settingsBean.setCameraPort(s.getCameraPort())
        self.__settingsBean.setCameraPollingTimeMs(s.getCameraPollingTimeMs())
        self.__settingsBean.setCameraRemotePath(s.getCameraRemotePath())

    @Slot(None)
    def saveParameters(self):
        s = Settings()

        s.setLaserIp(self.__settingsBean.getLaserIp())
        s.setLaserPort(self.__settingsBean.getLaserPort())
        s.setLaserPollingTime(self.__settingsBean.getLaserPollingTimeMs())
        s.setLaserRemotePath(self.__settingsBean.getLaserRemotePath())
        s.setCameraIp(self.__settingsBean.getCameraIp())
        s.setCameraPort(self.__settingsBean.getCameraPort())
        s.setCameraPollingTimeMs(self.__settingsBean.getCameraPollingTimeMs())
        s.setCameraRemotePath(self.__settingsBean.getCameraRemotePath())

        s.saveCurrentParameters()
