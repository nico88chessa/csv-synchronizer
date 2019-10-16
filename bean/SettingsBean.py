from PySide2.QtCore import QObject, Property, Signal


class SettingsBean(QObject):

    @Signal
    def laserIpChanged(self): pass

    @Signal
    def laserPortChanged(self): pass

    @Signal
    def laserPollingTimeMsChanged(self): pass

    @Signal
    def laserRemotePathChanged(self):
        pass

    @Signal
    def cameraIpChanged(self): pass

    @Signal
    def cameraPortChanged(self): pass

    @Signal
    def cameraPollingTimeMsChanged(self):
        pass

    @Signal
    def cameraRemotePathChanged(self):
        pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__laserIp: str = ""
        self.__laserPort: int = 0
        self.__laserPollingTimeMs = 0
        self.__laserRemotePath: str = ""
        self.__cameraIp: str = ""
        self.__cameraPort = 0
        self.__cameraPollingTimeMs = 0
        self.__cameraRemotePath: str = ""

    def getLaserIp(self):
        return self.__laserIp

    def setLaserIp(self, ip):
        if ip != self.__laserIp:
            self.__laserIp = ip
            self.laserIpChanged.emit()

    def getLaserPort(self) -> int:
        return self.__laserPort

    def setLaserPort(self, port: int):
        if port != self.__laserPort:
            self.__laserPort = port
            self.laserPortChanged.emit()

    def getLaserPollingTimeMs(self) -> int:
        return self.__laserPollingTimeMs

    def setLaserPollingTimeMs(self, pollingTimeMs: int):
        if pollingTimeMs != self.__laserPollingTimeMs:
            self.__laserPollingTimeMs = pollingTimeMs
            self.laserPollingTimeMsChanged.emit()

    def getLaserRemotePath(self) -> str:
        return self.__laserRemotePath

    def setLaserRemotePath(self, remotePath: str):
        if self.__laserRemotePath != remotePath:
            self.__laserRemotePath = remotePath
            self.laserRemotePathChanged.emit()

    def getCameraIp(self):
        return self.__cameraIp

    def setCameraIp(self, ip):
        if ip != self.__cameraIp:
            self.__cameraIp = ip
            self.cameraIpChanged.emit()

    def getCameraPort(self) -> int:
        return self.__cameraPort

    def setCameraPort(self, port: int):
        if port != self.__cameraPort:
            self.__cameraPort = port
            self.cameraPortChanged.emit()

    def getCameraPollingTimeMs(self) -> int:
        return self.__cameraPollingTimeMs

    def setCameraPollingTimeMs(self, pollingTimeMs: int):
        if pollingTimeMs != self.__cameraPollingTimeMs:
            self.__cameraPollingTimeMs = pollingTimeMs
            self.cameraPollingTimeMsChanged.emit()

    def getCameraRemotePath(self) -> str:
        return self.__cameraRemotePath

    def setCameraRemotePath(self, remotePath: str):
        if self.__cameraRemotePath != remotePath:
            self.__cameraRemotePath = remotePath
            self.cameraRemotePathChanged.emit()

    pLaserIp = Property(str, getLaserIp, setLaserIp, notify=laserIpChanged)
    pLaserPort = Property(int, getLaserPort, setLaserPort, notify=laserPortChanged)
    pLaserPollingTimeMs = Property(int, getLaserPollingTimeMs, setLaserPollingTimeMs, notify=laserPollingTimeMsChanged)
    pLaserRemotePath = Property(str, getLaserRemotePath, setLaserRemotePath, notify=laserRemotePathChanged)
    pCameraIp = Property(str, getCameraIp, setCameraIp, notify=cameraIpChanged)
    pCameraPort = Property(int, getCameraPort, setCameraPort, notify=cameraPortChanged)
    pCameraPollingTimeMs = Property(int, getCameraPollingTimeMs, setCameraPollingTimeMs,
                                    notify=cameraPollingTimeMsChanged)
    pCameraRemotePath = Property(str, getCameraRemotePath, setCameraRemotePath, notify=cameraRemotePathChanged)
