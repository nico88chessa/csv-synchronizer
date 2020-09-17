import os
import sys

from PySide2.QtCore import QFile
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType

from bean.ProcessBean import ProcessBean
from bean.SettingsBean import SettingsBean
from controller.SettingsController import SettingsController
from controller.ProcessController import ProcessController
from core.Logger import Logger
import resources

if __name__ == "__main__":

    # Set up the application window
    app = QGuiApplication(sys.argv)

    version = "1.0.2"

    app.setOrganizationName("DV")
    app.setApplicationName("CSV-Synchronizer")
    app.setApplicationVersion(version)

    Logger().info("Start applicazione CSV-Synchronizer")
    Logger().info("Versione: " + version)

    # qmlFile = QFile(":/ui/main.qml")
    # qmlFile.open(QFile.ReadOnly | QFile.Text)
    # Load the QML file
    # qmlFile = os.path.join(os.path.dirname(__file__), "./ui/main.qml")

    qmlRegisterType(SettingsController, "SettingsController", 1, 0, "QMLSettingsController")
    qmlRegisterType(ProcessController, "ProcessController", 1, 0, "QMLProcessController")
    qmlRegisterType(ProcessBean, "ProcessBean", 1, 0, "QMLProcessBean")
    qmlRegisterType(SettingsBean, "SettingsBean", 1, 0, "QMLSettingsBean")

    engine = QQmlApplicationEngine()
    engine.load(":/ui/main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sc = SettingsController()

    res = app.exec_()
    sys.exit(res)
