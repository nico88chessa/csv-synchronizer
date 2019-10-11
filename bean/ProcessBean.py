from PySide2.QtCore import QObject, Property, Signal, QStringListModel, QMetaMethod
from pip._internal.utils import typing
from pyside2uic.properties import QtCore


class ProcessBean(QObject):

    @Signal
    def localFolderPathChanged(self): pass

    @Signal
    def laserFolderItemsChanged(self): pass

    @Signal
    def laserFolderItemsModelChanged(self): pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__localFolderPath = str
        self.__laserFolderItems = ["AAA", "BBB", "CCC"]
        self.__laserFolderItemsModel = QStringListModel()
        self.__laserFolderItemsModel.setStringList(["AAA", "BBB", "CCC"])
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
        self.__laserFolderItems = items
        # self.setLaserFolderItemsModel(items)
        self.__laserFolderItemsModel.setStringList(items)
        self.laserFolderItemsChanged.emit()

    def getLaserFolderItemsModel(self):
        # return {"AAA", "BBB", "CCC" }
        return self.__laserFolderItemsModel.stringList()

    # def setLaserFolderItemsModel(self, l):
    #     self.__laserFolderItemsModel.setStringList(l)
    #     self.laserFolderItemsModelChanged.emit()

    pLocalFolderPath = Property(str, getLocalFolderPath, setLocalFolderPath, notify=localFolderPathChanged)
    pLaserFolderItems = Property(str, getLaserFolderItems, setLaserFolderItems, notify=laserFolderItemsChanged)
    pLaserFolderItemsModel = Property(list, getLaserFolderItemsModel, setLaserFolderItems, notify=laserFolderItemsChanged)
