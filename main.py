import os
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType

from bean.ProcessBean import ProcessBean
from bean.SettingsBean import SettingsBean
from controller.SettingsController import SettingsController
from controller.ProcessController import ProcessController

if __name__ == "__main__":

    # Set up the application window
    app = QGuiApplication(sys.argv)

    app.setOrganizationName("DV")
    app.setApplicationName("CSV-Synchronizer")

    # Load the QML file
    qmlFile = os.path.join(os.path.dirname(__file__), "./ui/main.qml")

    qmlRegisterType(SettingsController, "SettingsController", 1, 0, "QMLSettingsController")
    qmlRegisterType(ProcessController, "ProcessController", 1, 0, "QMLProcessController")
    qmlRegisterType(ProcessBean, "ProcessBean", 1, 0, "QMLProcessBean")
    qmlRegisterType(SettingsBean, "SettingsBean", 1, 0, "QMLSettingsBean")

    engine = QQmlApplicationEngine()
    engine.load(qmlFile)

    if not engine.rootObjects():
        sys.exit(-1)

    sc = SettingsController()

    res = app.exec_()
    sys.exit(res)
