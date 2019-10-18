import os
import sys

from PySide2.QtCore import QObject, Signal, QTimer, Slot


class FSWatcher(QObject):

    itemsPathUpdatedSignal = Signal(list)
    isConnectedSignal = Signal(bool)
    startedSignal = Signal()
    stoppedSignal = Signal()
    pathUnreachableSignal = Signal()

    def __init__(self, path: str, intervalMs: int, parent=None):
        super().__init__(parent)
        self.__path = path
        self.timer = QTimer(self)
        self.timeoutMs = intervalMs
        self.timer.setInterval(self.timeoutMs)
        self.__isConnected = False
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.timer.timeout.connect(self.process)

    @Slot()
    def startProcess(self):
        try:
            self.timer.start()
            self.startedSignal.emit()
        except:
            self.setConnected(False)
            self.restartProcess()

    @Slot()
    def stopProcess(self):
        self.timer.stop()
        self.stoppedSignal.emit()
        self.setConnected(False)

    @Slot()
    def restartProcess(self):
        if self.timer.isActive():
            self.timer.stop()
        QTimer().singleShot(1000, self.startProcess)

    @Slot()
    def process(self):
        res = None
        try:
            res = os.listdir(self.__path)
            self.setConnected(True)
            self.itemsPathUpdatedSignal.emit(res)
        except OSError as err:
            print("FSWatcher error:", err)
            self.pathUnreachableSignal.emit()
            self.setConnected(False)
            self.restartProcess()

        # print(res)

    def isConnected(self):
        return self.__isConnected

    def setConnected(self, isConnected: bool):
        if self.__isConnected != isConnected:
            self.__isConnected = isConnected
            self.isConnectedSignal.emit(self.__isConnected)