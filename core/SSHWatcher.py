import sys

from PySide2.QtCore import QTimer, Slot, QObject, Signal
import paramiko


class SSHWatcher(QObject):

    isConnectedSignal = Signal(bool)
    stoppedSignal = Signal()
    startedSignal = Signal()
    itemsPathUpdatedSignal = Signal(list)

    def __init__(self, userName, password, parent=None, remotePath="", sshAddress="", intervalMs=1000):
        super().__init__(parent)
        self.__remotePath = remotePath
        self.__sshAddress = sshAddress
        self.__timer = QTimer(self)
        self.__timeoutMs = intervalMs
        self.__timer.setInterval(self.timeoutMs)
        self.__userName = userName
        self.__pwd = password

        self.__sshClient = paramiko.SSHClient()
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.__timer.timeout.connect(self.process)

    @Slot()
    def startProcess(self):
        try:
            # self.ftpController.connect(host="192.168.1.1")
            self.__sshClient = self.client.connect(self.__sshAddress, username=self.__userName, password=self.__pwd)
            # self.nlst()
            self.timer.start()
            self.startedSignal.emit()
            self.isConnectedSignal.emit(True)
        except:
            self.restartProcess()

    @Slot()
    def stopProcess(self):
        self.timer.stop()
        self.__sshClient.close()
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
            stdin, stdout, stderr = self.__sshClient.exec_command('ls')
            self.itemsPathUpdatedSignal.emit(stdout)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            self.isConnectedSignal.emit(False)
            self.restartProcess()

        print(res)
