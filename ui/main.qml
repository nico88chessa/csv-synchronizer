import QtQuick 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.3

//import "../controller/"
import SettingsController 1.0

/*Item {*/

ApplicationWindow {

    QMLSettingsController {
        id: settingsCtrl
    }

    width: 640
    height: 480
    minimumWidth: 640
    minimumHeight: 480
    visible: true

    GridLayout {
        id: glMain
        anchors.fill: parent
        rows: 2
        columns: 1

        TabBar {
            id: tabBar
            width: parent.width
            Layout.fillWidth: true
            currentIndex: 2
            TabButton {
                text: qsTr("Process")
            }
            TabButton {
                text: qsTr("Laser Settings")
            }
            TabButton {
                text: qsTr("Camera Settings")
            }

        }

        StackLayout {

            width: parent.width
            Layout.fillHeight: true
            currentIndex: tabBar.currentIndex
            id: stackLayout
            Layout.fillWidth: true

            Item {

                id: processItem

                GridLayout {
                    id: gMain
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 10
                    anchors.topMargin: 10
                    anchors.fill: parent
                    clip: true
                    rows: 2
                    columns: 1

                    GridLayout {
                        id: gBody
                        width: 100
                        height: 100
                        Layout.fillWidth: true
                        rows: 3
                        columns: 2

                        TextField {
                            id: textField1
                            text: qsTr("Text Field")
                            placeholderText: qsTr("")
                            Layout.fillWidth: true
                        }


                        Button {
                            id: button
                            width: 200
                            height: 40
                            text: qsTr("Button")
                            Layout.fillWidth: true
                        }

                        TextField {
                            id: textField
                            placeholderText: "Inserire la path"
                            height: 40
                            Layout.fillHeight: false
                            Layout.fillWidth: true
                        }

                        Item {
                            Layout.rowSpan: 1
                            Layout.preferredHeight: 2
                            Layout.preferredWidth: 4
                            Layout.fillWidth: true
                            Layout.fillHeight: false
                        }

                        Item {
                            Layout.columnSpan: 2
                            Layout.rowSpan: 1
                            Layout.fillHeight: true
                            Layout.fillWidth: true
                        }

                    }

                    GridLayout {
                        id: gFooter
                        width: 100
                        height: 100

                        Item {
                            Layout.fillWidth: true
                        }

                        Button {
                            id: bStart
                            text: qsTr("Button")
                        }

                        Button {
                            id: bStop
                            text: qsTr("Button")
                        }

                    }

                }
            }

            Item {
                id: laserSettings

                ColumnLayout {
                    id: columnLayout
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 10
                    anchors.topMargin: 10
                    anchors.fill: parent

                    GridLayout {
                        id: glLaser
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                        columns: 2
                        columnSpacing: 5

                        Text {
                            id: tLaserIp
                            text: qsTr("Laser IP")
                            Layout.minimumWidth: 120
                            Layout.fillWidth: false
                            font.pixelSize: 12
                        }

                        TextField {
                            id: tfLaserIp
                            text: settingsCtrl.pSettingsBean.pLaserIp
                            placeholderText: "Laser IP address"
                            inputMask: "000.000.000.000"
                            onEditingFinished: settingsCtrl.pSettingsBean.pLaserIp = text
                        }

                        Text {
                            id: tLaserPort
                            text: qsTr("Laser Port")
                            Layout.minimumWidth: 120
                            font.pixelSize: 12
                        }

                        TextField {
                            id: tfLaserPort
                            text: "%0".arg(settingsCtrl.pSettingsBean.pLaserPort)
                            placeholderText: "Laser Port"
                            inputMask: "00000"
                            onEditingFinished: settingsCtrl.pSettingsBean.pLaserPort = tfLaserPort.text
                        }

                        Item {
                            id: element3
                            width: 200
                            height: 200
                            Layout.columnSpan: 2
                            Layout.preferredHeight: 1
                            Layout.preferredWidth: 0
                            Layout.fillWidth: false
                            Layout.fillHeight: true
                        }

                    }

                    GridLayout {
                        id: gridLayout1
                        width: 100
                        height: 100

                        Item {
                            id: element2
                            width: 200
                            height: 200
                            Layout.fillWidth: true
                            Layout.preferredHeight: 0
                            Layout.preferredWidth: -1
                        }

                        Button {
                            id: bLaserSet
                            text: qsTr("Set Laser Configuration")
                            onClicked: settingsCtrl.saveParameters()
                        }

                    }

                }
            }

            Item {
                id: cameraSettings

                ColumnLayout {
                    id: columnLayout1
                    anchors.fill: parent
                    anchors.bottomMargin: 10
                    anchors.rightMargin: 10
                    anchors.topMargin: 10
                    anchors.leftMargin: 10
                    GridLayout {
                        id: gridLayout2
                        Layout.fillWidth: true
                        columns: 2
                        Layout.fillHeight: true
                        columnSpacing: 5
                        Text {
                            id: tCameraIp
                            text: qsTr("Camera IP")
                            Layout.fillWidth: false
                            Layout.minimumWidth: 120
                            font.pixelSize: 12
                        }

                        TextField {
                            id: tfCameraIp
                            text: settingsCtrl.pSettingsBean.pCameraIp
                            placeholderText: "Camera IP address"
                            inputMask: "000.000.000.000"
                            onEditingFinished: settingsCtrl.pSettingsBean.pCameraIp = tfCameraIp.text
                        }

                        Text {
                            id: tCameraPort
                            text: qsTr("Camera Port")
                            Layout.minimumWidth: 120
                            font.pixelSize: 12
                        }

                        TextField {
                            id: tfCameraPort
                            text: settingsCtrl.pSettingsBean.pCameraPort
                            placeholderText: "Camera Port"
                            inputMask: "00000"
                            onEditingFinished: settingsCtrl.pSettingsBean.pCameraPort = tfCameraPort.text
                        }

                        Item {
                            id: element4
                            width: 200
                            height: 200
                            Layout.columnSpan: 2
                            Layout.fillWidth: false
                            Layout.fillHeight: true
                            Layout.preferredWidth: 0
                            Layout.preferredHeight: 1
                        }
                    }

                    GridLayout {
                        id: gridLayout3
                        width: 100
                        height: 100
                        Item {
                            id: element5
                            width: 200
                            height: 200
                            Layout.fillWidth: true
                            Layout.preferredWidth: -1
                            Layout.preferredHeight: 0
                        }

                        Button {
                            id: bCameraSet
                            text: qsTr("Set Camera Configuration")
                            onClicked: settingsCtrl.saveParameters()
                        }
                    }
                }
            }

        }


    }

}

/*##^## Designer {
    D{i:20;anchors_height:100;anchors_width:100}D{i:21;anchors_height:100;anchors_width:100;anchors_x:76;anchors_y:85}
D{i:22;anchors_height:100;anchors_width:100;anchors_x:76;anchors_y:85}D{i:26;anchors_height:100;anchors_width:100}
D{i:31;anchors_height:100;anchors_width:100}D{i:32;anchors_height:100;anchors_width:100;anchors_x:76;anchors_y:85}
D{i:33;anchors_height:100;anchors_width:100;anchors_x:76;anchors_y:85}D{i:37;anchors_height:100;anchors_width:100}
}
 ##^##*/
