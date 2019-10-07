from typing import Type

from Singleton import Singleton
from PySide2.QtCore import QStandardPaths

import os
import configparser


class Settings(metaclass=Singleton):

    _fileFolder = "CSVDaemon"
    _filename = "config.ini"

    _laserIp: str
    _laserPort: int
    _cameraIp: str
    _cameraPort: int

    def __init__(self):
        folder = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        folder += "/" + Settings._fileFolder
        if not os.path.exists(folder):
            os.makedirs(folder)

        filePath = folder + "/" + Settings._filename
        if not os.path.exists(filePath):
            config = configparser.ConfigParser()
            config["Laser"] = {
                "ip": "192.168.100.20",
                "port": 21
            }
            config["Camera"] = {
                "ip": "192.168.100.21",
                "port": 21
            }

            with open(filePath, 'w') as fp:
                config.write(fp)

        config = configparser.ConfigParser()
        config.read(filePath)

        self._laserIp = config["Laser"]["ip"]
        self._laserPort = int(config["Laser"]["port"])
        self._cameraIp = config["Camera"]["ip"]
        self._cameraPort = int(config["Camera"]["port"])

    def getLaserIp(self):
        return self._laserIp

    def setLaserIp(self, ip):
        self._laserIp = ip

    def getLaserPort(self) -> int:
        return self._laserPort

    def setLaserPort(self, port: int):
        self._laserPort = port

    def getCameraIp(self):
        return self._cameraIp

    def setCameraIp(self, ip):
        self._cameraIp = ip

    def getCameraPort(self) -> int:
        return self._cameraPort

    def setCameraPort(self, port: int):
        self._cameraPort = port

    def saveCurrentParameters(self):
        folder = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        folder += "/" + Settings._fileFolder
        if not os.path.exists(folder):
            os.makedirs(folder)

        filePath = folder + "/" + Settings._filename

        config = configparser.ConfigParser()
        config["Laser"] = {
            "ip": self.getLaserIp(),
            "port": self.getLaserPort()
        }
        config["Camera"] = {
            "ip": self.getCameraIp(),
            "port": self.getCameraPort()
        }

        with open(filePath, 'w') as fp:
            config.write(fp)

