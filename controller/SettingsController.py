from PySide2.QtCore import QObject, Slot, Property, Signal, QThread
from PySide2.QtWidgets import QApplication

from bean.SettingsBean import SettingsBean
from Settings import Settings
from core.FTPWatcher import FTPWatcher
from core.Logger import Logger


class SettingsController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__settingsBean: SettingsBean = None

    @Signal
    def settingsBeanChanged(self): pass

    def getSettingsBean(self):
        return self.__settingsBean

    def setSettingsBean(self, bean: SettingsBean):
        self.__settingsBean = bean
        self.settingsBeanChanged.emit()

    pSettingsBean = Property(SettingsBean, getSettingsBean, setSettingsBean, notify=settingsBeanChanged)

    @Slot()
    def initBean(self):
        s = Settings()

        self.__settingsBean.setLaserIp(s.getLaserIp())
        self.__settingsBean.setLaserPort(s.getLaserPort())
        self.__settingsBean.setLaserPollingTimeMs(s.getLaserPollingTime())
        self.__settingsBean.setLaserRemotePath(s.getLaserRemotePath())

        self.__settingsBean.setCameraPollingTimeMs(s.getCameraPollingTimeMs())
        self.__settingsBean.setCameraRemotePath(s.getCameraRemotePath())
        self.__settingsBean.setCameraSendCSV(s.getCameraSendCSV())

        self.__settingsBean.setLocalRowMargin(s.getLocalRowMargin())
        self.__settingsBean.setLocalCsvFilename(s.getLocalCsvFilename())
        self.__settingsBean.setLocalLaserErrorFilename(s.getLocalLaserErrorFilename())
        self.__settingsBean.setLocalLaserLogFilename(s.getLocalLaserLogFilename())
        self.__settingsBean.setLocalWaitTimeBeforeProcess(s.getLocalWaitTimeBeforeProcess())
        self.__settingsBean.setLocalLoadingPath(s.getLocalLoadingPath())
        self.__settingsBean.setLocalDownloadingPath(s.getLocalDownloadingPath())

        self.__settingsBean.setVersion(QApplication.instance().applicationVersion())

        Logger().info("Laser Ip: " + self.__settingsBean.getLaserIp())
        Logger().info("Laser Port: " + str(self.__settingsBean.getLaserPort()))
        Logger().info("Laser Polling Time [ms]: " + str(self.__settingsBean.getLaserPollingTimeMs()))
        Logger().info("Laser Remote Path: " + self.__settingsBean.getLaserRemotePath())
        Logger().info("Camera Polling Time [ms]: " + str(self.__settingsBean.getCameraPollingTimeMs()))
        Logger().info("Camera Remote Path: " + self.__settingsBean.getCameraRemotePath())
        Logger().info("Camera Send CSV: " + str(self.__settingsBean.getCameraSendCSV()))
        Logger().info("Local Row Margin: " + str(self.__settingsBean.getLocalRowMargin()))
        Logger().info("Local Csv Filename: " + self.__settingsBean.getLocalCsvFilename())
        Logger().info("Local Laser Error Filename: " + self.__settingsBean.getLocalLaserErrorFilename())
        Logger().info("Local Laser Log Filename: " + self.__settingsBean.getLocalLaserLogFilename())
        Logger().info("Local Wait Time before process [s]: " + str(self.__settingsBean.getLocalWaitTimeBeforeProcess()))
        Logger().info("Local Loading Path: " + self.__settingsBean.getLocalLoadingPath())
        Logger().info("Local Downloading Path: " + self.__settingsBean.getLocalDownloadingPath())


    @Slot(None)
    def saveParameters(self):

        Logger().info("Salvataggio parametri")

        s = Settings()

        s.setLaserIp(self.__settingsBean.getLaserIp())
        s.setLaserPort(self.__settingsBean.getLaserPort())
        s.setLaserPollingTime(self.__settingsBean.getLaserPollingTimeMs())
        s.setLaserRemotePath(self.__settingsBean.getLaserRemotePath())

        s.setCameraPollingTimeMs(self.__settingsBean.getCameraPollingTimeMs())
        s.setCameraRemotePath(self.__settingsBean.getCameraRemotePath())
        s.setCameraSendCSV(self.__settingsBean.getCameraSendCSV())

        s.setLocalRowMargin(self.__settingsBean.getLocalRowMargin())
        s.setLocalCsvFilename(self.__settingsBean.getLocalCsvFilename())
        s.setLocalLaserErrorFilename(self.__settingsBean.getLocalLaserErrorFilename())
        s.setLocalLaserLogFilename(self.__settingsBean.getLocalLaserLogFilename())
        s.setLocalWaitTimeBeforeProcess(self.__settingsBean.getLocalWaitTimeBeforeProcess())
        s.setLocalLoadingPath(self.__settingsBean.getLocalLoadingPath())
        s.setLocalDownloadingPath(self.__settingsBean.getLocalDownloadingPath())

        Logger().info("Laser Ip: " + self.__settingsBean.getLaserIp())
        Logger().info("Laser Port: " + str(self.__settingsBean.getLaserPort()))
        Logger().info("Laser Polling Time [ms]: " + str(self.__settingsBean.getLaserPollingTimeMs()))
        Logger().info("Laser Remote Path: " + self.__settingsBean.getLaserRemotePath())
        Logger().info("Camera Polling Time [ms]: " + str(self.__settingsBean.getCameraPollingTimeMs()))
        Logger().info("Camera Remote Path: " + self.__settingsBean.getCameraRemotePath())
        Logger().info("Camera Send CSV: " + str(self.__settingsBean.getCameraSendCSV()))
        Logger().info("Local Row Margin: " + str(self.__settingsBean.getLocalRowMargin()))
        Logger().info("Local Csv Filename: " + self.__settingsBean.getLocalCsvFilename())
        Logger().info("Local Laser Error Filename: " + self.__settingsBean.getLocalLaserErrorFilename())
        Logger().info("Local Laser Log Filename: " + self.__settingsBean.getLocalLaserLogFilename())
        Logger().info("Local Wait time before process [s]: " + str(self.__settingsBean.getLocalWaitTimeBeforeProcess()))
        Logger().info("Local Loading Path: " + self.__settingsBean.getLocalLoadingPath())
        Logger().info("Local Downloading Path: " + self.__settingsBean.getLocalDownloadingPath())

        s.saveCurrentParameters()
