from typing import Type

from PySide2.QtCore import QObject, Property, Signal
from PySide2.QtQml import qmlRegisterType


class ProcessBean(QObject):

    @Signal
    def localFolderPathChanged(self): pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__localFolderPath = str

    def getLocalFolderPath(self) -> str:
        return self.__localFolderPath

    def setLocalFolderPath(self, path: str):
        if (self.__localFolderPath != path):
            self.__localFolderPath = path
            self.localFolderPathChanged.emit()

    pLocalFolderPath = Property(str, getLocalFolderPath, setLocalFolderPath, notify=localFolderPathChanged)
