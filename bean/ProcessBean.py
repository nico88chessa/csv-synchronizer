from typing import List

from PySide2.QtCore import QObject, Property, Signal, QStringListModel, QMetaMethod

from core.CSVRegenerator import CSVRegeneratorStepStatus

class ProcessBean(QObject):

    __isCameraWatcherRunning: bool
    __isLaserWatcherRunning: bool

    laserFolderItemsChanged = Signal()
    cameraFolderItemsChanged = Signal()
    laserWatcherRunningChanged = Signal()
    cameraWatcherRunningChanged = Signal()
    laserConnectionUpChanged = Signal()
    cameraConnectionUpChanged = Signal()
    errorFileFoundedChanged = Signal()
    csvRegenerationThreadRunningChanged = Signal()
    csvRegenerationDownloadStepStatusChanged = Signal()
    csvRegenerationCreationStepStatusChanged = Signal()
    csvRegenerationSendingLaserStatusChanged = Signal()
    csvRegenerationSendingCameraStatusChanged = Signal()
    csvRegenerationExitCodeChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__laserFolderItems: List[str] = list()
        self.__cameraFolderItems: List[str] = list()
        self.__isLaserWatcherRunning = False
        self.__isCameraWatcherRunning = False
        self.__isLaserConnectionUp = False
        self.__isCameraConnectionUp = False
        self.__errorFileFounded = False
        self.__csvRegenerationThreadRunning: bool = False
        self.__csvRegenerationDownloadStepStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegenerationCreationStepStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegenerationSendingLaserStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegenerationSendingCameraStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegenerationExitCode: int = 0


    def getLaserFolderItems(self):
        return self.__laserFolderItems

    def setLaserFolderItems(self, items: list):
        isModified = False
        if len(self.__laserFolderItems) != len(items):
            isModified = True
        if not isModified:
            for i in items:
                if i not in self.__laserFolderItems:
                    isModified = True
                    break
        if isModified:
            self.__laserFolderItems = items
            self.laserFolderItemsChanged.emit()

    def getCameraFolderItems(self):
        return self.__cameraFolderItems

    def setCameraFolderItems(self, items: list):
        isModified = False
        if len(self.__cameraFolderItems) != len(items):
            isModified = True
        for i in items:
            if i not in self.__cameraFolderItems:
                isModified = True
                break
        if isModified:
            self.__cameraFolderItems = items
            self.cameraFolderItemsChanged.emit()

    def isLaserWatcherRunning(self):
        return self.__isLaserWatcherRunning

    def setLaserWatcherRunning(self, isRunning: bool):
        if self.__isLaserWatcherRunning != isRunning:
            self.__isLaserWatcherRunning = isRunning
            self.laserWatcherRunningChanged.emit()

    def isLaserConnectionUp(self):
        return self.__isLaserConnectionUp

    def setLaserConnectionUp(self, connectionUp: bool):
        if self.__isLaserConnectionUp != connectionUp:
            self.__isLaserConnectionUp = connectionUp
            self.laserConnectionUpChanged.emit()

    def isCameraWatcherRunning(self):
        return self.__isCameraWatcherRunning

    def setCameraWatcherRunning(self, isRunning: bool):
        if self.__isCameraWatcherRunning != isRunning:
            self.__isCameraWatcherRunning = isRunning
            self.cameraWatcherRunningChanged.emit()

    def isCameraConnectionUp(self):
        return self.__isCameraConnectionUp

    def setCameraConnectionUp(self, connectionUp: bool):
        if self.__isCameraConnectionUp != connectionUp:
            self.__isCameraConnectionUp = connectionUp
            self.cameraConnectionUpChanged.emit()

    def isErrorFileFounded(self):
        return self.__errorFileFounded

    def setErrorFileFounded(self, founded: bool):
        if self.__errorFileFounded != founded:
            self.__errorFileFounded = founded
            self.errorFileFoundedChanged.emit()

    def isCsvRegenerationThreadRunning(self):
        return self.__csvRegenerationThreadRunning

    def setCsvRegenerationThreadRunning(self, status: bool):
        if self.__csvRegenerationThreadRunning != status:
            self.__csvRegenerationThreadRunning = status
            self.csvRegenerationThreadRunningChanged.emit()

    def getCsvRegenerationDownloadStepStatus(self):
        return self.__csvRegenerationDownloadStepStatus

    def setCsvRegenerationDownloadStepStatus(self, status: int):
        if self.__csvRegenerationDownloadStepStatus != status:
            self.__csvRegenerationDownloadStepStatus = status
            self.csvRegenerationDownloadStepStatusChanged.emit()

    def getCsvRegenerationCreationStepStatus(self):
        return self.__csvRegenerationCreationStepStatus

    def setCsvRegenerationCreationStepStatus(self, status: int):
        if self.__csvRegenerationCreationStepStatus != status:
            self.__csvRegenerationCreationStepStatus = status
            self.csvRegenerationCreationStepStatusChanged.emit()

    def getCsvRegenerationSendingLaserStatus(self):
        return self.__csvRegenerationSendingLaserStatus

    def setCsvRegenerationSendingLaserStatus(self, status: int):
        if self.__csvRegenerationSendingLaserStatus != status:
            self.__csvRegenerationSendingLaserStatus = status
            self.csvRegenerationSendingLaserStatusChanged.emit()

    def getCsvRegenerationSendingCameraStatus(self):
        return self.__csvRegenerationSendingCameraStatus

    def setCsvRegenerationSendingCameraStatus(self, status: int):
        if self.__csvRegenerationSendingCameraStatus != status:
            self.__csvRegenerationSendingCameraStatus = status
            self.csvRegenerationSendingCameraStatusChanged.emit()

    def getCsvRegenerationExitCode(self):
        return self.__csvRegenerationExitCode

    def setCsvRegenerationExitCode(self, exitCode: int):
        if self.__csvRegenerationExitCode != exitCode:
            self.__csvRegenerationExitCode = exitCode
            self.csvRegenerationExitCodeChanged.emit()


    pLaserFolderItems = Property("QStringList", getLaserFolderItems, setLaserFolderItems,
                                 notify=laserFolderItemsChanged)
    pCameraFolderItems = Property("QStringList", getCameraFolderItems, setCameraFolderItems,
                                  notify=cameraFolderItemsChanged)
    pLaserWatcherRunning = Property(bool, isLaserWatcherRunning, setLaserWatcherRunning,
                                    notify=laserWatcherRunningChanged)
    pLaserConnectionUp = Property(bool, isLaserConnectionUp, setLaserConnectionUp, notify=laserConnectionUpChanged)
    pCameraWatcherRunning = Property(bool, isCameraWatcherRunning, setCameraWatcherRunning,
                                     notify=cameraWatcherRunningChanged)
    pCameraConnectionUp = Property(bool, isCameraConnectionUp, setCameraConnectionUp, notify=cameraConnectionUpChanged)
    pErrorFileFounded = Property(bool, isErrorFileFounded, setErrorFileFounded, notify=errorFileFoundedChanged)

    pCsvRegenerationThreadRunning = Property(bool, isCsvRegenerationThreadRunning,
                                             setCsvRegenerationThreadRunning,
                                             notify=csvRegenerationThreadRunningChanged)
    pCsvRegenerationDownloadStepStatus = Property(int, getCsvRegenerationDownloadStepStatus,
                                                  setCsvRegenerationDownloadStepStatus,
                                                  notify=csvRegenerationDownloadStepStatusChanged)
    pCsvRegenerationCreationStepStatus = Property(int, getCsvRegenerationCreationStepStatus,
                                                  setCsvRegenerationCreationStepStatus,
                                                  notify=csvRegenerationCreationStepStatusChanged)
    pCsvRegenerationSendingLaserStatus = Property(int, getCsvRegenerationSendingLaserStatus,
                                                  setCsvRegenerationSendingLaserStatus,
                                                  notify=csvRegenerationSendingLaserStatusChanged)
    pCsvRegenerationSendingCameraStatus = Property(int, getCsvRegenerationSendingCameraStatus,
                                                   setCsvRegenerationSendingCameraStatus,
                                                   notify=csvRegenerationSendingCameraStatusChanged)
    pCsvRegenerationExitCode = Property(int, getCsvRegenerationExitCode,
                                        setCsvRegenerationExitCode,
                                        notify=csvRegenerationExitCodeChanged)
