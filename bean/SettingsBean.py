from PySide2.QtCore import QObject, Property, Signal


class SettingsBean(QObject):

    cameraRemotePathChanged = Signal()
    cameraPollingTimeMsChanged = Signal()

    laserIpChanged = Signal()
    laserPortChanged = Signal()
    laserPollingTimeMsChanged = Signal()
    laserRemotePathChanged = Signal()

    localRowMarginChanged = Signal()
    localCsvFilenameChanged = Signal()
    localLaserErrorFilenameChanged = Signal()
    localLoadingPathChanged = Signal()
    localDownloadingPathChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__cameraRemotePath: str = ""
        self.__cameraPollingTimeMs = 0

        self.__laserIp: str = ""
        self.__laserPort: int = 0
        self.__laserPollingTimeMs = 0
        self.__laserRemotePath: str = ""

        self.__localRowMargin: int = 0
        self.__localCsvFilename: str = ""
        self.__localLaserErrorFilename: str = ""
        self.__localLoadingPath: str = ""
        self.__localDownloadingPath: str = ""

    def getCameraRemotePath(self) -> str:
        return self.__cameraRemotePath

    def setCameraRemotePath(self, remotePath: str):
        if self.__cameraRemotePath.lower() != remotePath.lower():
            self.__cameraRemotePath = remotePath
            self.cameraRemotePathChanged.emit()

    def getCameraPollingTimeMs(self) -> int:
        return self.__cameraPollingTimeMs

    def setCameraPollingTimeMs(self, pollingTimeMs: int):
        if pollingTimeMs != self.__cameraPollingTimeMs:
            self.__cameraPollingTimeMs = pollingTimeMs
            self.cameraPollingTimeMsChanged.emit()

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
        if self.__laserRemotePath.lower() != remotePath.lower():
            self.__laserRemotePath = remotePath
            self.laserRemotePathChanged.emit()

    def getLocalRowMargin(self) -> int:
        return self.__localRowMargin

    def setLocalRowMargin(self, margin: int):
        if self.__localRowMargin != margin:
            self.__localRowMargin = margin
            self.localRowMarginChanged.emit()

    def getLocalCsvFilename(self):
        return self.__localCsvFilename

    def setLocalCsvFilename(self, csvFilename: str):
        if self.__localCsvFilename.lower() != csvFilename.lower():
            self.__localCsvFilename = csvFilename
            self.localCsvFilenameChanged.emit()

    def getLocalLaserErrorFilename(self):
        return self.__localLaserErrorFilename

    def setLocalLaserErrorFilename(self, errorFilename: str):
        if self.__localLaserErrorFilename.lower() != errorFilename.lower():
            self.__localLaserErrorFilename = errorFilename
            self.localLaserErrorFilenameChanged.emit()

    def getLocalLoadingPath(self):
        return self.__localLoadingPath

    def setLocalLoadingPath(self, loadingPath: str):
        if self.__localLoadingPath.lower() != loadingPath.lower():
            self.__localLoadingPath = loadingPath
            self.localLoadingPathChanged.emit()

    def getLocalDownloadingPath(self):
        return self.__localDownloadingPath

    def setLocalDownloadingPath(self, downloadingPath: str):
        if self.__localDownloadingPath.lower() != downloadingPath.lower():
            self.__localDownloadingPath = downloadingPath
            self.localDownloadingPathChanged.emit()

    pLaserIp = Property(str, getLaserIp, setLaserIp, notify=laserIpChanged)
    pLaserPort = Property(int, getLaserPort, setLaserPort, notify=laserPortChanged)
    pLaserPollingTimeMs = Property(int, getLaserPollingTimeMs, setLaserPollingTimeMs, notify=laserPollingTimeMsChanged)
    pLaserRemotePath = Property(str, getLaserRemotePath, setLaserRemotePath, notify=laserRemotePathChanged)

    pCameraRemotePath = Property(str, getCameraRemotePath, setCameraRemotePath, notify=cameraRemotePathChanged)
    pCameraPollingTimeMs = Property(int, getCameraPollingTimeMs, setCameraPollingTimeMs,
                                    notify=cameraPollingTimeMsChanged)

    pLocalRowMargin = Property(int, getLocalRowMargin, setLocalRowMargin, notify=localRowMarginChanged)
    pLocalCsvFilename = Property(str, getLocalCsvFilename, setLocalCsvFilename, notify=localCsvFilenameChanged)
    pLocalLaserErrorFilename = Property(str, getLocalLaserErrorFilename, setLocalLaserErrorFilename,
                                        notify=localLaserErrorFilenameChanged)
    pLocalLoadingPath = Property(str, getLocalLoadingPath, setLocalLoadingPath, notify=localLoadingPathChanged)
    pLocalDownloadingPath = Property(str, getLocalDownloadingPath, setLocalDownloadingPath,
                                     notify=localDownloadingPathChanged)
