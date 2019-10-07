import os
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType

from controller.SettingsController import SettingsController

if __name__ == "__main__":

    # Set up the application window
    app = QGuiApplication(sys.argv)

    # Load the QML file
    qmlFile = os.path.join(os.path.dirname(__file__), "./ui/main.qml")
    #view.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

    qmlRegisterType(SettingsController, "SettingsController", 1, 0, "QMLSettingsController")

    engine = QQmlApplicationEngine()
    engine.load(qmlFile)


    if not engine.rootObjects():
        sys.exit(-1)

    sc = SettingsController()

    res = app.exec_()
    sys.exit(res)
