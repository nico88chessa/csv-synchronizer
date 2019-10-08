from typing import Type

from PySide2.QtCore import QObject, Property, Signal
from PySide2.QtQml import qmlRegisterType


class ProcessBean(QObject):

    @Signal
    def folderPathChanged(self): pass

    def __init__(self, parent=None):
        super().__init__(parent)
        self._folderPath = str

    def getFolderPath(self) -> str:
        return self._folderPath

    def setFolderPath(self, path: str):
        if (self._folderPath != path):
            self._folderPath = path
            self.folderPathChanged.emit()

    pFolderPath = Property(str, getFolderPath, setFolderPath, notify=folderPathChanged)
