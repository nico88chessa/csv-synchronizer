import QtQuick 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.3
import QtQuick.Dialogs 1.3

import "../controller/"
import SettingsController 1.0
import ProcessController 1.0
import ProcessBean 1.0
import SettingsBean 1.0

/*Item {*/

ApplicationWindow {

    id: mainWindow

    // definizione segnali
    Connections {
        target: mainWindow
        onClosing: {
            processCtrl.closingApplicationSignal()
        }
    }

    Component.onCompleted: {
        settingsCtrl.initBean()
        processCtrl.initBean()
    }

    // definizione oggetti C++
    QMLSettingsBean {
        id: settingsBean
    }

    QMLProcessBean {
        id: processBean
        onLaserFolderItemsChanged: lvCameraFolder.forceLayout()
//        onLaserFolderItemsChanged: mainWindow.width = (mainWindow.width == 800 ? 640 : 800)
    }

    QMLSettingsController {
        id: settingsCtrl
        pSettingsBean: settingsBean
    }

    QMLProcessController {
        id: processCtrl
        pProcessBean: processBean
        pSettingsBean: settingsBean
    }

    // definizione UI
    FileDialog {
        id: fileDialog
        title: qsTr("Choose a folder")
        folder: processCtrl.getUrlFromNativePath(processCtrl.pProcessBean.pLocalFolderPath)
        selectFolder: true
        onAccepted: processCtrl.handleUrlPath(fileDialog.fileUrl)
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
            Component.onCompleted: tabBar.currentIndex = 0

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
                    rows: 3
                    columns: 1

                    GridLayout {
                        id: gBody
                        width: 100
                        height: 100
                        Layout.fillWidth: true
                        rows: 3
                        columns: 3

                        TextField {
                            id: tfFolderPath
                            text: processCtrl.pProcessBean.pLocalFolderPath
                            placeholderText: qsTr("")
                            Layout.fillWidth: true
                        }


                        Button {
                            id: bChangeFolder
                            width: 200
                            height: 40
                            text: qsTr("Change Folder")
                            Layout.fillWidth: false
                            onClicked: fileDialog.open()
                        }

                        Button {
                            id: bSavePath
                            text: qsTr("Save Path")
                            onClicked: processCtrl.saveParameters()
                        }


                    }

                    RowLayout {
                        id: rowLayout
                        width: 100
                        height: 100
                        scale: 1
                        Layout.fillHeight: false
                        visible: true
                        Layout.fillWidth: true

                        GridLayout {
                            id: gLaserView
                            height: 100
                            columnSpacing: 10
                            rowSpacing: 10
                            Layout.columnSpan: 1
                            clip: false
                            Layout.rowSpan: 1
                            rows: 1
                            Layout.fillWidth: true
                            Layout.fillHeight: false
                            columns: 3

                            Text {
                                id: tLaser
                                text: qsTr("Laser Folder")
                                Layout.preferredWidth: 100
                                Layout.fillWidth: true
                                font.pixelSize: 12
                            }

                            RoundButton {
                                id: rbLaserConnected
                                text: ""
                                Layout.preferredHeight: 40
                                Layout.preferredWidth: 40
                                Layout.fillWidth: false
                            }

                            ListView {
                                id: lvLaserFolder
                                x: 0
                                y: 0
                                width: 110
                                height: 160
                                Layout.fillHeight: false
                                Layout.columnSpan: 2
                                Layout.fillWidth: true
                                delegate: Item {
                                    x: 5
                                    width: 80
                                    height: 40
                                    Row {
                                        id: row1
                                        Rectangle {
                                            width: 40
                                            height: 40
                                            color: colorCode
                                        }

                                        Text {
                                            text: name
                                            anchors.verticalCenter: parent.verticalCenter
                                            font.bold: true
                                        }
                                        spacing: 10
                                    }
                                }

                                model: ListModel {
                                    ListElement {
                                        name: "Grey"
                                        colorCode: "grey"
                                    }

                                    ListElement {
                                        name: "Red"
                                        colorCode: "red"
                                    }

                                    ListElement {
                                        name: "Blue"
                                        colorCode: "blue"
                                    }

                                    ListElement {
                                        name: "Green"
                                        colorCode: "green"
                                    }
                                }
                            }

                        }

                        ToolSeparator {
                            id: toolSeparator
                            topPadding: 2
                            Layout.fillHeight: true
                            Layout.rowSpan: 1
                            Layout.columnSpan: 1
                            padding: 10
                        }

                        GridLayout {
                            id: gCameraView
                            width: 100
                            height: 100
                            rows: 1
                            columns: 2

                            Text {
                                id: tCamera
                                text: qsTr("Camera Folder")
                                Layout.preferredWidth: 100
                                Layout.fillWidth: true
                                font.pixelSize: 12
                            }

                            RoundButton {
                                id: rbCameraConnected
                                text: ""
                                Layout.preferredHeight: 40
                                Layout.preferredWidth: 40
                            }

                            ListView {
                                id: lvCameraFolder
                                width: 110
                                height: 160
                                Layout.columnSpan: 2
                                Layout.fillWidth: true
                                delegate: Item {
                                    x: 5
                                    width: 80
                                    height: 40
                                    Row {
                                        id: row2
                                        Rectangle {
                                            width: 40
                                            height: 40
                                            color: "red"
                                        }

                                        Text {
                                            text: modelData
                                            anchors.verticalCenter: parent.verticalCenter
                                            font.bold: true
                                        }
                                        spacing: 10
                                    }
                                }
                                model: processBean.pLaserFolderItems
//                                model: ["apples", "oranges", "pears"]

//                                model: ListModel {
//                                    ListElement {
//                                        name: "Grey"
//                                        colorCode: "grey"
//                                    }

//                                    ListElement {
//                                        name: "Red"
//                                        colorCode: "red"
//                                    }

//                                    ListElement {
//                                        name: "Blue"
//                                        colorCode: "blue"
//                                    }

//                                    ListElement {
//                                        name: "Green"
//                                        colorCode: "green"
//                                    }
//                                }

                            }

                        }

                    }

                    Item {
                        id: spacer
                        width: 200
                        height: 200
                        Layout.fillHeight: true
                    }

                    GridLayout {
                        id: gFooter
                        width: 100
                        height: 100

                        Item {
                            Layout.fillHeight: false
                            Layout.fillWidth: true
                        }

                        Button {
                            id: bStop
                            text: qsTr("Button")
                            onClicked: processCtrl.startWatcher()
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

                        Text {
                            id: tLaserPollingTimeMs
                            text: qsTr("Polling Time [ms]")
                            font.pixelSize: 12
                        }

                        TextField {
                            id: tfLaserPollingTimeMs
                            text: settingsCtrl.pSettingsBean.pLaserPollingTimeMs
                            validator: IntValidator {
                                bottom: 100;
                                top: 100000;
                            }
                            onEditingFinished: settingsCtrl.pSettingsBean.pLaserPollingTimeMs = tfLaserPollingTimeMs.text
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

                        Text {
                            id: tCameraPollingTimeMs
                            text: qsTr("Polling Time [ms]")
                            font.pixelSize: 12
                        }

                        TextField {
                            id: tfCameraPollingTimeMs
                            text: settingsCtrl.pSettingsBean.pCameraPollingTimeMs
                            validator: IntValidator {
                                bottom: 100;
                                top: 100000;
                            }
                            onEditingFinished: settingsCtrl.pSettingsBean.pCameraPollingTimeMs = tfCameraPollingTimeMs.text
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
