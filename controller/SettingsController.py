from PySide2.QtCore import QObject, Slot, Property, Signal
from PySide2.QtQml import QQmlApplicationEngine

from bean.SettingsBean import SettingsBean
from Settings import Settings


class SettingsController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._settingsBean = SettingsBean()

        # self.setupSignalsAndSlots()

        s = Settings()

        self._settingsBean.setLaserIp(s.getLaserIp())
        self._settingsBean.setLaserPort(s.getLaserPort())
        self._settingsBean.setCameraIp(s.getCameraIp())
        self._settingsBean.setCameraPort(s.getCameraPort())

    def getSettingsBean(self):
        return self._settingsBean

    pSettingsBean = Property(SettingsBean, getSettingsBean, constant=True)

    @Slot(None)
    def saveParameters(self):
        s = Settings()

        s.setLaserIp(self._settingsBean.getLaserIp())
        s.setLaserPort(self._settingsBean.getLaserPort())
        s.setCameraIp(self._settingsBean.getCameraIp())
        s.setCameraPort(self._settingsBean.getCameraPort())

        s.saveCurrentParameters()
