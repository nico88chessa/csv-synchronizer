import ftplib
import time

from PySide2.QtCore import QTimer, Slot, QObject, Signal
from ftplib import FTP

from core.Logger import Logger


class FTPWatcher(QObject):

    isConnectedSignal = Signal(bool)
    stoppedSignal = Signal()
    startedSignal = Signal()
    itemsPathUpdatedSignal = Signal(list)

    def __init__(self, parent=None, remotePath="", ftpAddress="", ftpPort=0, intervalMs=1000):
        super().__init__(parent)
        self.remotePath = remotePath
        self.ftpAddress = ftpAddress
        self.ftpPort = ftpPort
        self.timer = QTimer(self)
        self.timeoutMs = intervalMs
        self.timer.setInterval(self.timeoutMs)

        self.ftpController = FTP()
        self.ftpController.host = self.ftpAddress
        self.ftpController.port = self.ftpPort
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.timer.timeout.connect(self.process)

    @Slot()
    def startProcess(self):
        try:
            # self.ftpController.connect(host="192.168.1.1")
            self.startedSignal.emit()
            self.ftpController.connect()
            self.ftpController.login()
            # self.nlst()
            self.timer.start()
            self.isConnectedSignal.emit(True)

        except ftplib.all_errors as ftpErr:
            Logger().error("FTPWatcher error:" + str(ftpErr))
            self.ftpController.close()
            self.restartProcess()

    @Slot()
    def stopProcess(self):
        self.timer.stop()
        self.ftpController.close()
        self.isConnectedSignal.emit(False)
        self.stoppedSignal.emit()

    @Slot()
    def restartProcess(self):
        if self.timer.isActive():
            self.timer.stop()
        QTimer().singleShot(1000, self.startProcess)

    @Slot()
    def process(self):
        res = None
        try:
            res = self.ftpController.nlst(self.remotePath)
            self.itemsPathUpdatedSignal.emit(res)
        except ftplib.all_errors as ftpErr:
            Logger().error("FTPWatcher error: " + str(ftpErr))
            self.isConnectedSignal.emit(False)
            self.ftpController.close()
            self.restartProcess()
