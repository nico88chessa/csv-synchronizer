from typing import Type

from PySide2.QtCore import QObject, Property, Signal
from PySide2.QtQml import qmlRegisterType


class SettingsBean(QObject):

    @Signal
    def laserIpChanged(self): pass

    @Signal
    def laserPortChanged(self): pass

    @Signal
    def cameraIpChanged(self): pass

    @Signal
    def cameraPortChanged(self): pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self._laserIp = str
        self._laserPort = int
        self._cameraIp = str
        self._cameraPort = int

    def getLaserIp(self):
        return self._laserIp

    def setLaserIp(self, ip):
        if (ip != self._laserIp):
            self._laserIp = ip
            self.laserIpChanged.emit()

    def getLaserPort(self) -> int:
        return self._laserPort

    def setLaserPort(self, port : int):
        if (port != self._laserPort):
            self._laserPort = port
            self.laserPortChanged.emit()

    def getCameraIp(self):
        return self._cameraIp

    def setCameraIp(self, ip):
        if (ip != self._cameraIp):
            self._cameraIp = ip
            self.cameraIpChanged.emit()

    def getCameraPort(self) -> int:
        return self._cameraPort

    def setCameraPort(self, port: int):
        if (port != self._cameraPort):
            self._cameraPort = port
            self.cameraPortChanged.emit()

    pLaserIp = Property(str, getLaserIp, setLaserIp, notify=laserIpChanged)
    pLaserPort = Property(int, getLaserPort, setLaserPort, notify=laserPortChanged)
    pCameraIp = Property(str, getCameraIp, setCameraIp, notify=cameraIpChanged)
    pCameraPort = Property(int, getCameraPort, setCameraPort, notify=cameraPortChanged)
