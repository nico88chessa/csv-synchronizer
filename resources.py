# -*- coding: utf-8 -*-

# Resource object code
#
# Created: mer ott 30 11:45:30 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.1)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\xe6\x9f\
\xef\
\xbb\xbfimport QtQuick\
 2.12\x0d\x0aimport Qt\
Quick.Layouts 1.\
3\x0d\x0aimport QtQuic\
k.Controls 2.5\x0d\x0a\
import QtQuick.D\
ialogs 1.3\x0d\x0a\x0d\x0a//\
import \x22../contr\
oller/\x22\x0d\x0aimport \
SettingsControll\
er 1.0\x0d\x0aimport P\
rocessController\
 1.0\x0d\x0aimport Pro\
cessBean 1.0\x0d\x0aim\
port SettingsBea\
n 1.0\x0d\x0a\x0d\x0a/*Item \
{*/\x0d\x0a\x0d\x0aApplicati\
onWindow {\x0d\x0a\x0d\x0a  \
  id: mainWindow\
\x0d\x0a    width: 102\
4\x0d\x0a    height: 7\
68\x0d\x0a    //    fl\
ags: Qt.Customiz\
eWindowHint | Qt\
.Window\x0d\x0a\x0d\x0a    D\
ialog {\x0d\x0a       \
 id: operationDi\
alog\x0d\x0a        st\
andardButtons: D\
ialog.Ok\x0d\x0a      \
  width: 200\x0d\x0a  \
      height: 80\
\x0d\x0a\x0d\x0a        Text\
 {\x0d\x0a            \
id: operationDia\
logText\x0d\x0a       \
     anchors.cen\
terIn: parent\x0d\x0a \
           text:\
 \x22\x22\x0d\x0a        }\x0d\x0a\
\x0d\x0a    }\x0d\x0a\x0d\x0a    /\
/ definizione se\
gnali\x0d\x0a    Conne\
ctions {\x0d\x0a      \
  target: mainWi\
ndow\x0d\x0a        on\
Closing: {\x0d\x0a    \
        processC\
trl.closingAppli\
cationSignal()\x0d\x0a\
        }\x0d\x0a    }\
\x0d\x0a\x0d\x0a    Connecti\
ons {\x0d\x0a        t\
arget: processCt\
rl\x0d\x0a        onSh\
owDialogSignal: \
{\x0d\x0a            o\
perationDialogTe\
xt.text = messag\
e\x0d\x0a            o\
perationDialog.v\
isible = true\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a\x0d\x0a    Component\
.onCompleted: {\x0d\
\x0a        setting\
sCtrl.initBean()\
\x0d\x0a        proces\
sCtrl.initBean()\
\x0d\x0a    }\x0d\x0a\x0d\x0a    /\
/ definizione og\
getti C++\x0d\x0a    Q\
MLSettingsBean {\
\x0d\x0a        id: se\
ttingsBean\x0d\x0a    \
}\x0d\x0a\x0d\x0a    QMLProc\
essBean {\x0d\x0a     \
   id: processBe\
an\x0d\x0a        //  \
      onLaserFol\
derItemsChanged:\
 lvCameraFolder.\
forceLayout()\x0d\x0a \
       //       \
 onLaserFolderIt\
emsChanged: main\
Window.width = (\
mainWindow.width\
 == 800 ? 640 : \
800)\x0d\x0a    }\x0d\x0a\x0d\x0a \
   QMLSettingsCo\
ntroller {\x0d\x0a    \
    id: settings\
Ctrl\x0d\x0a        pS\
ettingsBean: set\
tingsBean\x0d\x0a    }\
\x0d\x0a\x0d\x0a    QMLProce\
ssController {\x0d\x0a\
        id: proc\
essCtrl\x0d\x0a       \
 pProcessBean: p\
rocessBean\x0d\x0a    \
    pSettingsBea\
n: settingsBean\x0d\
\x0a    }\x0d\x0a\x0d\x0a    mi\
nimumWidth: 1024\
\x0d\x0a    minimumHei\
ght: 768\x0d\x0a    vi\
sible: true\x0d\x0a\x0d\x0a \
   GridLayout {\x0d\
\x0a        id: glM\
ain\x0d\x0a        anc\
hors.fill: paren\
t\x0d\x0a        rows:\
 2\x0d\x0a        colu\
mns: 1\x0d\x0a\x0d\x0a      \
  TabBar {\x0d\x0a    \
        id: tabB\
ar\x0d\x0a            \
width: parent.wi\
dth\x0d\x0a           \
 Layout.fillWidt\
h: true\x0d\x0a       \
     currentInde\
x: 1\x0d\x0a          \
  TabButton {\x0d\x0a \
               t\
ext: qsTr(\x22Proce\
ss\x22)\x0d\x0a          \
  }\x0d\x0a           \
 TabButton {\x0d\x0a  \
              te\
xt: qsTr(\x22Settin\
gs\x22)\x0d\x0a          \
  }\x0d\x0a           \
 Component.onCom\
pleted: tabBar.c\
urrentIndex = 0\x0d\
\x0a\x0d\x0a        }\x0d\x0a\x0d\x0a\
        Text {\x0d\x0a\
            id: \
tVersione\x0d\x0a     \
       text: qsT\
r(\x22Versione - \x22)\
 + settingsBean.\
pVersion\x0d\x0a      \
      verticalAl\
ignment: Text.Al\
ignVCenter\x0d\x0a    \
        horizont\
alAlignment: Tex\
t.AlignRight\x0d\x0a  \
          Layout\
.fillWidth: true\
\x0d\x0a            fo\
nt.pixelSize: 12\
\x0d\x0a            La\
yout.rightMargin\
: 10\x0d\x0a//        \
    anchors.righ\
t: glMain.right\x0d\
\x0a//            a\
nchors.rightMarg\
in: 10\x0d\x0a        \
}\x0d\x0a\x0d\x0a        Sta\
ckLayout {\x0d\x0a\x0d\x0a  \
          width:\
 parent.width\x0d\x0a \
           Layou\
t.fillHeight: tr\
ue\x0d\x0a            \
currentIndex: ta\
bBar.currentInde\
x\x0d\x0a            i\
d: stackLayout\x0d\x0a\
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a\x0d\x0a          \
  Item {\x0d\x0a\x0d\x0a    \
            id: \
processItem\x0d\x0a\x0d\x0a \
               G\
ridLayout {\x0d\x0a   \
                \
 id: gMain\x0d\x0a    \
                \
anchors.rightMar\
gin: 10\x0d\x0a       \
             anc\
hors.leftMargin:\
 10\x0d\x0a           \
         anchors\
.bottomMargin: 1\
0\x0d\x0a             \
       anchors.t\
opMargin: 10\x0d\x0a  \
                \
  anchors.fill: \
parent\x0d\x0a        \
            clip\
: true\x0d\x0a        \
            rows\
: 3\x0d\x0a           \
         columns\
: 1\x0d\x0a\x0d\x0a         \
           GridL\
ayout {\x0d\x0a       \
                \
 id: gBody\x0d\x0a    \
                \
    width: 100\x0d\x0a\
                \
        height: \
100\x0d\x0a           \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
             row\
s: 2\x0d\x0a          \
              co\
lumns: 3\x0d\x0a\x0d\x0a    \
                \
    TextField {\x0d\
\x0a               \
             id:\
 tfFolderPath\x0d\x0a \
                \
           text:\
 settingsBean.pL\
ocalLoadingPath\x0d\
\x0a               \
             Lay\
out.columnSpan: \
2\x0d\x0a             \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
                \
   onEditingFini\
shed: processCtr\
l.setLocalLoadin\
gPath(tfFolderPa\
th.text)\x0d\x0a      \
                \
  }\x0d\x0a\x0d\x0a         \
               B\
utton {\x0d\x0a\x0d\x0a     \
                \
       FileDialo\
g {\x0d\x0a           \
                \
     id: localLo\
adingPathFileDia\
log\x0d\x0a           \
                \
     title: qsTr\
(\x22Choose a folde\
r\x22)\x0d\x0a           \
                \
     selectFolde\
r: true\x0d\x0a       \
                \
         onAccep\
ted: processCtrl\
.setLocalLoading\
Path(localLoadin\
gPathFileDialog.\
fileUrl)\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       id: bChan\
geFolder\x0d\x0a      \
                \
      width: 120\
\x0d\x0a              \
              he\
ight: 40\x0d\x0a      \
                \
      text: qsTr\
(\x22Change local f\
older\x22)\x0d\x0a       \
                \
     Layout.mini\
mumWidth: 140\x0d\x0a \
                \
           right\
Padding: 15\x0d\x0a   \
                \
         leftPad\
ding: 15\x0d\x0a      \
                \
      onClicked:\
 {\x0d\x0a            \
                \
    localLoading\
PathFileDialog.f\
older = processC\
trl.getUrlFromNa\
tivePath(setting\
sBean.pLocalLoad\
ingPath)\x0d\x0a      \
                \
          localL\
oadingPathFileDi\
alog.open()\x0d\x0a   \
                \
         }\x0d\x0a    \
                \
    }\x0d\x0a\x0d\x0a       \
                \
 TextField {\x0d\x0a  \
                \
          id: tf\
CsvFilenameRO\x0d\x0a \
                \
           text:\
 settingsBean.pL\
ocalCsvFilename\x0d\
\x0a               \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
 readOnly: true\x0d\
\x0a               \
         }\x0d\x0a\x0d\x0a  \
                \
      Button {\x0d\x0a\
                \
            id: \
bSendToDevices\x0d\x0a\
                \
            widt\
h: 120\x0d\x0a        \
                \
    text: qsTr(\x22\
Send CSV to devi\
ces\x22)\x0d\x0a         \
                \
   Layout.minimu\
mWidth: 140\x0d\x0a   \
                \
         rightPa\
dding: 15\x0d\x0a     \
                \
       leftPaddi\
ng: 15\x0d\x0a        \
                \
    onClicked: p\
rocessCtrl.sendC\
svFileToDevices(\
)\x0d\x0a             \
           }\x0d\x0a\x0d\x0a\
                \
        Button {\
\x0d\x0a              \
              id\
: bRemoveFromDev\
ices\x0d\x0a          \
                \
  width: 120\x0d\x0a  \
                \
          text: \
qsTr(\x22Remove CSV\
 devices\x22)\x0d\x0a    \
                \
        Layout.m\
inimumWidth: 140\
\x0d\x0a              \
              on\
Clicked: process\
Ctrl.removeCsvFi\
leFromDevices()\x0d\
\x0a               \
         }\x0d\x0a\x0d\x0a\x0d\x0a\
\x0d\x0a              \
      }\x0d\x0a\x0d\x0a     \
               R\
owLayout {\x0d\x0a    \
                \
    id: rowLayou\
t\x0d\x0a             \
           width\
: 100\x0d\x0a         \
               h\
eight: 450\x0d\x0a    \
                \
    scale: 1\x0d\x0a  \
                \
      Layout.fil\
lHeight: false\x0d\x0a\
                \
        visible:\
 true\x0d\x0a         \
               L\
ayout.fillWidth:\
 true\x0d\x0a\x0d\x0a       \
                \
 GridLayout {\x0d\x0a \
                \
           id: g\
LaserView\x0d\x0a     \
                \
       columnSpa\
cing: 10\x0d\x0a      \
                \
      rowSpacing\
: 10\x0d\x0a          \
                \
  Layout.columnS\
pan: 1\x0d\x0a        \
                \
    clip: false\x0d\
\x0a               \
             Lay\
out.rowSpan: 1\x0d\x0a\
                \
            rows\
: 1\x0d\x0a           \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
     Layout.fill\
Height: true\x0d\x0a  \
                \
          column\
s: 3\x0d\x0a\x0d\x0a        \
                \
    Text {\x0d\x0a    \
                \
            id: \
tLaser\x0d\x0a        \
                \
        text: qs\
Tr(\x22Laser Folder\
\x22)\x0d\x0a            \
                \
    Layout.colum\
nSpan: 3\x0d\x0a      \
                \
          Layout\
.preferredWidth:\
 100\x0d\x0a          \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
              fo\
nt.pixelSize: 12\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tLase\
rWatcher\x0d\x0a      \
                \
          text: \
qsTr(\x22Watcher\x22)\x0d\
\x0a               \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
         Layout.\
columnSpan: 2\x0d\x0a \
                \
               f\
ont.pixelSize: 1\
2\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
RoundButton {\x0d\x0a \
                \
               i\
d: rbLaserWatche\
r\x0d\x0a             \
                \
   width: 30\x0d\x0a  \
                \
              he\
ight: 30\x0d\x0a      \
                \
          text: \
\x22\x22\x0d\x0a            \
                \
    Layout.align\
ment: Qt.AlignRi\
ght | Qt.AlignVC\
enter\x0d\x0a         \
                \
       Layout.pr\
eferredHeight: 3\
0\x0d\x0a             \
                \
   Layout.prefer\
redWidth: 30\x0d\x0a  \
                \
              ba\
ckground: Rectan\
gle {\x0d\x0a         \
                \
           id: r\
bLaserWatcherRec\
t\x0d\x0a             \
                \
       radius: r\
bLaserWatcher.ra\
dius\x0d\x0a          \
                \
          color:\
 \x22red\x22\x0d\x0a        \
                \
        }\x0d\x0a\x0d\x0a   \
                \
             Con\
nections {\x0d\x0a    \
                \
                \
target: processB\
ean\x0d\x0a           \
                \
         onLaser\
WatcherRunningCh\
anged: rbLaserWa\
tcher.updateButt\
on(processBean.p\
LaserWatcherRunn\
ing)\x0d\x0a          \
                \
      }\x0d\x0a\x0d\x0a     \
                \
           funct\
ion updateButton\
(isRunning) {\x0d\x0a \
                \
                \
   if (isRunning\
)\x0d\x0a             \
                \
           rbLas\
erWatcherRect.co\
lor = \x22green\x22\x0d\x0a \
                \
                \
   else\x0d\x0a       \
                \
                \
 rbLaserWatcherR\
ect.color = \x22red\
\x22\x0d\x0a             \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     Text {\x0d\x0a   \
                \
             id:\
 tLaserConnectio\
n\x0d\x0a             \
                \
   text: qsTr(\x22C\
onnection\x22)\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
     Layout.colu\
mnSpan: 2\x0d\x0a     \
                \
           font.\
pixelSize: 12\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Roun\
dButton {\x0d\x0a     \
                \
           id: r\
bLaserConnection\
\x0d\x0a              \
                \
  width: 30\x0d\x0a   \
                \
             hei\
ght: 30\x0d\x0a       \
                \
         text: \x22\
\x22\x0d\x0a             \
                \
   Layout.prefer\
redHeight: 30\x0d\x0a \
                \
               L\
ayout.preferredW\
idth: 30\x0d\x0a      \
                \
          Layout\
.alignment: Qt.A\
lignRight | Qt.A\
lignVCenter\x0d\x0a\x0d\x0a \
                \
               b\
ackground: Recta\
ngle {\x0d\x0a        \
                \
            id: \
rbLaserConnectio\
nRect\x0d\x0a         \
                \
           radiu\
s: rbLaserConnec\
tion.radius\x0d\x0a   \
                \
                \
 color: \x22red\x22\x0d\x0a \
                \
               }\
\x0d\x0a\x0d\x0a            \
                \
    Connections \
{\x0d\x0a             \
                \
       target: p\
rocessBean\x0d\x0a    \
                \
                \
onLaserConnectio\
nUpChanged: rbLa\
serConnection.up\
dateButton(proce\
ssBean.pLaserCon\
nectionUp)\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
                \
 function update\
Button(isConnect\
ed) {\x0d\x0a         \
                \
           if (i\
sConnected)\x0d\x0a   \
                \
                \
     rbLaserConn\
ectionRect.color\
 = \x22green\x22\x0d\x0a    \
                \
                \
else\x0d\x0a          \
                \
              rb\
LaserConnectionR\
ect.color = \x22red\
\x22\x0d\x0a             \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     ListView {\x0d\
\x0a               \
                \
 id: lvLaserFold\
er\x0d\x0a            \
                \
    x: 0\x0d\x0a      \
                \
          y: 0\x0d\x0a\
                \
                \
Layout.minimumHe\
ight: 180\x0d\x0a     \
                \
           clip:\
 true\x0d\x0a         \
                \
       Layout.fi\
llHeight: true\x0d\x0a\
                \
                \
Layout.columnSpa\
n: 3\x0d\x0a          \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
              sp\
acing: 4\x0d\x0a      \
                \
          model:\
 processBean.pLa\
serFolderItems\x0d\x0a\
                \
                \
opacity: process\
Bean.pLaserConne\
ctionUp ? 1.0 : \
0.4\x0d\x0a           \
                \
     enabled: pr\
ocessBean.pLaser\
ConnectionUp\x0d\x0a\x0d\x0a\
                \
                \
delegate: Item {\
\x0d\x0a              \
                \
      id: lvLase\
rFolderItem\x0d\x0a   \
                \
                \
 x: 5\x0d\x0a         \
                \
           width\
: parent.width\x0d\x0a\
                \
                \
    height: 40\x0d\x0a\
\x0d\x0a              \
                \
      Row {\x0d\x0a   \
                \
                \
     id: lvLaser\
FolderItemRow\x0d\x0a\x0d\
\x0a               \
                \
         Text {\x0d\
\x0a               \
                \
             pad\
ding: 10\x0d\x0a      \
                \
                \
      id: lvLase\
rFolderItemText\x0d\
\x0a               \
                \
             par\
ent: lvLaserFold\
erItem\x0d\x0a        \
                \
                \
    text: modelD\
ata\x0d\x0a           \
                \
                \
 font.bold: true\
\x0d\x0a              \
                \
              an\
chors.verticalCe\
nter: parent.ver\
ticalCenter\x0d\x0a\x0d\x0a \
                \
                \
           Recta\
ngle {\x0d\x0a        \
                \
                \
        parent: \
lvLaserFolderIte\
m\x0d\x0a             \
                \
                \
   width: parent\
.width\x0d\x0a        \
                \
                \
        height: \
parent.height\x0d\x0a \
                \
                \
               a\
nchors.top: pare\
nt.top\x0d\x0a        \
                \
                \
        color: \x22\
#112233FF\x22\x0d\x0a    \
                \
                \
        }\x0d\x0a     \
                \
                \
   }\x0d\x0a          \
                \
          }\x0d\x0a   \
                \
             }\x0d\x0a\
\x0d\x0a              \
                \
  ScrollBar.vert\
ical: ScrollBar \
{\x0d\x0a             \
                \
       parent: l\
vLaserFolder\x0d\x0a  \
                \
                \
  anchors.top: l\
vLaserFolder.top\
\x0d\x0a              \
                \
      anchors.bo\
ttom: lvLaserFol\
der.bottom\x0d\x0a    \
                \
                \
interactive: tru\
e\x0d\x0a             \
                \
       policy: \x22\
AlwaysOn\x22\x0d\x0a     \
                \
               c\
lip: true\x0d\x0a     \
                \
           }\x0d\x0a\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             Ite\
m {\x0d\x0a           \
                \
     id: element\
\x0d\x0a              \
                \
  width: 0\x0d\x0a    \
                \
            heig\
ht: 0\x0d\x0a         \
                \
       Layout.fi\
llHeight: false\x0d\
\x0a               \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
         visible\
: true\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     Button {\x0d\x0a \
                \
               i\
d: bStartLaserWa\
tcher\x0d\x0a         \
                \
       text: qsT\
r(\x22Start\x22)\x0d\x0a    \
                \
            enab\
led: !processBea\
n.pLaserWatcherR\
unning\x0d\x0a        \
                \
        onClicke\
d: processCtrl.s\
tartLaserWatcher\
()\x0d\x0a            \
                \
}\x0d\x0a\x0d\x0a           \
                \
 Button {\x0d\x0a     \
                \
           id: b\
StopLaserWatcher\
\x0d\x0a              \
                \
  text: qsTr(\x22St\
op\x22)\x0d\x0a          \
                \
      enabled: p\
rocessBean.pLase\
rWatcherRunning\x0d\
\x0a               \
                \
 onClicked: proc\
essCtrl.stopLase\
rWatcher()\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\
\x0a\x0d\x0a\x0d\x0a           \
             }\x0d\x0a\
\x0d\x0a              \
          ToolSe\
parator {\x0d\x0a     \
                \
       id: toolS\
eparator\x0d\x0a      \
                \
      topPadding\
: 2\x0d\x0a           \
                \
 Layout.fillHeig\
ht: true\x0d\x0a      \
                \
      Layout.row\
Span: 1\x0d\x0a       \
                \
     Layout.colu\
mnSpan: 1\x0d\x0a     \
                \
       padding: \
10\x0d\x0a            \
            }\x0d\x0a\x0d\
\x0a               \
         GridLay\
out {\x0d\x0a         \
                \
   id: gCameraVi\
ew\x0d\x0a            \
                \
columnSpacing: 1\
0\x0d\x0a             \
               r\
owSpacing: 10\x0d\x0a \
                \
           Layou\
t.fillHeight: tr\
ue\x0d\x0a            \
                \
rows: 1\x0d\x0a       \
                \
     columns: 3\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tCame\
ra\x0d\x0a            \
                \
    text: qsTr(\x22\
Camera Folder\x22)\x0d\
\x0a               \
                \
 Layout.columnSp\
an: 3\x0d\x0a         \
                \
       Layout.pr\
eferredWidth: 10\
0\x0d\x0a             \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
           font.\
pixelSize: 12\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Text\
 {\x0d\x0a            \
                \
    id: tCameraW\
atcher\x0d\x0a        \
                \
        text: qs\
Tr(\x22Watcher\x22)\x0d\x0a \
                \
               L\
ayout.columnSpan\
: 2\x0d\x0a           \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
             fon\
t.pixelSize: 12\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Ro\
undButton {\x0d\x0a   \
                \
             id:\
 rbCameraWatcher\
\x0d\x0a              \
                \
  width: 30\x0d\x0a   \
                \
             hei\
ght: 30\x0d\x0a       \
                \
         text: \x22\
\x22\x0d\x0a             \
                \
   Layout.alignm\
ent: Qt.AlignRig\
ht | Qt.AlignVCe\
nter\x0d\x0a          \
                \
      Layout.pre\
ferredHeight: 30\
\x0d\x0a              \
                \
  Layout.preferr\
edWidth: 30\x0d\x0a\x0d\x0a \
                \
               b\
ackground: Recta\
ngle {\x0d\x0a        \
                \
            id: \
rbCameraWatcherR\
ect\x0d\x0a           \
                \
         radius:\
 rbLaserConnecti\
on.radius\x0d\x0a     \
                \
               c\
olor: \x22red\x22\x0d\x0a   \
                \
             }\x0d\x0a\
\x0d\x0a              \
                \
  Connections {\x0d\
\x0a               \
                \
     target: pro\
cessBean\x0d\x0a      \
                \
              on\
CameraWatcherRun\
ningChanged: rbC\
ameraWatcher.upd\
ateButton(proces\
sBean.pCameraWat\
cherRunning)\x0d\x0a  \
                \
              }\x0d\
\x0a\x0d\x0a             \
                \
   function upda\
teButton(isRunni\
ng) {\x0d\x0a         \
                \
           if (i\
sRunning)\x0d\x0a     \
                \
                \
   rbCameraWatch\
erRect.color = \x22\
green\x22\x0d\x0a        \
                \
            else\
\x0d\x0a              \
                \
          rbCame\
raWatcherRect.co\
lor = \x22red\x22\x0d\x0a   \
                \
             }\x0d\x0a\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tCame\
raConnection\x0d\x0a  \
                \
              te\
xt: qsTr(\x22Connec\
tion\x22)\x0d\x0a        \
                \
        Layout.c\
olumnSpan: 2\x0d\x0a  \
                \
              La\
yout.fillWidth: \
true\x0d\x0a          \
                \
      font.pixel\
Size: 12\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       RoundButt\
on {\x0d\x0a          \
                \
      id: rbCame\
raConnection\x0d\x0a  \
                \
              wi\
dth: 30\x0d\x0a       \
                \
         height:\
 30\x0d\x0a           \
                \
     text: \x22\x22\x0d\x0a \
                \
               L\
ayout.alignment:\
 Qt.AlignRight |\
 Qt.AlignVCenter\
\x0d\x0a              \
                \
  Layout.preferr\
edHeight: 30\x0d\x0a  \
                \
              La\
yout.preferredWi\
dth: 30\x0d\x0a\x0d\x0a     \
                \
           backg\
round: Rectangle\
 {\x0d\x0a            \
                \
        id: rbCa\
meraConnectionRe\
ct\x0d\x0a            \
                \
        radius: \
rbLaserConnectio\
n.radius\x0d\x0a      \
                \
              co\
lor: \x22red\x22\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
                \
 Connections {\x0d\x0a\
                \
                \
    target: proc\
essBean\x0d\x0a       \
                \
             onC\
ameraConnectionU\
pChanged: rbCame\
raConnection.upd\
ateButton(proces\
sBean.pCameraCon\
nectionUp)\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
                \
 function update\
Button(isConnect\
ed) {\x0d\x0a         \
                \
           if (i\
sConnected)\x0d\x0a   \
                \
                \
     rbCameraCon\
nectionRect.colo\
r = \x22green\x22\x0d\x0a   \
                \
                \
 else\x0d\x0a         \
                \
               r\
bCameraConnectio\
nRect.color = \x22r\
ed\x22\x0d\x0a           \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       ListView \
{\x0d\x0a             \
                \
   id: lvCameraF\
older\x0d\x0a         \
                \
       Layout.mi\
nimumHeight: 180\
\x0d\x0a              \
                \
  Layout.fillHei\
ght: true\x0d\x0a     \
                \
           clip:\
 true\x0d\x0a         \
                \
       Layout.co\
lumnSpan: 3\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
     spacing: 4\x0d\
\x0a               \
                \
 model: processB\
ean.pCameraFolde\
rItems\x0d\x0a        \
                \
        opacity:\
 processBean.pCa\
meraConnectionUp\
 ? 1.0 : 0.4\x0d\x0a  \
                \
              en\
abled: processBe\
an.pCameraConnec\
tionUp\x0d\x0a\x0d\x0a      \
                \
          delega\
te: Item {\x0d\x0a    \
                \
                \
id: lvCameraFold\
erItem\x0d\x0a        \
                \
            x: 5\
\x0d\x0a              \
                \
      width: par\
ent.width\x0d\x0a     \
                \
               h\
eight: 40\x0d\x0a\x0d\x0a   \
                \
                \
 Row {\x0d\x0a        \
                \
                \
id: lvCameraFold\
erItemRow\x0d\x0a\x0d\x0a   \
                \
                \
     Text {\x0d\x0a   \
                \
                \
         padding\
: 10\x0d\x0a          \
                \
                \
  id: lvCameraFo\
lderItemText\x0d\x0a  \
                \
                \
          parent\
: lvCameraFolder\
Item\x0d\x0a          \
                \
                \
  text: modelDat\
a\x0d\x0a             \
                \
               f\
ont.bold: true\x0d\x0a\
                \
                \
            anch\
ors.verticalCent\
er: parent.verti\
calCenter\x0d\x0a\x0d\x0a   \
                \
                \
         Rectang\
le {\x0d\x0a          \
                \
                \
      parent: lv\
CameraFolderItem\
\x0d\x0a              \
                \
                \
  width: parent.\
width\x0d\x0a         \
                \
                \
       height: p\
arent.height\x0d\x0a  \
                \
                \
              an\
chors.top: paren\
t.top\x0d\x0a         \
                \
                \
       color: \x22#\
112233FF\x22\x0d\x0a     \
                \
                \
       }\x0d\x0a      \
                \
                \
  }\x0d\x0a           \
                \
             spa\
cing: 10\x0d\x0a      \
                \
              }\x0d\
\x0a               \
                \
 }\x0d\x0a\x0d\x0a          \
                \
      ScrollBar.\
vertical: Scroll\
Bar {\x0d\x0a         \
                \
           ancho\
rs.top: lvCamera\
Folder.top\x0d\x0a    \
                \
                \
anchors.bottom: \
lvCameraFolder.b\
ottom\x0d\x0a         \
                \
           inter\
active: true\x0d\x0a  \
                \
                \
  policy: \x22Alway\
sOn\x22\x0d\x0a          \
                \
          clip: \
true\x0d\x0a          \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        Item {\x0d\x0a\
                \
                \
id: element1\x0d\x0a  \
                \
              wi\
dth: 0\x0d\x0a        \
                \
        height: \
0\x0d\x0a             \
                \
   Layout.fillHe\
ight: false\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
     Layout.colu\
mnSpan: 1\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        Button {\
\x0d\x0a              \
                \
  id: bStarCamer\
aWatcher\x0d\x0a      \
                \
          text: \
qsTr(\x22Start\x22)\x0d\x0a \
                \
               e\
nabled: !process\
Bean.pCameraWatc\
herRunning\x0d\x0a    \
                \
            onCl\
icked: processCt\
rl.startCameraWa\
tcher()\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      Button {\x0d\x0a\
                \
                \
id: bStopCameraW\
atcher\x0d\x0a        \
                \
        text: qs\
Tr(\x22Stop\x22)\x0d\x0a    \
                \
            enab\
led: processBean\
.pCameraWatcherR\
unning\x0d\x0a        \
                \
        onClicke\
d: processCtrl.s\
topCameraWatcher\
()\x0d\x0a            \
                \
}\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a   \
                \
     }\x0d\x0a\x0d\x0a      \
              }\x0d\
\x0a\x0d\x0a             \
       Frame {\x0d\x0a\
                \
        id: fReg\
eneration\x0d\x0a     \
                \
   width: 200\x0d\x0a \
                \
       height: 2\
00\x0d\x0a            \
            opac\
ity: 1\x0d\x0a        \
                \
padding: 0\x0d\x0a    \
                \
    leftPadding:\
 0\x0d\x0a            \
            righ\
tPadding: 0\x0d\x0a   \
                \
     bottomPaddi\
ng: 0\x0d\x0a         \
               t\
opPadding: 0\x0d\x0a  \
                \
      Layout.fil\
lHeight: true\x0d\x0a \
                \
       Layout.fi\
llWidth: true\x0d\x0a\x0d\
\x0a               \
         GridLay\
out {\x0d\x0a         \
                \
   id: gRegenera\
tion\x0d\x0a          \
                \
  columns: 7\x0d\x0a  \
                \
          rows: \
2\x0d\x0a             \
               v\
isible: true\x0d\x0a  \
                \
          anchor\
s.fill: parent\x0d\x0a\
                \
            Layo\
ut.fillHeight: t\
rue\x0d\x0a           \
                \
 Layout.fillWidt\
h: true\x0d\x0a\x0d\x0a     \
                \
       function \
getColor(status)\
 {\x0d\x0a            \
                \
    if (status =\
== 0)\x0d\x0a         \
                \
           retur\
n \x22lightGray\x22\x0d\x0a \
                \
               e\
lse if (status =\
== 1)\x0d\x0a         \
                \
           retur\
n \x22orange\x22\x0d\x0a    \
                \
            else\
 if (status === \
2)\x0d\x0a            \
                \
        return \x22\
green\x22\x0d\x0a        \
                \
        else\x0d\x0a  \
                \
                \
  return \x22red\x22\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             Ite\
m {\x0d\x0a           \
                \
     id: itemErr\
orFounded\x0d\x0a     \
                \
           width\
: 130\x0d\x0a         \
                \
       height: 6\
5\x0d\x0a             \
                \
   Layout.fillWi\
dth: false\x0d\x0a    \
                \
            Layo\
ut.columnSpan: 1\
\x0d\x0a              \
                \
  RoundButton {\x0d\
\x0a               \
                \
     id: rbError\
Founded\x0d\x0a       \
                \
             wid\
th: 40\x0d\x0a        \
                \
            heig\
ht: 40\x0d\x0a        \
                \
            text\
: \x22\x22\x0d\x0a          \
                \
          anchor\
s.horizontalCent\
er: parent.horiz\
ontalCenter\x0d\x0a\x0d\x0a \
                \
                \
   background: R\
ectangle {\x0d\x0a    \
                \
                \
    radius: pare\
nt.radius\x0d\x0a     \
                \
                \
   color: proces\
sBean.pErrorFile\
Founded ? \x22red\x22 \
: \x22lightGray\x22\x0d\x0a \
                \
                \
   }\x0d\x0a          \
                \
      }\x0d\x0a       \
                \
         Text {\x0d\
\x0a               \
                \
     id: tErrorF\
ounded\x0d\x0a        \
                \
            text\
: qsTr(\x22ERROR FO\
UNDED\x22)\x0d\x0a       \
                \
             anc\
hors.bottom: par\
ent.bottom\x0d\x0a    \
                \
                \
anchors.bottomMa\
rgin: 0\x0d\x0a       \
                \
             anc\
hors.horizontalC\
enter: parent.ho\
rizontalCenter\x0d\x0a\
                \
                \
}\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
Item {\x0d\x0a        \
                \
        id: item\
CsvCreationRunni\
ng\x0d\x0a            \
                \
    width: 130\x0d\x0a\
                \
                \
height: 65\x0d\x0a    \
                \
            Roun\
dButton {\x0d\x0a     \
                \
               i\
d: rbCsvCreation\
Running\x0d\x0a       \
                \
             wid\
th: 40\x0d\x0a        \
                \
            heig\
ht: 40\x0d\x0a        \
                \
            text\
: \x22\x22\x0d\x0a          \
                \
          anchor\
s.horizontalCent\
er: parent.horiz\
ontalCenter\x0d\x0a\x0d\x0a \
                \
                \
   background: R\
ectangle {\x0d\x0a    \
                \
                \
    radius: pare\
nt.radius\x0d\x0a     \
                \
                \
   color: proces\
sBean.pCsvRegThr\
eadRunning ? ( p\
rocessBean.pCsvR\
egThreadPause ? \
\x22orange\x22 : \x22gree\
n\x22 ) : \x22lightGra\
y\x22\x0d\x0a            \
                \
        }\x0d\x0a     \
                \
           }\x0d\x0a  \
                \
              Te\
xt {\x0d\x0a          \
                \
          id: tC\
svCreationRunnin\
g\x0d\x0a             \
                \
       text: qsT\
r(\x22CSV CREATION \
RUN\x22)\x0d\x0a         \
                \
           ancho\
rs.bottom: paren\
t.bottom\x0d\x0a      \
                \
              an\
chors.bottomMarg\
in: 0\x0d\x0a         \
                \
           ancho\
rs.horizontalCen\
ter: parent.hori\
zontalCenter\x0d\x0a  \
                \
              }\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              It\
em {\x0d\x0a          \
                \
      id: itemSp\
acer\x0d\x0a          \
                \
      width: 130\
\x0d\x0a              \
                \
  height: 1\x0d\x0a   \
                \
             Lay\
out.fillHeight: \
false\x0d\x0a         \
                \
       Layout.fi\
llWidth: true\x0d\x0a \
                \
               L\
ayout.columnSpan\
: 3\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Item {\x0d\x0a      \
                \
          id: it\
emCsvNewEmpty\x0d\x0a \
                \
               w\
idth: 130\x0d\x0a     \
                \
           heigh\
t: 65\x0d\x0a         \
                \
       RoundButt\
on {\x0d\x0a          \
                \
          id: rb\
CsvNewEmpty\x0d\x0a   \
                \
                \
 width: 40\x0d\x0a    \
                \
                \
height: 40\x0d\x0a    \
                \
                \
text: \x22\x22\x0d\x0a      \
                \
              an\
chors.horizontal\
Center: parent.h\
orizontalCenter\x0d\
\x0a\x0d\x0a             \
                \
       backgroun\
d: Rectangle {\x0d\x0a\
                \
                \
        radius: \
parent.radius\x0d\x0a \
                \
                \
       color: pr\
ocessBean.pCsvRe\
gThreadCsvNewEmp\
ty ? \x22blue\x22 : \x22l\
ightGray\x22\x0d\x0a     \
                \
               }\
\x0d\x0a              \
                \
  }\x0d\x0a           \
                \
     Text {\x0d\x0a   \
                \
                \
 id: tCsvNewEmpt\
y\x0d\x0a             \
                \
       text: qsT\
r(\x22NEW CSV MANUA\
LLY\x22)\x0d\x0a         \
                \
           ancho\
rs.bottom: paren\
t.bottom\x0d\x0a      \
                \
              an\
chors.bottomMarg\
in: 0\x0d\x0a         \
                \
           ancho\
rs.horizontalCen\
ter: parent.hori\
zontalCenter\x0d\x0a  \
                \
              }\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Co\
lumnLayout {\x0d\x0a  \
                \
              id\
: columnLayout\x0d\x0a\
                \
                \
width: 100\x0d\x0a    \
                \
            heig\
ht: 100\x0d\x0a       \
                \
         spacing\
: 0\x0d\x0a\x0d\x0a         \
                \
       CheckBox \
{\x0d\x0a             \
                \
       id: cbSto\
p\x0d\x0a             \
                \
       text: qsT\
r(\x22Stop\x22)\x0d\x0a     \
                \
               p\
adding: 1\x0d\x0a     \
                \
               o\
nCheckedChanged:\
 processCtrl.cha\
ngeStopRequestVa\
lue(cbStop.check\
ed)\x0d\x0a           \
                \
     }\x0d\x0a\x0d\x0a      \
                \
          CheckB\
ox {\x0d\x0a          \
                \
          id: cb\
Pause\x0d\x0a         \
                \
           text:\
 qsTr(\x22Pause\x22)\x0d\x0a\
                \
                \
    padding: 1\x0d\x0a\
                \
                \
    onCheckedCha\
nged: processCtr\
l.changePauseReq\
uestValue(cbPaus\
e.checked)\x0d\x0a    \
                \
            }\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Item\
 {\x0d\x0a            \
                \
    id: itemClea\
nLocalFolderStat\
us\x0d\x0a            \
                \
    width: 130\x0d\x0a\
                \
                \
height: 65\x0d\x0a    \
                \
            Roun\
dButton {\x0d\x0a     \
                \
               i\
d: rbCleanLocalF\
olderStatus\x0d\x0a   \
                \
                \
 width: 40\x0d\x0a    \
                \
                \
height: 40\x0d\x0a    \
                \
                \
text: \x22\x22\x0d\x0a      \
                \
              an\
chors.horizontal\
Center: parent.h\
orizontalCenter\x0d\
\x0a\x0d\x0a             \
                \
       backgroun\
d: Rectangle {\x0d\x0a\
                \
                \
        radius: \
parent.radius\x0d\x0a \
                \
                \
       color: gR\
egeneration.getC\
olor(processBean\
.pCsvRegThreadCl\
eanLocalFolderSt\
atus)\x0d\x0a         \
                \
           }\x0d\x0a  \
                \
              }\x0d\
\x0a               \
                \
 Text {\x0d\x0a       \
                \
             id:\
 tCleanLocalFold\
erStatus\x0d\x0a      \
                \
              te\
xt: qsTr(\x22CLEAN \
LOCAL FOLDER\x22)\x0d\x0a\
                \
                \
    anchors.bott\
om: parent.botto\
m\x0d\x0a             \
                \
       anchors.b\
ottomMargin: 0\x0d\x0a\
                \
                \
    anchors.hori\
zontalCenter: pa\
rent.horizontalC\
enter\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Item {\x0d\x0a \
                \
               i\
d: itemCleanCame\
raFolderStatus\x0d\x0a\
                \
                \
width: 130\x0d\x0a    \
                \
            heig\
ht: 65\x0d\x0a        \
                \
        RoundBut\
ton {\x0d\x0a         \
                \
           id: r\
bCleanCameraFold\
erStatus\x0d\x0a      \
                \
              wi\
dth: 40\x0d\x0a       \
                \
             hei\
ght: 40\x0d\x0a       \
                \
             tex\
t: \x22\x22\x0d\x0a         \
                \
           ancho\
rs.horizontalCen\
ter: parent.hori\
zontalCenter\x0d\x0a\x0d\x0a\
                \
                \
    background: \
Rectangle {\x0d\x0a   \
                \
                \
     radius: par\
ent.radius\x0d\x0a    \
                \
                \
    color: gRege\
neration.getColo\
r(processBean.pC\
svRegThreadClean\
CameraFolderStat\
us)\x0d\x0a           \
                \
         }\x0d\x0a    \
                \
            }\x0d\x0a \
                \
               T\
ext {\x0d\x0a         \
                \
           id: t\
CleanCameraFolde\
rStatus\x0d\x0a       \
                \
             tex\
t: qsTr(\x22CLEAN C\
AMERA FOLDER\x22)\x0d\x0a\
                \
                \
    anchors.bott\
om: parent.botto\
m\x0d\x0a             \
                \
       anchors.b\
ottomMargin: 0\x0d\x0a\
                \
                \
    anchors.hori\
zontalCenter: pa\
rent.horizontalC\
enter\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Item {\x0d\x0a \
                \
               i\
d: itemSpacer2\x0d\x0a\
                \
                \
width: 130\x0d\x0a    \
                \
            heig\
ht: 1\x0d\x0a         \
                \
       Layout.fi\
llHeight: false\x0d\
\x0a               \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
         Layout.\
columnSpan: 5\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Item\
 {\x0d\x0a            \
                \
    id: itemRena\
meLaserItemsStat\
us\x0d\x0a            \
                \
    width: 130\x0d\x0a\
                \
                \
height: 65\x0d\x0a    \
                \
            Roun\
dButton {\x0d\x0a     \
                \
               i\
d: rbRenameLaser\
ItemsStatus\x0d\x0a   \
                \
                \
 width: 40\x0d\x0a    \
                \
                \
height: 40\x0d\x0a    \
                \
                \
text: \x22\x22\x0d\x0a      \
                \
              an\
chors.horizontal\
Center: parent.h\
orizontalCenter\x0d\
\x0a\x0d\x0a             \
                \
       backgroun\
d: Rectangle {\x0d\x0a\
                \
                \
        radius: \
parent.radius\x0d\x0a \
                \
                \
       color: gR\
egeneration.getC\
olor(processBean\
.pCsvRegThreadRe\
nameLaserItemsSt\
atus)\x0d\x0a         \
                \
           }\x0d\x0a  \
                \
              }\x0d\
\x0a               \
                \
 Text {\x0d\x0a       \
                \
             id:\
 tRenameLaserIte\
msStatus\x0d\x0a      \
                \
              te\
xt: qsTr(\x22RENAME\
 LASER ITEMS\x22)\x0d\x0a\
                \
                \
    anchors.bott\
om: parent.botto\
m\x0d\x0a             \
                \
       anchors.b\
ottomMargin: 0\x0d\x0a\
                \
                \
    anchors.hori\
zontalCenter: pa\
rent.horizontalC\
enter\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Item {\x0d\x0a \
                \
               i\
d: itemDownloadI\
temsStatus\x0d\x0a    \
                \
            widt\
h: 130\x0d\x0a        \
                \
        height: \
65\x0d\x0a            \
                \
    RoundButton \
{\x0d\x0a             \
                \
       id: rbDow\
nloadItemsStatus\
\x0d\x0a              \
                \
      width: 40\x0d\
\x0a               \
                \
     height: 40\x0d\
\x0a               \
                \
     text: \x22\x22\x0d\x0a \
                \
                \
   anchors.horiz\
ontalCenter: par\
ent.horizontalCe\
nter\x0d\x0a\x0d\x0a        \
                \
            back\
ground: Rectangl\
e {\x0d\x0a           \
                \
             rad\
ius: parent.radi\
us\x0d\x0a            \
                \
            colo\
r: gRegeneration\
.getColor(proces\
sBean.pCsvRegThr\
eadDownloadItems\
Status)\x0d\x0a       \
                \
             }\x0d\x0a\
                \
                \
}\x0d\x0a             \
                \
   Text {\x0d\x0a     \
                \
               i\
d: tDownloadItem\
sStatus\x0d\x0a       \
                \
             tex\
t: qsTr(\x22DOWNLOA\
D\x22)\x0d\x0a           \
                \
         anchors\
.bottom: parent.\
bottom\x0d\x0a        \
                \
            anch\
ors.bottomMargin\
: 0\x0d\x0a           \
                \
         anchors\
.horizontalCente\
r: parent.horizo\
ntalCenter\x0d\x0a    \
                \
            }\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Item\
 {\x0d\x0a            \
                \
    id: itemClea\
nLaserFolderStat\
us\x0d\x0a            \
                \
    width: 130\x0d\x0a\
                \
                \
height: 65\x0d\x0a    \
                \
            Roun\
dButton {\x0d\x0a     \
                \
               i\
d: rbCleanLaserF\
olderStatus\x0d\x0a   \
                \
                \
 width: 40\x0d\x0a    \
                \
                \
height: 40\x0d\x0a    \
                \
                \
text: \x22\x22\x0d\x0a      \
                \
              an\
chors.horizontal\
Center: parent.h\
orizontalCenter\x0d\
\x0a\x0d\x0a             \
                \
       backgroun\
d: Rectangle {\x0d\x0a\
                \
                \
        radius: \
parent.radius\x0d\x0a \
                \
                \
       color: gR\
egeneration.getC\
olor(processBean\
.pCsvRegThreadCl\
eanLaserFolderSt\
atus)\x0d\x0a         \
                \
           }\x0d\x0a  \
                \
              }\x0d\
\x0a               \
                \
 Text {\x0d\x0a       \
                \
             id:\
 tCleanLaserFold\
erStatus\x0d\x0a      \
                \
              te\
xt: qsTr(\x22CLEAN \
LASER FOLDER\x22)\x0d\x0a\
                \
                \
    anchors.bott\
om: parent.botto\
m\x0d\x0a             \
                \
       anchors.b\
ottomMargin: 0\x0d\x0a\
                \
                \
    anchors.hori\
zontalCenter: pa\
rent.horizontalC\
enter\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Item {\x0d\x0a \
                \
               i\
d: itemCsvCreati\
onProcessStatus\x0d\
\x0a               \
                \
 width: 130\x0d\x0a   \
                \
             hei\
ght: 65\x0d\x0a       \
                \
         RoundBu\
tton {\x0d\x0a        \
                \
            id: \
rbCsvCreationPro\
cessStatus\x0d\x0a    \
                \
                \
width: 40\x0d\x0a     \
                \
               h\
eight: 40\x0d\x0a     \
                \
               t\
ext: \x22\x22\x0d\x0a       \
                \
             anc\
hors.horizontalC\
enter: parent.ho\
rizontalCenter\x0d\x0a\
\x0d\x0a              \
                \
      background\
: Rectangle {\x0d\x0a \
                \
                \
       radius: p\
arent.radius\x0d\x0a  \
                \
                \
      color: gRe\
generation.getCo\
lor(processBean.\
pCsvRegThreadCsv\
CreationProcessS\
tatus)\x0d\x0a        \
                \
            }\x0d\x0a \
                \
               }\
\x0d\x0a              \
                \
  Text {\x0d\x0a      \
                \
              id\
: tCsvCreationPr\
ocessStatus\x0d\x0a   \
                \
                \
 text: qsTr(\x22CRE\
ATION CSV\x22)\x0d\x0a   \
                \
                \
 anchors.bottom:\
 parent.bottom\x0d\x0a\
                \
                \
    anchors.bott\
omMargin: 0\x0d\x0a   \
                \
                \
 anchors.horizon\
talCenter: paren\
t.horizontalCent\
er\x0d\x0a            \
                \
    }\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    Item {\x0d\x0a    \
                \
            id: \
itemSendCsvToLas\
erStatus\x0d\x0a      \
                \
          width:\
 130\x0d\x0a          \
                \
      height: 65\
\x0d\x0a              \
                \
  Layout.columnS\
pan: 1\x0d\x0a        \
                \
        RoundBut\
ton {\x0d\x0a         \
                \
           id: r\
bSendCsvToLaserS\
tatus\x0d\x0a         \
                \
           width\
: 40\x0d\x0a          \
                \
          height\
: 40\x0d\x0a          \
                \
          text: \
\x22\x22\x0d\x0a            \
                \
        anchors.\
horizontalCenter\
: parent.horizon\
talCenter\x0d\x0a\x0d\x0a   \
                \
                \
 background: Rec\
tangle {\x0d\x0a      \
                \
                \
  radius: parent\
.radius\x0d\x0a       \
                \
                \
 color: gRegener\
ation.getColor(p\
rocessBean.pCsvR\
egThreadSendCsvT\
oLaserStatus)\x0d\x0a \
                \
                \
   }\x0d\x0a          \
                \
      }\x0d\x0a       \
                \
         Text {\x0d\
\x0a               \
                \
     id: tSendCs\
vToLaserStatus\x0d\x0a\
                \
                \
    text: qsTr(\x22\
SEND CSV LASER\x22)\
\x0d\x0a              \
                \
      anchors.bo\
ttom: parent.bot\
tom\x0d\x0a           \
                \
         anchors\
.bottomMargin: 0\
\x0d\x0a              \
                \
      anchors.ho\
rizontalCenter: \
parent.horizonta\
lCenter\x0d\x0a       \
                \
         }\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         Item {\x0d\
\x0a               \
                \
 id: itemSendCsv\
ToCameraStatus\x0d\x0a\
                \
                \
width: 130\x0d\x0a    \
                \
            heig\
ht: 65\x0d\x0a        \
                \
        RoundBut\
ton {\x0d\x0a         \
                \
           id: r\
bSendCsvToCamera\
Status\x0d\x0a        \
                \
            widt\
h: 40\x0d\x0a         \
                \
           heigh\
t: 40\x0d\x0a         \
                \
           text:\
 \x22\x22\x0d\x0a           \
                \
         anchors\
.horizontalCente\
r: parent.horizo\
ntalCenter\x0d\x0a\x0d\x0a  \
                \
                \
  background: Re\
ctangle {\x0d\x0a     \
                \
                \
   radius: paren\
t.radius\x0d\x0a      \
                \
                \
  color: gRegene\
ration.getColor(\
processBean.pCsv\
RegThreadSendCsv\
ToCameraStatus)\x0d\
\x0a               \
                \
     }\x0d\x0a        \
                \
        }\x0d\x0a     \
                \
           Text \
{\x0d\x0a             \
                \
       id: tSend\
CsvToCameraStatu\
s\x0d\x0a             \
                \
       text: qsT\
r(\x22SEND CSV CAME\
RA\x22)\x0d\x0a          \
                \
          anchor\
s.bottom: parent\
.bottom\x0d\x0a       \
                \
             anc\
hors.bottomMargi\
n: 0\x0d\x0a          \
                \
          anchor\
s.horizontalCent\
er: parent.horiz\
ontalCenter\x0d\x0a   \
                \
             }\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a\x0d\x0a\x0d\x0a           \
             }\x0d\x0a\
                \
    }\x0d\x0a\x0d\x0a       \
             Gri\
dLayout {\x0d\x0a     \
                \
   id: gFooter\x0d\x0a\
                \
        width: 1\
00\x0d\x0a            \
            heig\
ht: 100\x0d\x0a\x0d\x0a     \
                \
   Item {\x0d\x0a     \
                \
       Layout.fi\
llHeight: false\x0d\
\x0a               \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
             }\x0d\x0a\
\x0d\x0a              \
      }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\
\x0a               \
 }\x0d\x0a            \
}\x0d\x0a\x0d\x0a           \
 Item {\x0d\x0a       \
         id: set\
tings\x0d\x0a         \
       Layout.fi\
llHeight: true\x0d\x0a\
                \
Layout.fillWidth\
: true\x0d\x0a\x0d\x0a      \
          GridLa\
yout {\x0d\x0a        \
            id: \
gridLayout\x0d\x0a    \
                \
layoutDirection:\
 Qt.LeftToRight\x0d\
\x0a               \
     anchors.rig\
ht: parent.right\
\x0d\x0a              \
      anchors.bo\
ttom: parent.bot\
tom\x0d\x0a           \
         anchors\
.left: parent.le\
ft\x0d\x0a            \
        anchors.\
top: parent.top\x0d\
\x0a               \
     anchors.rig\
htMargin: 10\x0d\x0a  \
                \
  anchors.leftMa\
rgin: 10\x0d\x0a      \
              an\
chors.bottomMarg\
in: 10\x0d\x0a        \
            anch\
ors.topMargin: 1\
0\x0d\x0a             \
       columnSpa\
cing: 50\x0d\x0a      \
              ro\
wSpacing: 50\x0d\x0a  \
                \
  columns: 2\x0d\x0a\x0d\x0a\
                \
    ColumnLayout\
 {\x0d\x0a            \
            id: \
cameraSettingsLa\
yout\x0d\x0a          \
              La\
yout.fillWidth: \
true\x0d\x0a          \
              Gr\
idLayout {\x0d\x0a    \
                \
        id: grid\
Layout2\x0d\x0a       \
                \
     Layout.fill\
Height: true\x0d\x0a  \
                \
          Layout\
.fillWidth: true\
\x0d\x0a              \
              co\
lumns: 2\x0d\x0a      \
                \
      columnSpac\
ing: 5\x0d\x0a\x0d\x0a      \
                \
      Text {\x0d\x0a  \
                \
              id\
: tCameraPath\x0d\x0a \
                \
               t\
ext: qsTr(\x22Camer\
a path\x22)\x0d\x0a      \
                \
          Layout\
.minimumWidth: 1\
20\x0d\x0a            \
                \
    font.pixelSi\
ze: 12\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     TextField {\
\x0d\x0a              \
                \
  id: tfCameraPa\
th\x0d\x0a            \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
            text\
: settingsBean.p\
CameraRemotePath\
\x0d\x0a              \
                \
  onEditingFinis\
hed: processCtrl\
.setCameraRemote\
Path(tfCameraPat\
h.text)\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      Button {\x0d\x0a\
\x0d\x0a              \
                \
  FileDialog {\x0d\x0a\
                \
                \
    id: cameraFi\
leDialog\x0d\x0a      \
                \
              ti\
tle: qsTr(\x22Choos\
e a folder\x22)\x0d\x0a  \
                \
                \
  selectFolder: \
true\x0d\x0a          \
                \
          onAcce\
pted: processCtr\
l.setCameraRemot\
ePath(cameraFile\
Dialog.fileUrl)\x0d\
\x0a               \
                \
 }\x0d\x0a\x0d\x0a          \
                \
      id: bCamer\
aFolder\x0d\x0a       \
                \
         text: q\
sTr(\x22Change came\
ra folder\x22)\x0d\x0a   \
                \
             Lay\
out.minimumWidth\
: 140\x0d\x0a         \
                \
       rightPadd\
ing: 15\x0d\x0a       \
                \
         leftPad\
ding: 15\x0d\x0a      \
                \
          Layout\
.alignment: Qt.A\
lignRight | Qt.A\
lignVCenter\x0d\x0a   \
                \
             Lay\
out.columnSpan: \
2\x0d\x0a             \
                \
   onClicked: {\x0d\
\x0a               \
                \
     cameraFileD\
ialog.folder = p\
rocessCtrl.getUr\
lFromNativePath(\
settingsBean.pCa\
meraRemotePath)\x0d\
\x0a               \
                \
     cameraFileD\
ialog.open()\x0d\x0a  \
                \
              }\x0d\
\x0a\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
Text {\x0d\x0a        \
                \
        id: tCam\
eraPollingTimeMs\
\x0d\x0a              \
                \
  text: qsTr(\x22Po\
lling time [ms]\x22\
)\x0d\x0a             \
                \
   Layout.minimu\
mWidth: 120\x0d\x0a   \
                \
             fon\
t.pixelSize: 12\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Te\
xtField {\x0d\x0a     \
                \
           id: t\
fCameraPollingTi\
meMs\x0d\x0a          \
                \
      text: sett\
ingsBean.pCamera\
PollingTimeMs\x0d\x0a \
                \
               L\
ayout.columnSpan\
: 1\x0d\x0a           \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
             val\
idator: IntValid\
ator {\x0d\x0a        \
                \
            bott\
om: 100;\x0d\x0a      \
                \
              to\
p: 100000;\x0d\x0a    \
                \
            }\x0d\x0a \
                \
               o\
nEditingFinished\
: settingsBean.p\
CameraPollingTim\
eMs = tfCameraPo\
llingTimeMs.text\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               I\
tem {\x0d\x0a         \
                \
       id: eleme\
nt4\x0d\x0a           \
                \
     Layout.colu\
mnSpan: 2\x0d\x0a     \
                \
           Layou\
t.fillWidth: fal\
se\x0d\x0a            \
                \
    Layout.fillH\
eight: true\x0d\x0a   \
                \
             Lay\
out.preferredWid\
th: 0\x0d\x0a         \
                \
       Layout.pr\
eferredHeight: 1\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a       \
                \
 }\x0d\x0a\x0d\x0a          \
              Gr\
idLayout {\x0d\x0a    \
                \
        id: grid\
Layout3\x0d\x0a       \
                \
     Layout.fill\
Width: true\x0d\x0a\x0d\x0a \
                \
           Butto\
n {\x0d\x0a           \
                \
     id: bCamera\
Set\x0d\x0a           \
                \
     text: qsTr(\
\x22Set camera conf\
iguration\x22)\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
     rightPaddin\
g: 15\x0d\x0a         \
                \
       leftPaddi\
ng: 15\x0d\x0a        \
                \
        onClicke\
d: settingsCtrl.\
saveParameters()\
\x0d\x0a              \
              }\x0d\
\x0a               \
         }\x0d\x0a    \
                \
}\x0d\x0a\x0d\x0a           \
         ColumnL\
ayout {\x0d\x0a       \
                \
 id: laserSettin\
gsLayout\x0d\x0a      \
                \
  Layout.fillWid\
th: true\x0d\x0a\x0d\x0a    \
                \
    GridLayout {\
\x0d\x0a              \
              id\
: glLaser\x0d\x0a     \
                \
       Layout.fi\
llHeight: true\x0d\x0a\
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
columns: 2\x0d\x0a    \
                \
        columnSp\
acing: 5\x0d\x0a\x0d\x0a    \
                \
        Text {\x0d\x0a\
                \
                \
id: tLaserIp\x0d\x0a  \
                \
              te\
xt: qsTr(\x22Laser \
IP\x22)\x0d\x0a          \
                \
      Layout.min\
imumWidth: 120\x0d\x0a\
                \
                \
Layout.fillWidth\
: false\x0d\x0a       \
                \
         font.pi\
xelSize: 12\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          TextFi\
eld {\x0d\x0a         \
                \
       id: tfLas\
erIp\x0d\x0a          \
                \
      text: sett\
ingsBean.pLaserI\
p\x0d\x0a             \
                \
   Layout.column\
Span: 1\x0d\x0a       \
                \
         Layout.\
fillWidth: true\x0d\
\x0a               \
                \
 placeholderText\
: \x22Laser IP addr\
ess\x22\x0d\x0a          \
                \
      inputMask:\
 \x22000.000.000.00\
0\x22\x0d\x0a            \
                \
    onEditingFin\
ished: settingsB\
ean.pLaserIp = t\
ext\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Text {\x0d\x0a      \
                \
          id: tL\
aserPort\x0d\x0a      \
                \
          text: \
qsTr(\x22Laser port\
\x22)\x0d\x0a            \
                \
    Layout.minim\
umWidth: 120\x0d\x0a  \
                \
              fo\
nt.pixelSize: 12\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               T\
extField {\x0d\x0a    \
                \
            id: \
tfLaserPort\x0d\x0a   \
                \
             tex\
t: \x22%0\x22.arg(sett\
ingsBean.pLaserP\
ort)\x0d\x0a          \
                \
      Layout.col\
umnSpan: 1\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    placeholderT\
ext: \x22Laser Port\
\x22\x0d\x0a             \
                \
   inputMask: \x220\
0000\x22\x0d\x0a         \
                \
       onEditing\
Finished: settin\
gsBean.pLaserPor\
t = tfLaserPort.\
text\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Text {\x0d\x0a     \
                \
           id: t\
LaserPollingTime\
Ms\x0d\x0a            \
                \
    text: qsTr(\x22\
Polling time [ms\
]\x22)\x0d\x0a           \
                \
     Layout.mini\
mumWidth: 120\x0d\x0a \
                \
               f\
ont.pixelSize: 1\
2\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
TextField {\x0d\x0a   \
                \
             id:\
 tfLaserPollingT\
imeMs\x0d\x0a         \
                \
       text: set\
tingsBean.pLaser\
PollingTimeMs\x0d\x0a \
                \
               L\
ayout.columnSpan\
: 1\x0d\x0a           \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
             val\
idator: IntValid\
ator {\x0d\x0a        \
                \
            bott\
om: 100;\x0d\x0a      \
                \
              to\
p: 100000;\x0d\x0a    \
                \
            }\x0d\x0a \
                \
               o\
nEditingFinished\
: settingsBean.p\
LaserPollingTime\
Ms = tfLaserPoll\
ingTimeMs.text\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             Tex\
t {\x0d\x0a           \
                \
     id: tLaserR\
emotePath\x0d\x0a     \
                \
           text:\
 qsTr(\x22Laser rem\
ote path\x22)\x0d\x0a    \
                \
            font\
.pixelSize: 12\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             Tex\
tField {\x0d\x0a      \
                \
          id: tf\
LaserRemotePath\x0d\
\x0a               \
                \
 text: settingsB\
ean.pLaserRemote\
Path\x0d\x0a          \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
              on\
EditingFinished:\
 settingsBean.pL\
aserRemotePath =\
 tfLaserRemotePa\
th.text\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      Item {\x0d\x0a  \
                \
              id\
: element3\x0d\x0a    \
                \
            Layo\
ut.columnSpan: 2\
\x0d\x0a              \
                \
  Layout.preferr\
edHeight: 1\x0d\x0a   \
                \
             Lay\
out.preferredWid\
th: 0\x0d\x0a         \
                \
       Layout.fi\
llHeight: true\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
         }\x0d\x0a\x0d\x0a  \
                \
      GridLayout\
 {\x0d\x0a            \
                \
id: gridLayout1\x0d\
\x0a               \
             col\
umns: 2\x0d\x0a       \
                \
     Layout.fill\
Width: true\x0d\x0a\x0d\x0a \
                \
           Butto\
n {\x0d\x0a           \
                \
     id: bLaserS\
et\x0d\x0a            \
                \
    text: qsTr(\x22\
Set laser config\
uration\x22)\x0d\x0a     \
                \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
                \
   rightPadding:\
 15\x0d\x0a           \
                \
     leftPadding\
: 15\x0d\x0a          \
                \
      onClicked:\
 settingsCtrl.sa\
veParameters()\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
         }\x0d\x0a\x0d\x0a  \
                \
  }\x0d\x0a\x0d\x0a         \
           Colum\
nLayout {\x0d\x0a     \
                \
   id: localSett\
ingsLayoutL\x0d\x0a   \
                \
     width: 100\x0d\
\x0a               \
         height:\
 100\x0d\x0a          \
              La\
yout.fillHeight:\
 true\x0d\x0a         \
               L\
ayout.columnSpan\
: 1\x0d\x0a\x0d\x0a         \
               G\
ridLayout {\x0d\x0a   \
                \
         id: gri\
dLayout4\x0d\x0a      \
                \
      width: 100\
\x0d\x0a              \
              he\
ight: 100\x0d\x0a     \
                \
       columns: \
2\x0d\x0a\x0d\x0a           \
                \
 Text {\x0d\x0a       \
                \
         id: tRi\
gheScarto\x0d\x0a     \
                \
           text:\
 qsTr(\x22Righe sca\
rto\x22)\x0d\x0a         \
                \
       Layout.mi\
nimumWidth: 120\x0d\
\x0a               \
                \
 font.pixelSize:\
 12\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  TextField {\x0d\x0a \
                \
               i\
d: tfRigheScarto\
\x0d\x0a              \
                \
  text: settings\
Bean.pLocalRowMa\
rgin\x0d\x0a          \
                \
      validator:\
 IntValidator {\x0d\
\x0a               \
                \
     bottom: 0;\x0d\
\x0a               \
                \
     top: 20;\x0d\x0a \
                \
               }\
\x0d\x0a              \
                \
  onEditingFinis\
hed: settingsBea\
n.pLocalRowMargi\
n = tfRigheScart\
o.text\x0d\x0a        \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             Tex\
t {\x0d\x0a           \
                \
     id: tWaitTi\
meBeforeProcess\x0d\
\x0a               \
                \
 text: qsTr(\x22Wai\
t time before pr\
ocess [s]\x22)\x0d\x0a   \
                \
             fon\
t.pixelSize: 12\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Te\
xtField {\x0d\x0a     \
                \
           id: t\
fWaitTimeBeforeP\
rocess\x0d\x0a        \
                \
        text: se\
ttingsBean.pLoca\
lWaitTimeBeforeP\
rocess\x0d\x0a        \
                \
        validato\
r: IntValidator \
{\x0d\x0a             \
                \
       bottom: 1\
;\x0d\x0a             \
                \
       top: 20;\x0d\
\x0a               \
                \
 }\x0d\x0a            \
                \
    onEditingFin\
ished: settingsB\
ean.pLocalWaitTi\
meBeforeProcess \
= tfWaitTimeBefo\
reProcess.text\x0d\x0a\
                \
                \
Layout.fillWidth\
: true\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     Text {\x0d\x0a   \
                \
             id:\
 tCsvFilename\x0d\x0a \
                \
               t\
ext: qsTr(\x22Nome \
file CSV\x22)\x0d\x0a    \
                \
            Layo\
ut.minimumWidth:\
 120\x0d\x0a          \
                \
      font.pixel\
Size: 12\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       TextField\
 {\x0d\x0a            \
                \
    id: tfCsvFil\
ename\x0d\x0a         \
                \
       text: set\
tingsBean.pLocal\
CsvFilename\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
     onEditingFi\
nished: settings\
Bean.pLocalCsvFi\
lename = tfCsvFi\
lename.text\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tLaserErro\
rFilename\x0d\x0a     \
                \
           text:\
 qsTr(\x22Nome file\
 errore laser\x22)\x0d\
\x0a               \
                \
 font.pixelSize:\
 12\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  TextField {\x0d\x0a \
                \
               i\
d: tfLaserErrorF\
ilename\x0d\x0a       \
                \
         text: s\
ettingsBean.pLoc\
alLaserErrorFile\
name\x0d\x0a          \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
              on\
EditingFinished:\
 settingsBean.pL\
ocalLaserErrorFi\
lename = tfLaser\
ErrorFilename.te\
xt\x0d\x0a            \
                \
}\x0d\x0a\x0d\x0a           \
                \
 Text {\x0d\x0a       \
                \
         id: tLa\
serLogFilename\x0d\x0a\
                \
                \
text: qsTr(\x22Nome\
 file log\x22)\x0d\x0a   \
                \
             fon\
t.pixelSize: 12\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Te\
xtField {\x0d\x0a     \
                \
           id: t\
fLaserLogFilenam\
e\x0d\x0a             \
                \
   text: setting\
sBean.pLocalLase\
rLogFilename\x0d\x0a  \
                \
              La\
yout.fillWidth: \
true\x0d\x0a          \
                \
      onEditingF\
inished: setting\
sBean.pLocalLase\
rLogFilename = t\
fLaserLogFilenam\
e.text\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     Item {\x0d\x0a   \
                \
             id:\
 element5\x0d\x0a     \
                \
           width\
: 200\x0d\x0a         \
                \
       height: 2\
00\x0d\x0a            \
                \
    Layout.fillH\
eight: true\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
      }\x0d\x0a       \
             }\x0d\x0a\
\x0d\x0a              \
      ColumnLayo\
ut {\x0d\x0a          \
              id\
: localSettingsL\
ayoutR\x0d\x0a        \
                \
width: 100\x0d\x0a    \
                \
    height: 100\x0d\
\x0a               \
         Layout.\
fillWidth: true\x0d\
\x0a               \
         Layout.\
columnSpan: 1\x0d\x0a\x0d\
\x0a               \
         GridLay\
out {\x0d\x0a         \
                \
   id: gridLayou\
t5\x0d\x0a            \
                \
width: 100\x0d\x0a    \
                \
        height: \
100\x0d\x0a           \
                \
 columns: 2\x0d\x0a   \
                \
         Layout.\
columnSpan: 1\x0d\x0a\x0d\
\x0a               \
             Tex\
t {\x0d\x0a           \
                \
     id: tLoadin\
gPath\x0d\x0a         \
                \
       text: qsT\
r(\x22Loading path\x22\
)\x0d\x0a             \
                \
   font.pixelSiz\
e: 12\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    TextField {\x0d\
\x0a               \
                \
 id: tfLoadingPa\
th\x0d\x0a            \
                \
    text: settin\
gsBean.pLocalLoa\
dingPath\x0d\x0a      \
                \
          Layout\
.fillWidth: true\
\x0d\x0a              \
                \
  onEditingFinis\
hed: processCtrl\
.setLocalLoading\
Path(tfLoadingPa\
th.text)\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Button {\x0d\
\x0a\x0d\x0a             \
                \
   FileDialog {\x0d\
\x0a               \
                \
     id: localLo\
adingPathFileDia\
log2\x0d\x0a          \
                \
          title:\
 qsTr(\x22Choose a \
folder\x22)\x0d\x0a      \
                \
              se\
lectFolder: true\
\x0d\x0a              \
                \
      onAccepted\
: processCtrl.se\
tLocalLoadingPat\
h(localLoadingPa\
thFileDialog2.fi\
leUrl)\x0d\x0a        \
                \
        }\x0d\x0a\x0d\x0a   \
                \
             id:\
 bLoadingPath\x0d\x0a \
                \
               t\
ext: qsTr(\x22Chang\
e loading path\x22)\
\x0d\x0a              \
                \
  rightPadding: \
15\x0d\x0a            \
                \
    leftPadding:\
 15\x0d\x0a           \
                \
     Layout.alig\
nment: Qt.AlignR\
ight | Qt.AlignV\
Center\x0d\x0a        \
                \
        Layout.c\
olumnSpan: 2\x0d\x0a  \
                \
              on\
Clicked: {\x0d\x0a    \
                \
                \
localLoadingPath\
FileDialog2.fold\
er = processCtrl\
.getUrlFromNativ\
ePath(settingsBe\
an.pLocalLoading\
Path)\x0d\x0a         \
                \
           local\
LoadingPathFileD\
ialog2.open()\x0d\x0a \
                \
               }\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tDown\
loadPath\x0d\x0a      \
                \
          text: \
qsTr(\x22Downloadin\
g path\x22)\x0d\x0a      \
                \
          font.p\
ixelSize: 12\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           TextF\
ield {\x0d\x0a        \
                \
        id: tfDo\
wnloadPath\x0d\x0a    \
                \
            text\
: settingsBean.p\
LocalDownloading\
Path\x0d\x0a          \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
              on\
EditingFinished:\
 settingsBean.pL\
ocalDownloadingP\
ath = tfDownload\
Path.text\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        Button {\
\x0d\x0a\x0d\x0a            \
                \
    FileDialog {\
\x0d\x0a              \
                \
      id: localD\
ownloadingPathFi\
leDialog\x0d\x0a      \
                \
              ti\
tle: qsTr(\x22Choos\
e a folder\x22)\x0d\x0a  \
                \
                \
  selectFolder: \
true\x0d\x0a          \
                \
          onAcce\
pted: processCtr\
l.setLocalDownlo\
adingPath(localD\
ownloadingPathFi\
leDialog.fileUrl\
)\x0d\x0a             \
                \
   }\x0d\x0a\x0d\x0a        \
                \
        id: bDow\
nloadPath\x0d\x0a     \
                \
           text:\
 qsTr(\x22Change do\
wnloading path\x22)\
\x0d\x0a              \
                \
  rightPadding: \
15\x0d\x0a            \
                \
    leftPadding:\
 15\x0d\x0a           \
                \
     Layout.colu\
mnSpan: 2\x0d\x0a     \
                \
           Layou\
t.alignment: Qt.\
AlignRight | Qt.\
AlignVCenter\x0d\x0a  \
                \
              on\
Clicked: {\x0d\x0a    \
                \
                \
localDownloading\
PathFileDialog.f\
older = processC\
trl.getUrlFromNa\
tivePath(setting\
sBean.pLocalDown\
loadingPath)\x0d\x0a  \
                \
                \
  localDownloadi\
ngPathFileDialog\
.open()\x0d\x0a       \
                \
         }\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         Button \
{\x0d\x0a             \
                \
   id: bLocalSet\
\x0d\x0a              \
                \
  text: qsTr(\x22Se\
t local configur\
ation\x22)\x0d\x0a       \
                \
         Layout.\
columnSpan: 2\x0d\x0a \
                \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
                \
       onClicked\
: settingsCtrl.s\
aveParameters()\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              It\
em {\x0d\x0a          \
                \
      id: elemen\
t2\x0d\x0a            \
                \
    width: 200\x0d\x0a\
                \
                \
height: 200\x0d\x0a   \
                \
             Lay\
out.fillHeight: \
true\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
               }\
\x0d\x0a              \
      }\x0d\x0a\x0d\x0a     \
               I\
tem {\x0d\x0a         \
               i\
d: spacer2\x0d\x0a    \
                \
    width: 0\x0d\x0a  \
                \
      height: 0\x0d\
\x0a               \
         Layout.\
fillHeight: true\
\x0d\x0a              \
      }\x0d\x0a\x0d\x0a     \
           }\x0d\x0a\x0d\x0a\
            }\x0d\x0a\x0d\
\x0a        }\x0d\x0a\x0d\x0a\x0d\x0a\
    }\x0d\x0a\x0d\x0a}\x0d\x0a\x0d\x0a\
"

qt_resource_name = b"\
\x00\x02\
\x00\x00\x07\xb9\
\x00u\
\x00i\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
