import QtQuick 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.3

//import "../controller/"
import SettingsController 1.0
import ProcessController 1.0
import ProcessBean 1.0
import SettingsBean 1.0

/*Item {*/

ApplicationWindow {

    id: mainWindow
    width: 1024
    height: 768
    //    flags: Qt.CustomizeWindowHint | Qt.Window

    Dialog {
        id: operationDialog
        standardButtons: Dialog.Ok
        width: 200
        height: 80

        Text {
            id: operationDialogText
            anchors.centerIn: parent
            text: ""
        }

    }

    // definizione segnali
    Connections {
        target: mainWindow
        onClosing: {
            processCtrl.closingApplicationSignal()
        }
    }

    Connections {
        target: processCtrl
        onShowDialogSignal: {
            operationDialogText.text = message
            operationDialog.visible = true
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
        //        onLaserFolderItemsChanged: lvCameraFolder.forceLayout()
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

    minimumWidth: 1024
    minimumHeight: 768
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
            currentIndex: 1
            TabButton {
                text: qsTr("Process")
            }
            TabButton {
                text: qsTr("Settings")
            }
            Component.onCompleted: tabBar.currentIndex = 0

        }

        Text {
            id: tVersione
            text: qsTr("Versione - ") + settingsBean.pVersion
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignRight
            Layout.fillWidth: true
            font.pixelSize: 12
            Layout.rightMargin: 10
//            anchors.right: glMain.right
//            anchors.rightMargin: 10
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
                        rows: 2
                        columns: 4

                        TextField {
                            id: tfFolderPath
                            text: settingsBean.pLocalLoadingPath
                            Layout.columnSpan: 3
                            Layout.fillWidth: true
                            onEditingFinished: processCtrl.setLocalLoadingPath(tfFolderPath.text)
                        }

                        Button {

                            FileDialog {
                                id: localLoadingPathFileDialog
                                title: qsTr("Choose a folder")
                                selectFolder: true
                                onAccepted: processCtrl.setLocalLoadingPath(localLoadingPathFileDialog.fileUrl)
                            }

                            id: bChangeFolder
                            width: 120
                            height: 40
                            text: qsTr("Change local folder")
                            Layout.minimumWidth: 140
                            rightPadding: 15
                            leftPadding: 15
                            onClicked: {
                                localLoadingPathFileDialog.folder = processCtrl.getUrlFromNativePath(settingsBean.pLocalLoadingPath)
                                localLoadingPathFileDialog.open()
                            }
                        }

                        TextField {
                            id: tfCsvFilenameRO
                            text: settingsBean.pLocalCsvFilename
                            Layout.fillWidth: true
                            readOnly: true
                        }

                        Button {
                            id: bSendToDevices
                            width: 120
                            text: qsTr("Send CSV to devices")
                            Layout.minimumWidth: 140
                            rightPadding: 15
                            leftPadding: 15
                            onClicked: processCtrl.sendCsvFileToDevices()
                        }

                        Button {
                            id: bRemoveFromDevices
                            width: 120
                            text: qsTr("Remove CSV devices")
                            Layout.minimumWidth: 140
                            onClicked: processCtrl.removeCsvFileFromDevices()
                        }

                        Button {
                            id: bRemoveErrorFromLaser
                            width: 120
                            text: qsTr("Remove Error")
                            Layout.minimumWidth: 140
                            onClicked: processCtrl.removeErrorFileFromLaser()
                        }



                    }

                    RowLayout {
                        id: rowLayout
                        width: 100
                        height: 450
                        scale: 1
                        Layout.fillHeight: false
                        visible: true
                        Layout.fillWidth: true

                        GridLayout {
                            id: gLaserView
                            columnSpacing: 10
                            rowSpacing: 10
                            Layout.columnSpan: 1
                            clip: false
                            Layout.rowSpan: 1
                            rows: 1
                            Layout.fillWidth: true
                            Layout.fillHeight: true
                            columns: 3

                            Text {
                                id: tLaser
                                text: qsTr("Laser Folder")
                                Layout.columnSpan: 3
                                Layout.preferredWidth: 100
                                Layout.fillWidth: true
                                font.pixelSize: 12
                            }

                            Text {
                                id: tLaserWatcher
                                text: qsTr("Watcher")
                                Layout.fillWidth: true
                                Layout.columnSpan: 2
                                font.pixelSize: 12
                            }

                            RoundButton {
                                id: rbLaserWatcher
                                width: 30
                                height: 30
                                text: ""
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                                Layout.preferredHeight: 30
                                Layout.preferredWidth: 30
                                background: Rectangle {
                                    id: rbLaserWatcherRect
                                    radius: rbLaserWatcher.radius
                                    color: "red"
                                }

                                Connections {
                                    target: processBean
                                    onLaserWatcherRunningChanged: rbLaserWatcher.updateButton(processBean.pLaserWatcherRunning)
                                }

                                function updateButton(isRunning) {
                                    if (isRunning)
                                        rbLaserWatcherRect.color = "green"
                                    else
                                        rbLaserWatcherRect.color = "red"
                                }

                            }

                            Text {
                                id: tLaserConnection
                                text: qsTr("Connection")
                                Layout.fillWidth: true
                                Layout.columnSpan: 2
                                font.pixelSize: 12
                            }

                            RoundButton {
                                id: rbLaserConnection
                                width: 30
                                height: 30
                                text: ""
                                Layout.preferredHeight: 30
                                Layout.preferredWidth: 30
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter

                                background: Rectangle {
                                    id: rbLaserConnectionRect
                                    radius: rbLaserConnection.radius
                                    color: "red"
                                }

                                Connections {
                                    target: processBean
                                    onLaserConnectionUpChanged: rbLaserConnection.updateButton(processBean.pLaserConnectionUp)
                                }

                                function updateButton(isConnected) {
                                    if (isConnected)
                                        rbLaserConnectionRect.color = "green"
                                    else
                                        rbLaserConnectionRect.color = "red"
                                }

                            }

                            ListView {
                                id: lvLaserFolder
                                x: 0
                                y: 0
                                Layout.minimumHeight: 180
                                clip: true
                                Layout.fillHeight: true
                                Layout.columnSpan: 3
                                Layout.fillWidth: true
                                spacing: 4
                                model: processBean.pLaserFolderItems
                                opacity: processBean.pLaserConnectionUp ? 1.0 : 0.4
                                enabled: processBean.pLaserConnectionUp

                                delegate: Item {
                                    id: lvLaserFolderItem
                                    x: 5
                                    width: parent.width
                                    height: 40

                                    Row {
                                        id: lvLaserFolderItemRow

                                        Text {
                                            padding: 10
                                            id: lvLaserFolderItemText
                                            parent: lvLaserFolderItem
                                            text: modelData
                                            font.bold: true
                                            anchors.verticalCenter: parent.verticalCenter

                                            Rectangle {
                                                parent: lvLaserFolderItem
                                                width: parent.width
                                                height: parent.height
                                                anchors.top: parent.top
                                                color: "#112233FF"
                                            }
                                        }
                                    }
                                }

                                ScrollBar.vertical: ScrollBar {
                                    parent: lvLaserFolder
                                    anchors.top: lvLaserFolder.top
                                    anchors.bottom: lvLaserFolder.bottom
                                    interactive: true
                                    policy: "AlwaysOn"
                                    clip: true
                                }

                            }

                            Item {
                                id: element
                                width: 0
                                height: 0
                                Layout.fillHeight: false
                                Layout.fillWidth: true
                                visible: true
                            }

                            Button {
                                id: bStartLaserWatcher
                                text: qsTr("Start")
                                enabled: !processBean.pLaserWatcherRunning
                                onClicked: processCtrl.startLaserWatcher()
                            }

                            Button {
                                id: bStopLaserWatcher
                                text: qsTr("Stop")
                                enabled: processBean.pLaserWatcherRunning
                                onClicked: processCtrl.stopLaserWatcher()
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
                            columnSpacing: 10
                            rowSpacing: 10
                            Layout.fillHeight: true
                            rows: 1
                            columns: 3

                            Text {
                                id: tCamera
                                text: qsTr("Camera Folder")
                                Layout.columnSpan: 3
                                Layout.preferredWidth: 100
                                Layout.fillWidth: true
                                font.pixelSize: 12
                            }

                            Text {
                                id: tCameraWatcher
                                text: qsTr("Watcher")
                                Layout.columnSpan: 2
                                Layout.fillWidth: true
                                font.pixelSize: 12
                            }

                            RoundButton {
                                id: rbCameraWatcher
                                width: 30
                                height: 30
                                text: ""
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                                Layout.preferredHeight: 30
                                Layout.preferredWidth: 30

                                background: Rectangle {
                                    id: rbCameraWatcherRect
                                    radius: rbLaserConnection.radius
                                    color: "red"
                                }

                                Connections {
                                    target: processBean
                                    onCameraWatcherRunningChanged: rbCameraWatcher.updateButton(processBean.pCameraWatcherRunning)
                                }

                                function updateButton(isRunning) {
                                    if (isRunning)
                                        rbCameraWatcherRect.color = "green"
                                    else
                                        rbCameraWatcherRect.color = "red"
                                }

                            }

                            Text {
                                id: tCameraConnection
                                text: qsTr("Connection")
                                Layout.columnSpan: 2
                                Layout.fillWidth: true
                                font.pixelSize: 12
                            }

                            RoundButton {
                                id: rbCameraConnection
                                width: 30
                                height: 30
                                text: ""
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                                Layout.preferredHeight: 30
                                Layout.preferredWidth: 30

                                background: Rectangle {
                                    id: rbCameraConnectionRect
                                    radius: rbLaserConnection.radius
                                    color: "red"
                                }

                                Connections {
                                    target: processBean
                                    onCameraConnectionUpChanged: rbCameraConnection.updateButton(processBean.pCameraConnectionUp)
                                }

                                function updateButton(isConnected) {
                                    if (isConnected)
                                        rbCameraConnectionRect.color = "green"
                                    else
                                        rbCameraConnectionRect.color = "red"
                                }

                            }

                            ListView {
                                id: lvCameraFolder
                                Layout.minimumHeight: 180
                                Layout.fillHeight: true
                                clip: true
                                Layout.columnSpan: 3
                                Layout.fillWidth: true
                                spacing: 4
                                model: processBean.pCameraFolderItems
                                opacity: processBean.pCameraConnectionUp ? 1.0 : 0.4
                                enabled: processBean.pCameraConnectionUp

                                delegate: Item {
                                    id: lvCameraFolderItem
                                    x: 5
                                    width: parent.width
                                    height: 40

                                    Row {
                                        id: lvCameraFolderItemRow

                                        Text {
                                            padding: 10
                                            id: lvCameraFolderItemText
                                            parent: lvCameraFolderItem
                                            text: modelData
                                            font.bold: true
                                            anchors.verticalCenter: parent.verticalCenter

                                            Rectangle {
                                                parent: lvCameraFolderItem
                                                width: parent.width
                                                height: parent.height
                                                anchors.top: parent.top
                                                color: "#112233FF"
                                            }
                                        }
                                        spacing: 10
                                    }
                                }

                                ScrollBar.vertical: ScrollBar {
                                    anchors.top: lvCameraFolder.top
                                    anchors.bottom: lvCameraFolder.bottom
                                    interactive: true
                                    policy: "AlwaysOn"
                                    clip: true
                                }

                            }

                            Item {
                                id: element1
                                width: 0
                                height: 0
                                Layout.fillHeight: false
                                Layout.fillWidth: true
                                Layout.columnSpan: 1
                            }

                            Button {
                                id: bStarCameraWatcher
                                text: qsTr("Start")
                                enabled: !processBean.pCameraWatcherRunning
                                onClicked: processCtrl.startCameraWatcher()
                            }

                            Button {
                                id: bStopCameraWatcher
                                text: qsTr("Stop")
                                enabled: processBean.pCameraWatcherRunning
                                onClicked: processCtrl.stopCameraWatcher()
                            }





                        }

                    }

                    Frame {
                        id: fRegeneration
                        width: 200
                        height: 200
                        opacity: 1
                        padding: 0
                        leftPadding: 0
                        rightPadding: 0
                        bottomPadding: 0
                        topPadding: 0
                        Layout.fillHeight: true
                        Layout.fillWidth: true

                        GridLayout {
                            id: gRegeneration
                            columns: 7
                            rows: 2
                            visible: true
                            anchors.fill: parent
                            Layout.fillHeight: true
                            Layout.fillWidth: true

                            function getColor(status) {
                                if (status === 0)
                                    return "lightGray"
                                else if (status === 1)
                                    return "orange"
                                else if (status === 2)
                                    return "green"
                                else
                                    return "red"
                            }

                            Item {
                                id: itemErrorFounded
                                width: 130
                                height: 65
                                Layout.fillWidth: false
                                Layout.columnSpan: 1
                                RoundButton {
                                    id: rbErrorFounded
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: processBean.pErrorFileFounded ? "red" : "lightGray"
                                    }
                                }
                                Text {
                                    id: tErrorFounded
                                    text: qsTr("ERROR FOUNDED")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemCsvCreationRunning
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbCsvCreationRunning
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: processBean.pCsvRegThreadRunning ? ( processBean.pCsvRegThreadPause ? "orange" : "green" ) : "lightGray"
                                    }
                                }
                                Text {
                                    id: tCsvCreationRunning
                                    text: qsTr("CSV CREATION RUN")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemSpacer
                                width: 130
                                height: 1
                                Layout.fillHeight: false
                                Layout.fillWidth: true
                                Layout.columnSpan: 3
                            }

                            Item {
                                id: itemCsvNewEmpty
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbCsvNewEmpty
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: processBean.pCsvRegThreadCsvNewEmpty ? "blue" : "lightGray"
                                    }
                                }
                                Text {
                                    id: tCsvNewEmpty
                                    text: qsTr("NEW CSV MANUALLY")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            ColumnLayout {
                                id: columnLayout
                                width: 100
                                height: 100
                                spacing: 0

                                CheckBox {
                                    id: cbStop
                                    text: qsTr("Stop")
                                    padding: 1
                                    onCheckedChanged: processCtrl.changeStopRequestValue(cbStop.checked)
                                }

                                CheckBox {
                                    id: cbPause
                                    text: qsTr("Pause")
                                    padding: 1
                                    onCheckedChanged: processCtrl.changePauseRequestValue(cbPause.checked)
                                }
                            }

                            Item {
                                id: itemCleanLocalFolderStatus
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbCleanLocalFolderStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadCleanLocalFolderStatus)
                                    }
                                }
                                Text {
                                    id: tCleanLocalFolderStatus
                                    text: qsTr("CLEAN LOCAL FOLDER")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemCleanCameraFolderStatus
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbCleanCameraFolderStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadCleanCameraFolderStatus)
                                    }
                                }
                                Text {
                                    id: tCleanCameraFolderStatus
                                    text: qsTr("CLEAN CAMERA FOLDER")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemSpacer2
                                width: 130
                                height: 1
                                Layout.fillHeight: false
                                Layout.fillWidth: true
                                Layout.columnSpan: 5
                            }

                            Item {
                                id: itemRenameLaserItemsStatus
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbRenameLaserItemsStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadRenameLaserItemsStatus)
                                    }
                                }
                                Text {
                                    id: tRenameLaserItemsStatus
                                    text: qsTr("RENAME LASER ITEMS")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemDownloadItemsStatus
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbDownloadItemsStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadDownloadItemsStatus)
                                    }
                                }
                                Text {
                                    id: tDownloadItemsStatus
                                    text: qsTr("DOWNLOAD")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemCleanLaserFolderStatus
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbCleanLaserFolderStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadCleanLaserFolderStatus)
                                    }
                                }
                                Text {
                                    id: tCleanLaserFolderStatus
                                    text: qsTr("CLEAN LASER FOLDER")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemCsvCreationProcessStatus
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbCsvCreationProcessStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadCsvCreationProcessStatus)
                                    }
                                }
                                Text {
                                    id: tCsvCreationProcessStatus
                                    text: qsTr("CREATION CSV")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemSendCsvToLaserStatus
                                width: 130
                                height: 65
                                Layout.columnSpan: 1
                                RoundButton {
                                    id: rbSendCsvToLaserStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadSendCsvToLaserStatus)
                                    }
                                }
                                Text {
                                    id: tSendCsvToLaserStatus
                                    text: qsTr("SEND CSV LASER")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }

                            Item {
                                id: itemSendCsvToCameraStatus
                                width: 130
                                height: 65
                                RoundButton {
                                    id: rbSendCsvToCameraStatus
                                    width: 40
                                    height: 40
                                    text: ""
                                    anchors.horizontalCenter: parent.horizontalCenter

                                    background: Rectangle {
                                        radius: parent.radius
                                        color: gRegeneration.getColor(processBean.pCsvRegThreadSendCsvToCameraStatus)
                                    }
                                }
                                Text {
                                    id: tSendCsvToCameraStatus
                                    text: qsTr("SEND CSV CAMERA")
                                    anchors.bottom: parent.bottom
                                    anchors.bottomMargin: 0
                                    anchors.horizontalCenter: parent.horizontalCenter
                                }
                            }



                        }
                    }

                    GridLayout {
                        id: gFooter
                        width: 100
                        height: 100

                        Item {
                            Layout.fillHeight: false
                            Layout.fillWidth: true
                        }

                    }




                }
            }

            Item {
                id: settings
                Layout.fillHeight: true
                Layout.fillWidth: true

                GridLayout {
                    id: gridLayout
                    layoutDirection: Qt.LeftToRight
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 10
                    anchors.topMargin: 10
                    columnSpacing: 50
                    rowSpacing: 50
                    columns: 2

                    ColumnLayout {
                        id: cameraSettingsLayout
                        Layout.fillWidth: true
                        GridLayout {
                            id: gridLayout2
                            Layout.fillHeight: true
                            Layout.fillWidth: true
                            columns: 2
                            columnSpacing: 5

                            Text {
                                id: tCameraPath
                                text: qsTr("Camera path")
                                Layout.minimumWidth: 120
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfCameraPath
                                Layout.fillWidth: true
                                text: settingsBean.pCameraRemotePath
                                onEditingFinished: processCtrl.setCameraRemotePath(tfCameraPath.text)
                            }

                            Button {

                                FileDialog {
                                    id: cameraFileDialog
                                    title: qsTr("Choose a folder")
                                    selectFolder: true
                                    onAccepted: processCtrl.setCameraRemotePath(cameraFileDialog.fileUrl)
                                }

                                id: bCameraFolder
                                text: qsTr("Change camera folder")
                                Layout.minimumWidth: 140
                                rightPadding: 15
                                leftPadding: 15
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                                Layout.columnSpan: 2
                                onClicked: {
                                    cameraFileDialog.folder = processCtrl.getUrlFromNativePath(settingsBean.pCameraRemotePath)
                                    cameraFileDialog.open()
                                }

                            }

                            Text {
                                id: tCameraPollingTimeMs
                                text: qsTr("Polling time [ms]")
                                Layout.minimumWidth: 120
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfCameraPollingTimeMs
                                text: settingsBean.pCameraPollingTimeMs
                                Layout.columnSpan: 1
                                Layout.fillWidth: true
                                validator: IntValidator {
                                    bottom: 100;
                                    top: 100000;
                                }
                                onEditingFinished: settingsBean.pCameraPollingTimeMs = tfCameraPollingTimeMs.text
                            }

                            Item {
                                id: element6
                                width: 0
                                height: 0
                                Layout.fillWidth: true
                            }

                            CheckBox {
                                id: cbCameraSendCsv
                                text: qsTr("Send CSV to camera")
                                checked: settingsBean.pCameraSendCSV
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                                leftPadding: 0
                                onCheckedChanged: settingsBean.pCameraSendCSV = cbCameraSendCsv.checked
                            }

                            Item {
                                id: element4
                                Layout.columnSpan: 2
                                Layout.fillWidth: false
                                Layout.fillHeight: true
                                Layout.preferredWidth: 0
                                Layout.preferredHeight: 1
                            }




                        }

                        GridLayout {
                            id: gridLayout3
                            Layout.fillWidth: true

                            Button {
                                id: bCameraSet
                                text: qsTr("Set camera configuration")
                                Layout.fillWidth: true
                                rightPadding: 15
                                leftPadding: 15
                                onClicked: settingsCtrl.saveParameters()
                            }
                        }
                    }

                    ColumnLayout {
                        id: laserSettingsLayout
                        Layout.fillWidth: true

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
                                text: settingsBean.pLaserIp
                                Layout.columnSpan: 1
                                Layout.fillWidth: true
                                placeholderText: "Laser IP address"
                                inputMask: "000.000.000.000"
                                onEditingFinished: settingsBean.pLaserIp = text
                            }

                            Text {
                                id: tLaserPort
                                text: qsTr("Laser port")
                                Layout.minimumWidth: 120
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfLaserPort
                                text: "%0".arg(settingsBean.pLaserPort)
                                Layout.columnSpan: 1
                                Layout.fillWidth: true
                                placeholderText: "Laser Port"
                                inputMask: "00000"
                                onEditingFinished: settingsBean.pLaserPort = tfLaserPort.text
                            }

                            Text {
                                id: tLaserPollingTimeMs
                                text: qsTr("Polling time [ms]")
                                Layout.minimumWidth: 120
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfLaserPollingTimeMs
                                text: settingsBean.pLaserPollingTimeMs
                                Layout.columnSpan: 1
                                Layout.fillWidth: true
                                validator: IntValidator {
                                    bottom: 100;
                                    top: 100000;
                                }
                                onEditingFinished: settingsBean.pLaserPollingTimeMs = tfLaserPollingTimeMs.text
                            }

                            Text {
                                id: tLaserRemotePath
                                text: qsTr("Laser remote path")
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfLaserRemotePath
                                text: settingsBean.pLaserRemotePath
                                Layout.fillWidth: true
                                onEditingFinished: settingsBean.pLaserRemotePath = tfLaserRemotePath.text
                            }

                            Item {
                                id: element3
                                Layout.columnSpan: 2
                                Layout.preferredHeight: 1
                                Layout.preferredWidth: 0
                                Layout.fillHeight: true
                            }

                        }

                        GridLayout {
                            id: gridLayout1
                            columns: 2
                            Layout.fillWidth: true

                            Button {
                                id: bLaserSet
                                text: qsTr("Set laser configuration")
                                Layout.fillWidth: true
                                rightPadding: 15
                                leftPadding: 15
                                onClicked: settingsCtrl.saveParameters()
                            }

                        }

                    }

                    ColumnLayout {
                        id: localSettingsLayoutL
                        width: 100
                        height: 100
                        Layout.fillHeight: true
                        Layout.columnSpan: 1

                        GridLayout {
                            id: gridLayout4
                            width: 100
                            height: 100
                            columns: 2

                            Text {
                                id: tRigheScarto
                                text: qsTr("Righe scarto")
                                Layout.minimumWidth: 120
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfRigheScarto
                                text: settingsBean.pLocalRowMargin
                                validator: IntValidator {
                                    bottom: 0;
                                    top: 20;
                                }
                                onEditingFinished: settingsBean.pLocalRowMargin = tfRigheScarto.text
                                Layout.fillWidth: true
                            }

                            Text {
                                id: tWaitTimeBeforeProcess
                                text: qsTr("Wait time before process [s]")
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfWaitTimeBeforeProcess
                                text: settingsBean.pLocalWaitTimeBeforeProcess
                                validator: IntValidator {
                                    bottom: 1;
                                    top: 20;
                                }
                                onEditingFinished: settingsBean.pLocalWaitTimeBeforeProcess = tfWaitTimeBeforeProcess.text
                                Layout.fillWidth: true
                            }

                            Text {
                                id: tCsvFilename
                                text: qsTr("Nome file CSV")
                                Layout.minimumWidth: 120
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfCsvFilename
                                text: settingsBean.pLocalCsvFilename
                                Layout.fillWidth: true
                                onEditingFinished: settingsBean.pLocalCsvFilename = tfCsvFilename.text
                            }

                            Text {
                                id: tLaserErrorFilename
                                text: qsTr("Nome file errore laser")
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfLaserErrorFilename
                                text: settingsBean.pLocalLaserErrorFilename
                                Layout.fillWidth: true
                                onEditingFinished: settingsBean.pLocalLaserErrorFilename = tfLaserErrorFilename.text
                            }

                            Text {
                                id: tLaserLogFilename
                                text: qsTr("Nome file log")
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfLaserLogFilename
                                text: settingsBean.pLocalLaserLogFilename
                                Layout.fillWidth: true
                                onEditingFinished: settingsBean.pLocalLaserLogFilename = tfLaserLogFilename.text
                            }

                            Item {
                                id: element5
                                width: 200
                                height: 200
                                Layout.fillHeight: true
                            }

                        }
                    }

                    ColumnLayout {
                        id: localSettingsLayoutR
                        width: 100
                        height: 100
                        Layout.fillWidth: true
                        Layout.columnSpan: 1

                        GridLayout {
                            id: gridLayout5
                            width: 100
                            height: 100
                            columns: 2
                            Layout.columnSpan: 1

                            Text {
                                id: tLoadingPath
                                text: qsTr("Loading path")
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfLoadingPath
                                text: settingsBean.pLocalLoadingPath
                                Layout.fillWidth: true
                                onEditingFinished: processCtrl.setLocalLoadingPath(tfLoadingPath.text)
                            }

                            Button {

                                FileDialog {
                                    id: localLoadingPathFileDialog2
                                    title: qsTr("Choose a folder")
                                    selectFolder: true
                                    onAccepted: processCtrl.setLocalLoadingPath(localLoadingPathFileDialog2.fileUrl)
                                }

                                id: bLoadingPath
                                text: qsTr("Change loading path")
                                rightPadding: 15
                                leftPadding: 15
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                                Layout.columnSpan: 2
                                onClicked: {
                                    localLoadingPathFileDialog2.folder = processCtrl.getUrlFromNativePath(settingsBean.pLocalLoadingPath)
                                    localLoadingPathFileDialog2.open()
                                }
                            }

                            Text {
                                id: tDownloadPath
                                text: qsTr("Downloading path")
                                font.pixelSize: 12
                            }

                            TextField {
                                id: tfDownloadPath
                                text: settingsBean.pLocalDownloadingPath
                                Layout.fillWidth: true
                                onEditingFinished: settingsBean.pLocalDownloadingPath = tfDownloadPath.text
                            }

                            Button {

                                FileDialog {
                                    id: localDownloadingPathFileDialog
                                    title: qsTr("Choose a folder")
                                    selectFolder: true
                                    onAccepted: processCtrl.setLocalDownloadingPath(localDownloadingPathFileDialog.fileUrl)
                                }

                                id: bDownloadPath
                                text: qsTr("Change downloading path")
                                rightPadding: 15
                                leftPadding: 15
                                Layout.columnSpan: 2
                                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                                onClicked: {
                                    localDownloadingPathFileDialog.folder = processCtrl.getUrlFromNativePath(settingsBean.pLocalDownloadingPath)
                                    localDownloadingPathFileDialog.open()
                                }
                            }

                            Button {
                                id: bLocalSet
                                text: qsTr("Set local configuration")
                                Layout.columnSpan: 2
                                Layout.fillWidth: true
                                onClicked: settingsCtrl.saveParameters()
                            }

                            Item {
                                id: element2
                                width: 200
                                height: 200
                                Layout.fillHeight: true
                            }

                        }
                    }

                    Item {
                        id: spacer2
                        width: 0
                        height: 0
                        Layout.fillHeight: true
                    }

                }

            }

        }


    }

}

