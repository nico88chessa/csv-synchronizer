from PySide2.QtCore import QObject, Property, Signal, QStringListModel, QMetaMethod
from pip._internal.utils import typing
from pyside2uic.properties import QtCore


class ProcessBean(QObject):

    @Signal
    def localFolderPathChanged(self): pass

    @Signal
    def laserFolderItemsChanged(self): pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__localFolderPath = str
        self.__laserFolderItems = list()
        self.laserFolderItemsChanged.emit()

    def getLocalFolderPath(self):
        return self.__localFolderPath

    def setLocalFolderPath(self, path: str):
        if (self.__localFolderPath != path):
            self.__localFolderPath = path
            self.localFolderPathChanged.emit()

    def getLaserFolderItems(self):
        return self.__laserFolderItems

    def setLaserFolderItems(self, items: list):
        isModified = False
        for i in items:
            if i not in self.__laserFolderItems:
                isModified = True
                break
        if isModified:
            self.__laserFolderItems = items
            self.laserFolderItemsChanged.emit()

    pLocalFolderPath = Property(str, getLocalFolderPath, setLocalFolderPath, notify=localFolderPathChanged)
    pLaserFolderItems = Property("QStringList", getLaserFolderItems, setLaserFolderItems, notify=laserFolderItemsChanged)
