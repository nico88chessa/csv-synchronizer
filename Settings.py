from typing import Type

from Singleton import Singleton
from PySide2.QtCore import QStandardPaths

import os
import configparser


class Settings(metaclass=Singleton):

    _fileFolder = "CSVDaemon"
    _filename = "config.ini"

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
                "remotePath": QStandardPaths.writableLocation(QStandardPaths.HomeLocation),
                "pollingTimeMs": 1000,
            }
            config["SW"] = {
                "rowMargin": 10,
                "csvFilename": "lista.csv",
                "laserErrorFilename": "error.txt",
                "loadingPath": QStandardPaths.writableLocation(QStandardPaths.HomeLocation),
                "downloadingPath": QStandardPaths.writableLocation(QStandardPaths.HomeLocation),
            }

            with open(filePath, 'w') as fp:
                config.write(fp)

        config = configparser.ConfigParser()
        config.read(filePath)

        self.__laserIp = config["Laser"]["ip"]
        self.__laserPort = int(config["Laser"]["port"])
        self.__laserPollingTimeMs = int(config["Laser"]["pollingTimeMs"])
        self.__laserRemotePath = config["Laser"]["remotePath"]

        self.__cameraRemotePath = config["Camera"]["remotePath"]
        self.__cameraPollingTimeMs = int(config["Camera"]["pollingTimeMs"])

        self.__localRowMargin = int(config["SW"]["rowMargin"])
        self.__localCsvFilename = config["SW"]["csvFilename"]
        self.__localLaserErrorFilename = config["SW"]["laserErrorFilename"]
        self.__localLoadingPath = config["SW"]["loadingPath"]
        self.__localDownloadingPath = config["SW"]["downloadingPath"]

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

    def getCameraPollingTimeMs(self) -> int:
        return self.__cameraPollingTimeMs

    def setCameraPollingTimeMs(self, timeMs: int):
        self.__cameraPollingTimeMs = timeMs

    def getCameraRemotePath(self):
        return self.__cameraRemotePath

    def setCameraRemotePath(self, path: str):
        self.__cameraRemotePath = path

    def getLocalRowMargin(self) -> int:
        return self.__localRowMargin

    def setLocalRowMargin(self, margin: int):
        self.__localRowMargin = margin

    def getLocalCsvFilename(self):
        return self.__localCsvFilename

    def setLocalCsvFilename(self, csvFilename: str):
        self.__localCsvFilename = csvFilename

    def getLocalLaserErrorFilename(self):
        return self.__localLaserErrorFilename

    def setLocalLaserErrorFilename(self, errorFilename: str):
        self.__localLaserErrorFilename = errorFilename

    def getLocalLoadingPath(self):
        return self.__localLoadingPath

    def setLocalLoadingPath(self, loadingPath: str):
        self.__localLoadingPath = loadingPath

    def getLocalDownloadingPath(self):
        return self.__localDownloadingPath

    def setLocalDownloadingPath(self, downloadingPath: str):
        self.__localDownloadingPath = downloadingPath

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
            "pollingTimeMs": self.getCameraPollingTimeMs(),
            "remotePath": self.getCameraRemotePath(),
        }
        config["SW"] = {
            "rowMargin": self.getLocalRowMargin(),
            "csvFilename": self.getLocalCsvFilename(),
            "laserErrorFilename": self.getLocalLaserErrorFilename(),
            "loadingPath": self.getLocalLoadingPath(),
            "downloadingPath": self.getLocalDownloadingPath()
        }

        with open(filePath, 'w') as fp:
            config.write(fp)
