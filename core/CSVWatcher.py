import time

from PySide2.QtCore import QThread, QTimer, Slot, QObject, Signal
from ftplib import FTP


class CSVWatcher(QObject):

    isConnectedSignal = Signal(bool)
    stoppedSignal = Signal()
    startedSignal = Signal()


    def __init__(self, parent = None, remotePath = "", ftpAddress = "", ftpPort = int(), intervalMs = int()):
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
            self.ftpController.connect()
            self.ftpController.login()
            # self.nlst()
            self.timer.start()
            self.startedSignal.emit()
            self.isConnectedSignal.emit(True)
        except:
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
        except:
            print("An exception occurred")
            self.isConnectedSignal.emit(False)
            self.restartProcess()

        print(res)
