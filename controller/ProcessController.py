from PySide2.QtCore import QObject, Slot, Property, Signal, QDir, QUrl
from PySide2.QtQml import QQmlApplicationEngine

from bean.ProcessBean import ProcessBean
from Settings import Settings


class ProcessController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._processBean = ProcessBean()

        s = Settings()

        self._processBean.setFolderPath(s.getFolderPath())

    def getProcessBean(self):
        return self._processBean

    pProcessBean = Property(ProcessBean, getProcessBean, constant=True)

    @Slot(None)
    def saveParameters(self):
        s = Settings()

        s.setFolderPath(self._processBean.getFolderPath())

        s.saveCurrentParameters()

    @Slot(str)
    def handleUrlPath(self, path: str):
        url = QUrl(path)
        pathOk: str
        if url.isLocalFile():
            pathOk = QDir.toNativeSeparators(url.toLocalFile())
        else:
            pathOk = path
        self._processBean.setFolderPath(pathOk)

    @Slot(str, result=str)
    def getUrlFromNativePath(self, path: str):
        path = QDir.fromNativeSeparators(path)
        url = QUrl.fromLocalFile(path)
        res = str(url.toString())
        return res


