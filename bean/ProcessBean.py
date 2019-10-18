from typing import List

from PySide2.QtCore import QObject, Property, Signal, QStringListModel, QMetaMethod


class ProcessBean(QObject):

    __isCameraWatcherRunning: bool
    __isLaserWatcherRunning: bool

    laserFolderItemsChanged = Signal()
    cameraFolderItemsChanged = Signal()
    laserWatcherRunningChanged = Signal()
    cameraWatcherRunningChanged = Signal()
    laserConnectionUpChanged = Signal()
    cameraConnectionUpChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__laserFolderItems: List[str] = list()
        self.__cameraFolderItems: List[str] = list()
        self.__isLaserWatcherRunning = False
        self.__isCameraWatcherRunning = False
        self.__isLaserConnectionUp = False
        self.__isCameraConnectionUp = False

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
