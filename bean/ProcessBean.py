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
    stopRegThreadChanged = Signal()

    csvRegThreadRunningChanged = Signal()
    csvRegThreadExitCodeChanged = Signal()
    csvRegThreadCleanLocalFolderStatusChanged = Signal()
    csvRegThreadCleanCameraFolderStatusChanged = Signal()
    csvRegThreadRenameLaserItemsStatusChanged = Signal()
    csvRegThreadDownloadItemsStatusChanged = Signal()
    csvRegThreadCleanLaserFolderStatusChanged = Signal()
    csvRegThreadCsvCreationProcessStatusChanged = Signal()
    csvRegThreadSendCsvToLaserStatusChanged = Signal()
    csvRegThreadSendCsvToCameraStatusChanged = Signal()
    csvRegThreadCsvNewEmptyChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__laserFolderItems: List[str] = list()
        self.__cameraFolderItems: List[str] = list()
        self.__isLaserWatcherRunning = False
        self.__isCameraWatcherRunning = False
        self.__isLaserConnectionUp = False
        self.__isCameraConnectionUp = False
        self.__errorFileFounded = False
        self.__stopRegThread = False

        self.__csvRegThreadRunning: bool = False
        self.__csvRegThreadExitCode: int = 0
        self.__csvRegThreadCleanLocalFolderStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadCleanCameraFolderStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadRenameLaserItemsStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadDownloadItemsStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadCleanLaserFolderStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadCsvCreationProcessStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadSendCsvToLaserStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadSendCsvToCameraStatus: int = CSVRegeneratorStepStatus.IDLE
        self.__csvRegThreadCsvNewEmpty: bool = False


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

    def isStopRegThread(self):
        return self.__stopRegThread

    def setStopRegThread(self, stop: bool):
        if self.__stopRegThread != stop:
            self.__stopRegThread = stop
            self.stopRegThreadChanged.emit()

    def getCsvRegThreadRunning(self):
        return self.__csvRegThreadRunning

    def setCsvRegThreadRunning(self, status: bool):
        if self.__csvRegThreadRunning != status:
            self.__csvRegThreadRunning = status
            self.csvRegThreadRunningChanged.emit()

    def getCsvRegThreadExitCode(self):
        return self.__csvRegThreadExitCode

    def setCsvRegThreadExitCode(self, status: int):
        if self.__csvRegThreadExitCode != status:
            self.__csvRegThreadExitCode = status
            self.csvRegThreadExitCodeChanged.emit()

    def getCsvRegThreadCleanLocalFolderStatus(self):
        return self.__csvRegThreadCleanLocalFolderStatus

    def setCsvRegThreadCleanLocalFolderStatus(self, status: int):
        if self.__csvRegThreadCleanLocalFolderStatus != status:
            self.__csvRegThreadCleanLocalFolderStatus = status
            self.csvRegThreadCleanLocalFolderStatusChanged.emit()

    def getCsvRegThreadCleanCameraFolderStatus(self):
        return self.__csvRegThreadCleanCameraFolderStatus

    def setCsvRegThreadCleanCameraFolderStatus(self, status: int):
        if self.__csvRegThreadCleanCameraFolderStatus != status:
            self.__csvRegThreadCleanCameraFolderStatus = status
            self.csvRegThreadCleanCameraFolderStatusChanged.emit()

    def getCsvRegThreadRenameLaserItemsStatus(self):
        return self.__csvRegThreadRenameLaserItemsStatus

    def setCsvRegThreadRenameLaserItemsStatus(self, status: int):
        if self.__csvRegThreadRenameLaserItemsStatus != status:
            self.__csvRegThreadRenameLaserItemsStatus = status
            self.csvRegThreadRenameLaserItemsStatusChanged.emit()

    def getCsvRegThreadDownloadItemsStatus(self):
        return self.__csvRegThreadDownloadItemsStatus

    def setCsvRegThreadDownloadItemsStatus(self, status: int):
        if self.__csvRegThreadDownloadItemsStatus != status:
            self.__csvRegThreadDownloadItemsStatus = status
            self.csvRegThreadDownloadItemsStatusChanged.emit()

    def getCsvRegThreadCleanLaserFolderStatus(self):
        return self.__csvRegThreadCleanLaserFolderStatus

    def setCsvRegThreadCleanLaserFolderStatus(self, status: int):
        if self.__csvRegThreadCleanLaserFolderStatus != status:
            self.__csvRegThreadCleanLaserFolderStatus = status
            self.csvRegThreadCleanLaserFolderStatusChanged.emit()

    def getCsvRegThreadCsvCreationProcessStatus(self):
        return self.__csvRegThreadCsvCreationProcessStatus

    def setCsvRegThreadCsvCreationProcessStatus(self, status: int):
        if self.__csvRegThreadCsvCreationProcessStatus != status:
            self.__csvRegThreadCsvCreationProcessStatus = status
            self.csvRegThreadCsvCreationProcessStatusChanged.emit()

    def getCsvRegThreadSendCsvToLaserStatus(self):
        return self.__csvRegThreadSendCsvToLaserStatus

    def setCsvRegThreadSendCsvToLaserStatus(self, status: int):
        if self.__csvRegThreadSendCsvToLaserStatus != status:
            self.__csvRegThreadSendCsvToLaserStatus = status
            self.csvRegThreadSendCsvToLaserStatusChanged.emit()

    def getCsvRegThreadSendCsvToCameraStatus(self):
        return self.__csvRegThreadSendCsvToCameraStatus

    def setCsvRegThreadSendCsvToCameraStatus(self, status: int):
        if self.__csvRegThreadSendCsvToCameraStatus != status:
            self.__csvRegThreadSendCsvToCameraStatus = status
            self.csvRegThreadSendCsvToCameraStatusChanged.emit()

    def isCsvRegThreadCsvNewEmpty(self):
        return self.__csvRegThreadCsvNewEmpty

    def setCsvRegThreadCsvNewEmpty(self, isEmpty: bool):
        if self.__csvRegThreadCsvNewEmpty != isEmpty:
            self.__csvRegThreadCsvNewEmpty = isEmpty
            self.csvRegThreadCsvNewEmptyChanged.emit()


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
    pStopRegThread = Property(bool, isStopRegThread, setStopRegThread, notify=stopRegThreadChanged)

    pCsvRegThreadRunning = Property(bool, getCsvRegThreadRunning, setCsvRegThreadRunning,
                                    notify=csvRegThreadRunningChanged)
    pCsvRegThreadExitCode = Property(int, getCsvRegThreadExitCode, setCsvRegThreadExitCode,
                                     notify=csvRegThreadExitCodeChanged)
    pCsvRegThreadCleanLocalFolderStatus = Property(int,
                                        getCsvRegThreadCleanLocalFolderStatus,
                                        setCsvRegThreadCleanLocalFolderStatus,
                                        notify=csvRegThreadCleanLocalFolderStatusChanged)
    pCsvRegThreadCleanCameraFolderStatus = Property(int,
                                                   getCsvRegThreadCleanCameraFolderStatus,
                                                   setCsvRegThreadCleanCameraFolderStatus,
                                                   notify=csvRegThreadCleanCameraFolderStatusChanged)
    pCsvRegThreadRenameLaserItemsStatus = Property(int,
                                             getCsvRegThreadRenameLaserItemsStatus,
                                             setCsvRegThreadRenameLaserItemsStatus,
                                             notify=csvRegThreadRenameLaserItemsStatusChanged)
    pCsvRegThreadDownloadItemsStatus = Property(int,
                                          getCsvRegThreadDownloadItemsStatus,
                                          setCsvRegThreadDownloadItemsStatus,
                                          notify=csvRegThreadDownloadItemsStatusChanged)
    pCsvRegThreadCleanLaserFolderStatus = Property(int,
                                             getCsvRegThreadCleanLaserFolderStatus,
                                             setCsvRegThreadCleanLaserFolderStatus,
                                             notify=csvRegThreadCleanLaserFolderStatusChanged)
    pCsvRegThreadCsvCreationProcessStatus = Property(int,
                                               getCsvRegThreadCsvCreationProcessStatus,
                                               setCsvRegThreadCsvCreationProcessStatus,
                                               notify=csvRegThreadCsvCreationProcessStatusChanged)
    pCsvRegThreadSendCsvToLaserStatus = Property(int,
                                           getCsvRegThreadSendCsvToLaserStatus,
                                           setCsvRegThreadSendCsvToLaserStatus,
                                           notify=csvRegThreadSendCsvToLaserStatusChanged)
    pCsvRegThreadSendCsvToCameraStatus = Property(int,
                                            getCsvRegThreadSendCsvToCameraStatus,
                                            setCsvRegThreadSendCsvToCameraStatus,
                                            notify=csvRegThreadSendCsvToCameraStatusChanged)
    pCsvRegThreadCsvNewEmpty = Property(bool,
                                        isCsvRegThreadCsvNewEmpty,
                                        setCsvRegThreadCsvNewEmpty,
                                        notify=csvRegThreadCsvNewEmptyChanged)
