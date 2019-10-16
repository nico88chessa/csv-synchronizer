from typing import Type

from Singleton import Singleton
from PySide2.QtCore import QStandardPaths

import os
import configparser


class Settings(metaclass=Singleton):

    _fileFolder = "CSVDaemon"
    _filename = "config.ini"

    # _laserIp: str
    # _laserPort: int
    # _cameraIp: str
    # _cameraPort: int

    def __init__(self):
        folder = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        # folder += "/" + Settings._fileFolder
        if not os.path.exists(folder):
            os.makedirs(folder)

        filePath = folder + "/" + Settings._filename
        if not os.path.exists(filePath):
            config = configparser.ConfigParser()
            config["Laser"] = {
                "ip": "192.168.100.20",
                "port": 21,
                "pollingTimeMs": 1000,
                "remotePath": ".",
            }
            config["Camera"] = {
                "ip": "192.168.100.21",
                "port": 21,
                "pollingTimeMs": 1000,
                "remotePath": ".",
            }
            config["SW"] = {
                "localFolderPath": QStandardPaths.writableLocation(QStandardPaths.HomeLocation),
            }

            with open(filePath, 'w') as fp:
                config.write(fp)

        config = configparser.ConfigParser()
        config.read(filePath)

        self.__laserIp = config["Laser"]["ip"]
        self.__laserPort = int(config["Laser"]["port"])
        self.__laserPollingTimeMs = int(config["Laser"]["pollingTimeMs"])
        self.__laserRemotePath = config["Laser"]["remotePath"]
        self.__cameraIp = config["Camera"]["ip"]
        self.__cameraPort = int(config["Camera"]["port"])
        self.__cameraPollingTimeMs = int(config["Camera"]["pollingTimeMs"])
        self.__cameraRemotePath = config["Camera"]["remotePath"]
        self.__localFolderPath = config["SW"]["localFolderPath"]

    def getLaserIp(self):
        return self.__laserIp

    def setLaserIp(self, ip):
        self.__laserIp = ip

    def getLaserPort(self) -> int:
        return self.__laserPort

    def setLaserPort(self, port: int):
        self.__laserPort = port

    def getLaserPollingTime(self) -> int:
        return self.__laserPollingTimeMs

    def setLaserPollingTime(self, timeMs: int):
        self.__laserPollingTimeMs = timeMs

    def getLaserRemotePath(self):
        return self.__laserRemotePath

    def setLaserRemotePath(self, path: str):
        self.__laserRemotePath = path

    def getCameraIp(self):
        return self.__cameraIp

    def setCameraIp(self, ip):
        self.__cameraIp = ip

    def getCameraPort(self) -> int:
        return self.__cameraPort

    def setCameraPort(self, port: int):
        self.__cameraPort = port

    def getCameraPollingTimeMs(self) -> int:
        return self.__cameraPollingTimeMs

    def setCameraPollingTimeMs(self, timeMs: int):
        self.__cameraPollingTimeMs = timeMs

    def getCameraRemotePath(self):
        return self.__cameraRemotePath

    def setCameraRemotePath(self, path: str):
        self.__cameraRemotePath = path

    def getLocalFolderPath(self):
        return self.__localFolderPath

    def setLocalFolderPath(self, path: str):
        self.__localFolderPath = path

    def saveCurrentParameters(self):
        folder = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        # folder += "/" + Settings._fileFolder
        if not os.path.exists(folder):
            os.makedirs(folder)

        filePath = folder + "/" + Settings._filename

        config = configparser.ConfigParser()
        config["Laser"] = {
            "ip": self.getLaserIp(),
            "port": self.getLaserPort(),
            "pollingTimeMs": self.getLaserPollingTime(),
            "remotePath": self.getLaserRemotePath(),
        }
        config["Camera"] = {
            "ip": self.getCameraIp(),
            "port": self.getCameraPort(),
            "pollingTimeMs": self.getCameraPollingTimeMs(),
            "remotePath": self.getCameraRemotePath(),
        }
        config["SW"] = {
            "localFolderPath": self.getLocalFolderPath(),
        }

        with open(filePath, 'w') as fp:
            config.write(fp)
