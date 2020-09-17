# -*- coding: utf-8 -*-

# Resource object code
#
# Created: gio set 17 15:34:10 2020
#      by: The Resource Compiler for PySide2 (Qt v5.13.1)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\xea\xec\
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
lumns: 4\x0d\x0a\x0d\x0a    \
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
3\x0d\x0a             \
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
         }\x0d\x0a\x0d\x0a  \
                \
      Button {\x0d\x0a\
                \
            id: \
bRemoveErrorFrom\
Laser\x0d\x0a         \
                \
   width: 120\x0d\x0a \
                \
           text:\
 qsTr(\x22Remove Er\
ror\x22)\x0d\x0a         \
                \
   Layout.minimu\
mWidth: 140\x0d\x0a   \
                \
         onClick\
ed: processCtrl.\
removeErrorFileF\
romLaser()\x0d\x0a    \
                \
    }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a   \
                \
 }\x0d\x0a\x0d\x0a          \
          RowLay\
out {\x0d\x0a         \
               i\
d: rowLayout\x0d\x0a  \
                \
      width: 100\
\x0d\x0a              \
          height\
: 450\x0d\x0a         \
               s\
cale: 1\x0d\x0a       \
                \
 Layout.fillHeig\
ht: false\x0d\x0a     \
                \
   visible: true\
\x0d\x0a              \
          Layout\
.fillWidth: true\
\x0d\x0a\x0d\x0a            \
            Grid\
Layout {\x0d\x0a      \
                \
      id: gLaser\
View\x0d\x0a          \
                \
  columnSpacing:\
 10\x0d\x0a           \
                \
 rowSpacing: 10\x0d\
\x0a               \
             Lay\
out.columnSpan: \
1\x0d\x0a             \
               c\
lip: false\x0d\x0a    \
                \
        Layout.r\
owSpan: 1\x0d\x0a     \
                \
       rows: 1\x0d\x0a\
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
Layout.fillHeigh\
t: true\x0d\x0a       \
                \
     columns: 3\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tLase\
r\x0d\x0a             \
                \
   text: qsTr(\x22L\
aser Folder\x22)\x0d\x0a \
                \
               L\
ayout.columnSpan\
: 3\x0d\x0a           \
                \
     Layout.pref\
erredWidth: 100\x0d\
\x0a               \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
         font.pi\
xelSize: 12\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tLaserWatc\
her\x0d\x0a           \
                \
     text: qsTr(\
\x22Watcher\x22)\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    Layout.colum\
nSpan: 2\x0d\x0a      \
                \
          font.p\
ixelSize: 12\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           Round\
Button {\x0d\x0a      \
                \
          id: rb\
LaserWatcher\x0d\x0a  \
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
dth: 30\x0d\x0a       \
                \
         backgro\
und: Rectangle {\
\x0d\x0a              \
                \
      id: rbLase\
rWatcherRect\x0d\x0a  \
                \
                \
  radius: rbLase\
rWatcher.radius\x0d\
\x0a               \
                \
     color: \x22red\
\x22\x0d\x0a             \
                \
   }\x0d\x0a\x0d\x0a        \
                \
        Connecti\
ons {\x0d\x0a         \
                \
           targe\
t: processBean\x0d\x0a\
                \
                \
    onLaserWatch\
erRunningChanged\
: rbLaserWatcher\
.updateButton(pr\
ocessBean.pLaser\
WatcherRunning)\x0d\
\x0a               \
                \
 }\x0d\x0a\x0d\x0a          \
                \
      function u\
pdateButton(isRu\
nning) {\x0d\x0a      \
                \
              if\
 (isRunning)\x0d\x0a  \
                \
                \
      rbLaserWat\
cherRect.color =\
 \x22green\x22\x0d\x0a      \
                \
              el\
se\x0d\x0a            \
                \
            rbLa\
serWatcherRect.c\
olor = \x22red\x22\x0d\x0a  \
                \
              }\x0d\
\x0a\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
Text {\x0d\x0a        \
                \
        id: tLas\
erConnection\x0d\x0a  \
                \
              te\
xt: qsTr(\x22Connec\
tion\x22)\x0d\x0a        \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
                \
Layout.columnSpa\
n: 2\x0d\x0a          \
                \
      font.pixel\
Size: 12\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       RoundButt\
on {\x0d\x0a          \
                \
      id: rbLase\
rConnection\x0d\x0a   \
                \
             wid\
th: 30\x0d\x0a        \
                \
        height: \
30\x0d\x0a            \
                \
    text: \x22\x22\x0d\x0a  \
                \
              La\
yout.preferredHe\
ight: 30\x0d\x0a      \
                \
          Layout\
.preferredWidth:\
 30\x0d\x0a           \
                \
     Layout.alig\
nment: Qt.AlignR\
ight | Qt.AlignV\
Center\x0d\x0a\x0d\x0a      \
                \
          backgr\
ound: Rectangle \
{\x0d\x0a             \
                \
       id: rbLas\
erConnectionRect\
\x0d\x0a              \
                \
      radius: rb\
LaserConnection.\
radius\x0d\x0a        \
                \
            colo\
r: \x22red\x22\x0d\x0a      \
                \
          }\x0d\x0a\x0d\x0a \
                \
               C\
onnections {\x0d\x0a  \
                \
                \
  target: proces\
sBean\x0d\x0a         \
                \
           onLas\
erConnectionUpCh\
anged: rbLaserCo\
nnection.updateB\
utton(processBea\
n.pLaserConnecti\
onUp)\x0d\x0a         \
                \
       }\x0d\x0a\x0d\x0a    \
                \
            func\
tion updateButto\
n(isConnected) {\
\x0d\x0a              \
                \
      if (isConn\
ected)\x0d\x0a        \
                \
                \
rbLaserConnectio\
nRect.color = \x22g\
reen\x22\x0d\x0a         \
                \
           else\x0d\
\x0a               \
                \
         rbLaser\
ConnectionRect.c\
olor = \x22red\x22\x0d\x0a  \
                \
              }\x0d\
\x0a\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
ListView {\x0d\x0a    \
                \
            id: \
lvLaserFolder\x0d\x0a \
                \
               x\
: 0\x0d\x0a           \
                \
     y: 0\x0d\x0a     \
                \
           Layou\
t.minimumHeight:\
 180\x0d\x0a          \
                \
      clip: true\
\x0d\x0a              \
                \
  Layout.fillHei\
ght: true\x0d\x0a     \
                \
           Layou\
t.columnSpan: 3\x0d\
\x0a               \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
         spacing\
: 4\x0d\x0a           \
                \
     model: proc\
essBean.pLaserFo\
lderItems\x0d\x0a     \
                \
           opaci\
ty: processBean.\
pLaserConnection\
Up ? 1.0 : 0.4\x0d\x0a\
                \
                \
enabled: process\
Bean.pLaserConne\
ctionUp\x0d\x0a\x0d\x0a     \
                \
           deleg\
ate: Item {\x0d\x0a   \
                \
                \
 id: lvLaserFold\
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
id: lvLaserFolde\
rItemRow\x0d\x0a\x0d\x0a    \
                \
                \
    Text {\x0d\x0a    \
                \
                \
        padding:\
 10\x0d\x0a           \
                \
                \
 id: lvLaserFold\
erItemText\x0d\x0a    \
                \
                \
        parent: \
lvLaserFolderIte\
m\x0d\x0a             \
                \
               t\
ext: modelData\x0d\x0a\
                \
                \
            font\
.bold: true\x0d\x0a   \
                \
                \
         anchors\
.verticalCenter:\
 parent.vertical\
Center\x0d\x0a\x0d\x0a      \
                \
                \
      Rectangle \
{\x0d\x0a             \
                \
                \
   parent: lvLas\
erFolderItem\x0d\x0a  \
                \
                \
              wi\
dth: parent.widt\
h\x0d\x0a             \
                \
                \
   height: paren\
t.height\x0d\x0a      \
                \
                \
          anchor\
s.top: parent.to\
p\x0d\x0a             \
                \
                \
   color: \x22#1122\
33FF\x22\x0d\x0a         \
                \
                \
   }\x0d\x0a          \
                \
              }\x0d\
\x0a               \
                \
     }\x0d\x0a        \
                \
        }\x0d\x0a\x0d\x0a   \
                \
             Scr\
ollBar.vertical:\
 ScrollBar {\x0d\x0a  \
                \
                \
  parent: lvLase\
rFolder\x0d\x0a       \
                \
             anc\
hors.top: lvLase\
rFolder.top\x0d\x0a   \
                \
                \
 anchors.bottom:\
 lvLaserFolder.b\
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
id: element\x0d\x0a   \
                \
             wid\
th: 0\x0d\x0a         \
                \
       height: 0\
\x0d\x0a              \
                \
  Layout.fillHei\
ght: false\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    visible: tru\
e\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
Button {\x0d\x0a      \
                \
          id: bS\
tartLaserWatcher\
\x0d\x0a              \
                \
  text: qsTr(\x22St\
art\x22)\x0d\x0a         \
                \
       enabled: \
!processBean.pLa\
serWatcherRunnin\
g\x0d\x0a             \
                \
   onClicked: pr\
ocessCtrl.startL\
aserWatcher()\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Butt\
on {\x0d\x0a          \
                \
      id: bStopL\
aserWatcher\x0d\x0a   \
                \
             tex\
t: qsTr(\x22Stop\x22)\x0d\
\x0a               \
                \
 enabled: proces\
sBean.pLaserWatc\
herRunning\x0d\x0a    \
                \
            onCl\
icked: processCt\
rl.stopLaserWatc\
her()\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\
                \
        }\x0d\x0a\x0d\x0a   \
                \
     ToolSeparat\
or {\x0d\x0a          \
                \
  id: toolSepara\
tor\x0d\x0a           \
                \
 topPadding: 2\x0d\x0a\
                \
            Layo\
ut.fillHeight: t\
rue\x0d\x0a           \
                \
 Layout.rowSpan:\
 1\x0d\x0a            \
                \
Layout.columnSpa\
n: 1\x0d\x0a          \
                \
  padding: 10\x0d\x0a \
                \
       }\x0d\x0a\x0d\x0a    \
                \
    GridLayout {\
\x0d\x0a              \
              id\
: gCameraView\x0d\x0a \
                \
           colum\
nSpacing: 10\x0d\x0a  \
                \
          rowSpa\
cing: 10\x0d\x0a      \
                \
      Layout.fil\
lHeight: true\x0d\x0a \
                \
           rows:\
 1\x0d\x0a            \
                \
columns: 3\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tCamera\x0d\x0a \
                \
               t\
ext: qsTr(\x22Camer\
a Folder\x22)\x0d\x0a    \
                \
            Layo\
ut.columnSpan: 3\
\x0d\x0a              \
                \
  Layout.preferr\
edWidth: 100\x0d\x0a  \
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
       Text {\x0d\x0a \
                \
               i\
d: tCameraWatche\
r\x0d\x0a             \
                \
   text: qsTr(\x22W\
atcher\x22)\x0d\x0a      \
                \
          Layout\
.columnSpan: 2\x0d\x0a\
                \
                \
Layout.fillWidth\
: true\x0d\x0a        \
                \
        font.pix\
elSize: 12\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         RoundBu\
tton {\x0d\x0a        \
                \
        id: rbCa\
meraWatcher\x0d\x0a   \
                \
             wid\
th: 30\x0d\x0a        \
                \
        height: \
30\x0d\x0a            \
                \
    text: \x22\x22\x0d\x0a  \
                \
              La\
yout.alignment: \
Qt.AlignRight | \
Qt.AlignVCenter\x0d\
\x0a               \
                \
 Layout.preferre\
dHeight: 30\x0d\x0a   \
                \
             Lay\
out.preferredWid\
th: 30\x0d\x0a\x0d\x0a      \
                \
          backgr\
ound: Rectangle \
{\x0d\x0a             \
                \
       id: rbCam\
eraWatcherRect\x0d\x0a\
                \
                \
    radius: rbLa\
serConnection.ra\
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
         onCamer\
aWatcherRunningC\
hanged: rbCamera\
Watcher.updateBu\
tton(processBean\
.pCameraWatcherR\
unning)\x0d\x0a       \
                \
         }\x0d\x0a\x0d\x0a  \
                \
              fu\
nction updateBut\
ton(isRunning) {\
\x0d\x0a              \
                \
      if (isRunn\
ing)\x0d\x0a          \
                \
              rb\
CameraWatcherRec\
t.color = \x22green\
\x22\x0d\x0a             \
                \
       else\x0d\x0a   \
                \
                \
     rbCameraWat\
cherRect.color =\
 \x22red\x22\x0d\x0a        \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tCameraCon\
nection\x0d\x0a       \
                \
         text: q\
sTr(\x22Connection\x22\
)\x0d\x0a             \
                \
   Layout.column\
Span: 2\x0d\x0a       \
                \
         Layout.\
fillWidth: true\x0d\
\x0a               \
                \
 font.pixelSize:\
 12\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  RoundButton {\x0d\
\x0a               \
                \
 id: rbCameraCon\
nection\x0d\x0a       \
                \
         width: \
30\x0d\x0a            \
                \
    height: 30\x0d\x0a\
                \
                \
text: \x22\x22\x0d\x0a      \
                \
          Layout\
.alignment: Qt.A\
lignRight | Qt.A\
lignVCenter\x0d\x0a   \
                \
             Lay\
out.preferredHei\
ght: 30\x0d\x0a       \
                \
         Layout.\
preferredWidth: \
30\x0d\x0a\x0d\x0a          \
                \
      background\
: Rectangle {\x0d\x0a \
                \
                \
   id: rbCameraC\
onnectionRect\x0d\x0a \
                \
                \
   radius: rbLas\
erConnection.rad\
ius\x0d\x0a           \
                \
         color: \
\x22red\x22\x0d\x0a         \
                \
       }\x0d\x0a\x0d\x0a    \
                \
            Conn\
ections {\x0d\x0a     \
                \
               t\
arget: processBe\
an\x0d\x0a            \
                \
        onCamera\
ConnectionUpChan\
ged: rbCameraCon\
nection.updateBu\
tton(processBean\
.pCameraConnecti\
onUp)\x0d\x0a         \
                \
       }\x0d\x0a\x0d\x0a    \
                \
            func\
tion updateButto\
n(isConnected) {\
\x0d\x0a              \
                \
      if (isConn\
ected)\x0d\x0a        \
                \
                \
rbCameraConnecti\
onRect.color = \x22\
green\x22\x0d\x0a        \
                \
            else\
\x0d\x0a              \
                \
          rbCame\
raConnectionRect\
.color = \x22red\x22\x0d\x0a\
                \
                \
}\x0d\x0a\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  ListView {\x0d\x0a  \
                \
              id\
: lvCameraFolder\
\x0d\x0a              \
                \
  Layout.minimum\
Height: 180\x0d\x0a   \
                \
             Lay\
out.fillHeight: \
true\x0d\x0a          \
                \
      clip: true\
\x0d\x0a              \
                \
  Layout.columnS\
pan: 3\x0d\x0a        \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
                \
spacing: 4\x0d\x0a    \
                \
            mode\
l: processBean.p\
CameraFolderItem\
s\x0d\x0a             \
                \
   opacity: proc\
essBean.pCameraC\
onnectionUp ? 1.\
0 : 0.4\x0d\x0a       \
                \
         enabled\
: processBean.pC\
ameraConnectionU\
p\x0d\x0a\x0d\x0a           \
                \
     delegate: I\
tem {\x0d\x0a         \
                \
           id: l\
vCameraFolderIte\
m\x0d\x0a             \
                \
       x: 5\x0d\x0a   \
                \
                \
 width: parent.w\
idth\x0d\x0a          \
                \
          height\
: 40\x0d\x0a\x0d\x0a        \
                \
            Row \
{\x0d\x0a             \
                \
           id: l\
vCameraFolderIte\
mRow\x0d\x0a\x0d\x0a        \
                \
                \
Text {\x0d\x0a        \
                \
                \
    padding: 10\x0d\
\x0a               \
                \
             id:\
 lvCameraFolderI\
temText\x0d\x0a       \
                \
                \
     parent: lvC\
ameraFolderItem\x0d\
\x0a               \
                \
             tex\
t: modelData\x0d\x0a  \
                \
                \
          font.b\
old: true\x0d\x0a     \
                \
                \
       anchors.v\
erticalCenter: p\
arent.verticalCe\
nter\x0d\x0a\x0d\x0a        \
                \
                \
    Rectangle {\x0d\
\x0a               \
                \
                \
 parent: lvCamer\
aFolderItem\x0d\x0a   \
                \
                \
             wid\
th: parent.width\
\x0d\x0a              \
                \
                \
  height: parent\
.height\x0d\x0a       \
                \
                \
         anchors\
.top: parent.top\
\x0d\x0a              \
                \
                \
  color: \x22#11223\
3FF\x22\x0d\x0a          \
                \
                \
  }\x0d\x0a           \
                \
             }\x0d\x0a\
                \
                \
        spacing:\
 10\x0d\x0a           \
                \
         }\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
                \
 ScrollBar.verti\
cal: ScrollBar {\
\x0d\x0a              \
                \
      anchors.to\
p: lvCameraFolde\
r.top\x0d\x0a         \
                \
           ancho\
rs.bottom: lvCam\
eraFolder.bottom\
\x0d\x0a              \
                \
      interactiv\
e: true\x0d\x0a       \
                \
             pol\
icy: \x22AlwaysOn\x22\x0d\
\x0a               \
                \
     clip: true\x0d\
\x0a               \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Item {\x0d\x0a     \
                \
           id: e\
lement1\x0d\x0a       \
                \
         width: \
0\x0d\x0a             \
                \
   height: 0\x0d\x0a  \
                \
              La\
yout.fillHeight:\
 false\x0d\x0a        \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
                \
Layout.columnSpa\
n: 1\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Button {\x0d\x0a   \
                \
             id:\
 bStarCameraWatc\
her\x0d\x0a           \
                \
     text: qsTr(\
\x22Start\x22)\x0d\x0a      \
                \
          enable\
d: !processBean.\
pCameraWatcherRu\
nning\x0d\x0a         \
                \
       onClicked\
: processCtrl.st\
artCameraWatcher\
()\x0d\x0a            \
                \
}\x0d\x0a\x0d\x0a           \
                \
 Button {\x0d\x0a     \
                \
           id: b\
StopCameraWatche\
r\x0d\x0a             \
                \
   text: qsTr(\x22S\
top\x22)\x0d\x0a         \
                \
       enabled: \
processBean.pCam\
eraWatcherRunnin\
g\x0d\x0a             \
                \
   onClicked: pr\
ocessCtrl.stopCa\
meraWatcher()\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a        \
                \
}\x0d\x0a\x0d\x0a           \
         }\x0d\x0a\x0d\x0a  \
                \
  Frame {\x0d\x0a     \
                \
   id: fRegenera\
tion\x0d\x0a          \
              wi\
dth: 200\x0d\x0a      \
                \
  height: 200\x0d\x0a \
                \
       opacity: \
1\x0d\x0a             \
           paddi\
ng: 0\x0d\x0a         \
               l\
eftPadding: 0\x0d\x0a \
                \
       rightPadd\
ing: 0\x0d\x0a        \
                \
bottomPadding: 0\
\x0d\x0a              \
          topPad\
ding: 0\x0d\x0a       \
                \
 Layout.fillHeig\
ht: true\x0d\x0a      \
                \
  Layout.fillWid\
th: true\x0d\x0a\x0d\x0a    \
                \
    GridLayout {\
\x0d\x0a              \
              id\
: gRegeneration\x0d\
\x0a               \
             col\
umns: 7\x0d\x0a       \
                \
     rows: 2\x0d\x0a  \
                \
          visibl\
e: true\x0d\x0a       \
                \
     anchors.fil\
l: parent\x0d\x0a     \
                \
       Layout.fi\
llHeight: true\x0d\x0a\
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a\x0d\x0a          \
                \
  function getCo\
lor(status) {\x0d\x0a \
                \
               i\
f (status === 0)\
\x0d\x0a              \
                \
      return \x22li\
ghtGray\x22\x0d\x0a      \
                \
          else i\
f (status === 1)\
\x0d\x0a              \
                \
      return \x22or\
ange\x22\x0d\x0a         \
                \
       else if (\
status === 2)\x0d\x0a \
                \
                \
   return \x22green\
\x22\x0d\x0a             \
                \
   else\x0d\x0a       \
                \
             ret\
urn \x22red\x22\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        Item {\x0d\x0a\
                \
                \
id: itemErrorFou\
nded\x0d\x0a          \
                \
      width: 130\
\x0d\x0a              \
                \
  height: 65\x0d\x0a  \
                \
              La\
yout.fillWidth: \
false\x0d\x0a         \
                \
       Layout.co\
lumnSpan: 1\x0d\x0a   \
                \
             Rou\
ndButton {\x0d\x0a    \
                \
                \
id: rbErrorFound\
ed\x0d\x0a            \
                \
        width: 4\
0\x0d\x0a             \
                \
       height: 4\
0\x0d\x0a             \
                \
       text: \x22\x22\x0d\
\x0a               \
                \
     anchors.hor\
izontalCenter: p\
arent.horizontal\
Center\x0d\x0a\x0d\x0a      \
                \
              ba\
ckground: Rectan\
gle {\x0d\x0a         \
                \
               r\
adius: parent.ra\
dius\x0d\x0a          \
                \
              co\
lor: processBean\
.pErrorFileFound\
ed ? \x22red\x22 : \x22li\
ghtGray\x22\x0d\x0a      \
                \
              }\x0d\
\x0a               \
                \
 }\x0d\x0a            \
                \
    Text {\x0d\x0a    \
                \
                \
id: tErrorFounde\
d\x0d\x0a             \
                \
       text: qsT\
r(\x22ERROR FOUNDED\
\x22)\x0d\x0a            \
                \
        anchors.\
bottom: parent.b\
ottom\x0d\x0a         \
                \
           ancho\
rs.bottomMargin:\
 0\x0d\x0a            \
                \
        anchors.\
horizontalCenter\
: parent.horizon\
talCenter\x0d\x0a     \
                \
           }\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           Item \
{\x0d\x0a             \
                \
   id: itemCsvCr\
eationRunning\x0d\x0a \
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
CsvCreationRunni\
ng\x0d\x0a            \
                \
        width: 4\
0\x0d\x0a             \
                \
       height: 4\
0\x0d\x0a             \
                \
       text: \x22\x22\x0d\
\x0a               \
                \
     anchors.hor\
izontalCenter: p\
arent.horizontal\
Center\x0d\x0a\x0d\x0a      \
                \
              ba\
ckground: Rectan\
gle {\x0d\x0a         \
                \
               r\
adius: parent.ra\
dius\x0d\x0a          \
                \
              co\
lor: processBean\
.pCsvRegThreadRu\
nning ? ( proces\
sBean.pCsvRegThr\
eadPause ? \x22oran\
ge\x22 : \x22green\x22 ) \
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
     id: tCsvCre\
ationRunning\x0d\x0a  \
                \
                \
  text: qsTr(\x22CS\
V CREATION RUN\x22)\
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
 id: itemSpacer\x0d\
\x0a               \
                \
 width: 130\x0d\x0a   \
                \
             hei\
ght: 1\x0d\x0a        \
                \
        Layout.f\
illHeight: false\
\x0d\x0a              \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
                \
          Layout\
.columnSpan: 3\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             Ite\
m {\x0d\x0a           \
                \
     id: itemCsv\
NewEmpty\x0d\x0a      \
                \
          width:\
 130\x0d\x0a          \
                \
      height: 65\
\x0d\x0a              \
                \
  RoundButton {\x0d\
\x0a               \
                \
     id: rbCsvNe\
wEmpty\x0d\x0a        \
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
  color: process\
Bean.pCsvRegThre\
adCsvNewEmpty ? \
\x22blue\x22 : \x22lightG\
ray\x22\x0d\x0a          \
                \
          }\x0d\x0a   \
                \
             }\x0d\x0a\
                \
                \
Text {\x0d\x0a        \
                \
            id: \
tCsvNewEmpty\x0d\x0a  \
                \
                \
  text: qsTr(\x22NE\
W CSV MANUALLY\x22)\
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
         ColumnL\
ayout {\x0d\x0a       \
                \
         id: col\
umnLayout\x0d\x0a     \
                \
           width\
: 100\x0d\x0a         \
                \
       height: 1\
00\x0d\x0a            \
                \
    spacing: 0\x0d\x0a\
\x0d\x0a              \
                \
  CheckBox {\x0d\x0a  \
                \
                \
  id: cbStop\x0d\x0a  \
                \
                \
  text: qsTr(\x22St\
op\x22)\x0d\x0a          \
                \
          paddin\
g: 1\x0d\x0a          \
                \
          onChec\
kedChanged: proc\
essCtrl.changeSt\
opRequestValue(c\
bStop.checked)\x0d\x0a\
                \
                \
}\x0d\x0a\x0d\x0a           \
                \
     CheckBox {\x0d\
\x0a               \
                \
     id: cbPause\
\x0d\x0a              \
                \
      text: qsTr\
(\x22Pause\x22)\x0d\x0a     \
                \
               p\
adding: 1\x0d\x0a     \
                \
               o\
nCheckedChanged:\
 processCtrl.cha\
ngePauseRequestV\
alue(cbPause.che\
cked)\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Item {\x0d\x0a \
                \
               i\
d: itemCleanLoca\
lFolderStatus\x0d\x0a \
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
CleanLocalFolder\
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
RegThreadCleanLo\
calFolderStatus)\
\x0d\x0a              \
                \
      }\x0d\x0a       \
                \
         }\x0d\x0a    \
                \
            Text\
 {\x0d\x0a            \
                \
        id: tCle\
anLocalFolderSta\
tus\x0d\x0a           \
                \
         text: q\
sTr(\x22CLEAN LOCAL\
 FOLDER\x22)\x0d\x0a     \
                \
               a\
nchors.bottom: p\
arent.bottom\x0d\x0a  \
                \
                \
  anchors.bottom\
Margin: 0\x0d\x0a     \
                \
               a\
nchors.horizonta\
lCenter: parent.\
horizontalCenter\
\x0d\x0a              \
                \
  }\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Item {\x0d\x0a      \
                \
          id: it\
emCleanCameraFol\
derStatus\x0d\x0a     \
                \
           width\
: 130\x0d\x0a         \
                \
       height: 6\
5\x0d\x0a             \
                \
   RoundButton {\
\x0d\x0a              \
                \
      id: rbClea\
nCameraFolderSta\
tus\x0d\x0a           \
                \
         width: \
40\x0d\x0a            \
                \
        height: \
40\x0d\x0a            \
                \
        text: \x22\x22\
\x0d\x0a              \
                \
      anchors.ho\
rizontalCenter: \
parent.horizonta\
lCenter\x0d\x0a\x0d\x0a     \
                \
               b\
ackground: Recta\
ngle {\x0d\x0a        \
                \
                \
radius: parent.r\
adius\x0d\x0a         \
                \
               c\
olor: gRegenerat\
ion.getColor(pro\
cessBean.pCsvReg\
ThreadCleanCamer\
aFolderStatus)\x0d\x0a\
                \
                \
    }\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
          Text {\
\x0d\x0a              \
                \
      id: tClean\
CameraFolderStat\
us\x0d\x0a            \
                \
        text: qs\
Tr(\x22CLEAN CAMERA\
 FOLDER\x22)\x0d\x0a     \
                \
               a\
nchors.bottom: p\
arent.bottom\x0d\x0a  \
                \
                \
  anchors.bottom\
Margin: 0\x0d\x0a     \
                \
               a\
nchors.horizonta\
lCenter: parent.\
horizontalCenter\
\x0d\x0a              \
                \
  }\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Item {\x0d\x0a      \
                \
          id: it\
emSpacer2\x0d\x0a     \
                \
           width\
: 130\x0d\x0a         \
                \
       height: 1\
\x0d\x0a              \
                \
  Layout.fillHei\
ght: false\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    Layout.colum\
nSpan: 5\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Item {\x0d\x0a \
                \
               i\
d: itemRenameLas\
erItemsStatus\x0d\x0a \
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
RenameLaserItems\
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
RegThreadRenameL\
aserItemsStatus)\
\x0d\x0a              \
                \
      }\x0d\x0a       \
                \
         }\x0d\x0a    \
                \
            Text\
 {\x0d\x0a            \
                \
        id: tRen\
ameLaserItemsSta\
tus\x0d\x0a           \
                \
         text: q\
sTr(\x22RENAME LASE\
R ITEMS\x22)\x0d\x0a     \
                \
               a\
nchors.bottom: p\
arent.bottom\x0d\x0a  \
                \
                \
  anchors.bottom\
Margin: 0\x0d\x0a     \
                \
               a\
nchors.horizonta\
lCenter: parent.\
horizontalCenter\
\x0d\x0a              \
                \
  }\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Item {\x0d\x0a      \
                \
          id: it\
emDownloadItemsS\
tatus\x0d\x0a         \
                \
       width: 13\
0\x0d\x0a             \
                \
   height: 65\x0d\x0a \
                \
               R\
oundButton {\x0d\x0a  \
                \
                \
  id: rbDownload\
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
.pCsvRegThreadDo\
wnloadItemsStatu\
s)\x0d\x0a            \
                \
        }\x0d\x0a     \
                \
           }\x0d\x0a  \
                \
              Te\
xt {\x0d\x0a          \
                \
          id: tD\
ownloadItemsStat\
us\x0d\x0a            \
                \
        text: qs\
Tr(\x22DOWNLOAD\x22)\x0d\x0a\
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
d: itemCleanLase\
rFolderStatus\x0d\x0a \
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
CleanLaserFolder\
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
RegThreadCleanLa\
serFolderStatus)\
\x0d\x0a              \
                \
      }\x0d\x0a       \
                \
         }\x0d\x0a    \
                \
            Text\
 {\x0d\x0a            \
                \
        id: tCle\
anLaserFolderSta\
tus\x0d\x0a           \
                \
         text: q\
sTr(\x22CLEAN LASER\
 FOLDER\x22)\x0d\x0a     \
                \
               a\
nchors.bottom: p\
arent.bottom\x0d\x0a  \
                \
                \
  anchors.bottom\
Margin: 0\x0d\x0a     \
                \
               a\
nchors.horizonta\
lCenter: parent.\
horizontalCenter\
\x0d\x0a              \
                \
  }\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Item {\x0d\x0a      \
                \
          id: it\
emCsvCreationPro\
cessStatus\x0d\x0a    \
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
       id: rbCsv\
CreationProcessS\
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
egThreadCsvCreat\
ionProcessStatus\
)\x0d\x0a             \
                \
       }\x0d\x0a      \
                \
          }\x0d\x0a   \
                \
             Tex\
t {\x0d\x0a           \
                \
         id: tCs\
vCreationProcess\
Status\x0d\x0a        \
                \
            text\
: qsTr(\x22CREATION\
 CSV\x22)\x0d\x0a        \
                \
            anch\
ors.bottom: pare\
nt.bottom\x0d\x0a     \
                \
               a\
nchors.bottomMar\
gin: 0\x0d\x0a        \
                \
            anch\
ors.horizontalCe\
nter: parent.hor\
izontalCenter\x0d\x0a \
                \
               }\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               I\
tem {\x0d\x0a         \
                \
       id: itemS\
endCsvToLaserSta\
tus\x0d\x0a           \
                \
     width: 130\x0d\
\x0a               \
                \
 height: 65\x0d\x0a   \
                \
             Lay\
out.columnSpan: \
1\x0d\x0a             \
                \
   RoundButton {\
\x0d\x0a              \
                \
      id: rbSend\
CsvToLaserStatus\
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
eadSendCsvToLase\
rStatus)\x0d\x0a      \
                \
              }\x0d\
\x0a               \
                \
 }\x0d\x0a            \
                \
    Text {\x0d\x0a    \
                \
                \
id: tSendCsvToLa\
serStatus\x0d\x0a     \
                \
               t\
ext: qsTr(\x22SEND \
CSV LASER\x22)\x0d\x0a   \
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
itemSendCsvToCam\
eraStatus\x0d\x0a     \
                \
           width\
: 130\x0d\x0a         \
                \
       height: 6\
5\x0d\x0a             \
                \
   RoundButton {\
\x0d\x0a              \
                \
      id: rbSend\
CsvToCameraStatu\
s\x0d\x0a             \
                \
       width: 40\
\x0d\x0a              \
                \
      height: 40\
\x0d\x0a              \
                \
      text: \x22\x22\x0d\x0a\
                \
                \
    anchors.hori\
zontalCenter: pa\
rent.horizontalC\
enter\x0d\x0a\x0d\x0a       \
                \
             bac\
kground: Rectang\
le {\x0d\x0a          \
                \
              ra\
dius: parent.rad\
ius\x0d\x0a           \
                \
             col\
or: gRegeneratio\
n.getColor(proce\
ssBean.pCsvRegTh\
readSendCsvToCam\
eraStatus)\x0d\x0a    \
                \
                \
}\x0d\x0a             \
                \
   }\x0d\x0a          \
                \
      Text {\x0d\x0a  \
                \
                \
  id: tSendCsvTo\
CameraStatus\x0d\x0a  \
                \
                \
  text: qsTr(\x22SE\
ND CSV CAMERA\x22)\x0d\
\x0a               \
                \
     anchors.bot\
tom: parent.bott\
om\x0d\x0a            \
                \
        anchors.\
bottomMargin: 0\x0d\
\x0a               \
                \
     anchors.hor\
izontalCenter: p\
arent.horizontal\
Center\x0d\x0a        \
                \
        }\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\
                \
        }\x0d\x0a     \
               }\
\x0d\x0a\x0d\x0a            \
        GridLayo\
ut {\x0d\x0a          \
              id\
: gFooter\x0d\x0a     \
                \
   width: 100\x0d\x0a \
                \
       height: 1\
00\x0d\x0a\x0d\x0a          \
              It\
em {\x0d\x0a          \
                \
  Layout.fillHei\
ght: false\x0d\x0a    \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
        }\x0d\x0a\x0d\x0a   \
                \
 }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a    \
            }\x0d\x0a \
           }\x0d\x0a\x0d\x0a\
            Item\
 {\x0d\x0a            \
    id: settings\
\x0d\x0a              \
  Layout.fillHei\
ght: true\x0d\x0a     \
           Layou\
t.fillWidth: tru\
e\x0d\x0a\x0d\x0a           \
     GridLayout \
{\x0d\x0a             \
       id: gridL\
ayout\x0d\x0a         \
           layou\
tDirection: Qt.L\
eftToRight\x0d\x0a    \
                \
anchors.right: p\
arent.right\x0d\x0a   \
                \
 anchors.bottom:\
 parent.bottom\x0d\x0a\
                \
    anchors.left\
: parent.left\x0d\x0a \
                \
   anchors.top: \
parent.top\x0d\x0a    \
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
  columnSpacing:\
 50\x0d\x0a           \
         rowSpac\
ing: 50\x0d\x0a       \
             col\
umns: 2\x0d\x0a\x0d\x0a     \
               C\
olumnLayout {\x0d\x0a \
                \
       id: camer\
aSettingsLayout\x0d\
\x0a               \
         Layout.\
fillWidth: true\x0d\
\x0a               \
         GridLay\
out {\x0d\x0a         \
                \
   id: gridLayou\
t2\x0d\x0a            \
                \
Layout.fillHeigh\
t: true\x0d\x0a       \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
         columns\
: 2\x0d\x0a           \
                \
 columnSpacing: \
5\x0d\x0a\x0d\x0a           \
                \
 Text {\x0d\x0a       \
                \
         id: tCa\
meraPath\x0d\x0a      \
                \
          text: \
qsTr(\x22Camera pat\
h\x22)\x0d\x0a           \
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
 tfCameraPath\x0d\x0a \
                \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
                \
       text: set\
tingsBean.pCamer\
aRemotePath\x0d\x0a   \
                \
             onE\
ditingFinished: \
processCtrl.setC\
ameraRemotePath(\
tfCameraPath.tex\
t)\x0d\x0a            \
                \
}\x0d\x0a\x0d\x0a           \
                \
 Button {\x0d\x0a\x0d\x0a   \
                \
             Fil\
eDialog {\x0d\x0a     \
                \
               i\
d: cameraFileDia\
log\x0d\x0a           \
                \
         title: \
qsTr(\x22Choose a f\
older\x22)\x0d\x0a       \
                \
             sel\
ectFolder: true\x0d\
\x0a               \
                \
     onAccepted:\
 processCtrl.set\
CameraRemotePath\
(cameraFileDialo\
g.fileUrl)\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
                \
 id: bCameraFold\
er\x0d\x0a            \
                \
    text: qsTr(\x22\
Change camera fo\
lder\x22)\x0d\x0a        \
                \
        Layout.m\
inimumWidth: 140\
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
cameraFileDialog\
.folder = proces\
sCtrl.getUrlFrom\
NativePath(setti\
ngsBean.pCameraR\
emotePath)\x0d\x0a    \
                \
                \
cameraFileDialog\
.open()\x0d\x0a       \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           Text \
{\x0d\x0a             \
                \
   id: tCameraPo\
llingTimeMs\x0d\x0a   \
                \
             tex\
t: qsTr(\x22Polling\
 time [ms]\x22)\x0d\x0a  \
                \
              La\
yout.minimumWidt\
h: 120\x0d\x0a        \
                \
        font.pix\
elSize: 12\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         TextFie\
ld {\x0d\x0a          \
                \
      id: tfCame\
raPollingTimeMs\x0d\
\x0a               \
                \
 text: settingsB\
ean.pCameraPolli\
ngTimeMs\x0d\x0a      \
                \
          Layout\
.columnSpan: 1\x0d\x0a\
                \
                \
Layout.fillWidth\
: true\x0d\x0a        \
                \
        validato\
r: IntValidator \
{\x0d\x0a             \
                \
       bottom: 1\
00;\x0d\x0a           \
                \
         top: 10\
0000;\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
          onEdit\
ingFinished: set\
tingsBean.pCamer\
aPollingTimeMs =\
 tfCameraPolling\
TimeMs.text\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Item {\
\x0d\x0a              \
                \
  id: element6\x0d\x0a\
                \
                \
width: 0\x0d\x0a      \
                \
          height\
: 0\x0d\x0a           \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          CheckB\
ox {\x0d\x0a          \
                \
      id: cbCame\
raSendCsv\x0d\x0a     \
                \
           text:\
 qsTr(\x22Send CSV \
to camera\x22)\x0d\x0a   \
                \
             che\
cked: settingsBe\
an.pCameraSendCS\
V\x0d\x0a             \
                \
   Layout.alignm\
ent: Qt.AlignRig\
ht | Qt.AlignVCe\
nter\x0d\x0a          \
                \
      leftPaddin\
g: 0\x0d\x0a          \
                \
      onCheckedC\
hanged: settings\
Bean.pCameraSend\
CSV = cbCameraSe\
ndCsv.checked\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Item\
 {\x0d\x0a            \
                \
    id: element4\
\x0d\x0a              \
                \
  Layout.columnS\
pan: 2\x0d\x0a        \
                \
        Layout.f\
illWidth: false\x0d\
\x0a               \
                \
 Layout.fillHeig\
ht: true\x0d\x0a      \
                \
          Layout\
.preferredWidth:\
 0\x0d\x0a            \
                \
    Layout.prefe\
rredHeight: 1\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
\x0d\x0a\x0d\x0a\x0d\x0a          \
              }\x0d\
\x0a\x0d\x0a             \
           GridL\
ayout {\x0d\x0a       \
                \
     id: gridLay\
out3\x0d\x0a          \
                \
  Layout.fillWid\
th: true\x0d\x0a\x0d\x0a    \
                \
        Button {\
\x0d\x0a              \
                \
  id: bCameraSet\
\x0d\x0a              \
                \
  text: qsTr(\x22Se\
t camera configu\
ration\x22)\x0d\x0a      \
                \
          Layout\
.fillWidth: true\
\x0d\x0a              \
                \
  rightPadding: \
15\x0d\x0a            \
                \
    leftPadding:\
 15\x0d\x0a           \
                \
     onClicked: \
settingsCtrl.sav\
eParameters()\x0d\x0a \
                \
           }\x0d\x0a  \
                \
      }\x0d\x0a       \
             }\x0d\x0a\
\x0d\x0a              \
      ColumnLayo\
ut {\x0d\x0a          \
              id\
: laserSettingsL\
ayout\x0d\x0a         \
               L\
ayout.fillWidth:\
 true\x0d\x0a\x0d\x0a       \
                \
 GridLayout {\x0d\x0a \
                \
           id: g\
lLaser\x0d\x0a        \
                \
    Layout.fillH\
eight: true\x0d\x0a   \
                \
         Layout.\
fillWidth: true\x0d\
\x0a               \
             col\
umns: 2\x0d\x0a       \
                \
     columnSpaci\
ng: 5\x0d\x0a\x0d\x0a       \
                \
     Text {\x0d\x0a   \
                \
             id:\
 tLaserIp\x0d\x0a     \
                \
           text:\
 qsTr(\x22Laser IP\x22\
)\x0d\x0a             \
                \
   Layout.minimu\
mWidth: 120\x0d\x0a   \
                \
             Lay\
out.fillWidth: f\
alse\x0d\x0a          \
                \
      font.pixel\
Size: 12\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       TextField\
 {\x0d\x0a            \
                \
    id: tfLaserI\
p\x0d\x0a             \
                \
   text: setting\
sBean.pLaserIp\x0d\x0a\
                \
                \
Layout.columnSpa\
n: 1\x0d\x0a          \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
              pl\
aceholderText: \x22\
Laser IP address\
\x22\x0d\x0a             \
                \
   inputMask: \x220\
00.000.000.000\x22\x0d\
\x0a               \
                \
 onEditingFinish\
ed: settingsBean\
.pLaserIp = text\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tLase\
rPort\x0d\x0a         \
                \
       text: qsT\
r(\x22Laser port\x22)\x0d\
\x0a               \
                \
 Layout.minimumW\
idth: 120\x0d\x0a     \
                \
           font.\
pixelSize: 12\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Text\
Field {\x0d\x0a       \
                \
         id: tfL\
aserPort\x0d\x0a      \
                \
          text: \
\x22%0\x22.arg(setting\
sBean.pLaserPort\
)\x0d\x0a             \
                \
   Layout.column\
Span: 1\x0d\x0a       \
                \
         Layout.\
fillWidth: true\x0d\
\x0a               \
                \
 placeholderText\
: \x22Laser Port\x22\x0d\x0a\
                \
                \
inputMask: \x220000\
0\x22\x0d\x0a            \
                \
    onEditingFin\
ished: settingsB\
ean.pLaserPort =\
 tfLaserPort.tex\
t\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
                \
Text {\x0d\x0a        \
                \
        id: tLas\
erPollingTimeMs\x0d\
\x0a               \
                \
 text: qsTr(\x22Pol\
ling time [ms]\x22)\
\x0d\x0a              \
                \
  Layout.minimum\
Width: 120\x0d\x0a    \
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
LaserPollingTime\
Ms\x0d\x0a            \
                \
    text: settin\
gsBean.pLaserPol\
lingTimeMs\x0d\x0a    \
                \
            Layo\
ut.columnSpan: 1\
\x0d\x0a              \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
                \
          valida\
tor: IntValidato\
r {\x0d\x0a           \
                \
         bottom:\
 100;\x0d\x0a         \
                \
           top: \
100000;\x0d\x0a       \
                \
         }\x0d\x0a    \
                \
            onEd\
itingFinished: s\
ettingsBean.pLas\
erPollingTimeMs \
= tfLaserPolling\
TimeMs.text\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tLaserRemo\
tePath\x0d\x0a        \
                \
        text: qs\
Tr(\x22Laser remote\
 path\x22)\x0d\x0a       \
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
erRemotePath\x0d\x0a  \
                \
              te\
xt: settingsBean\
.pLaserRemotePat\
h\x0d\x0a             \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
           onEdi\
tingFinished: se\
ttingsBean.pLase\
rRemotePath = tf\
LaserRemotePath.\
text\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Item {\x0d\x0a     \
                \
           id: e\
lement3\x0d\x0a       \
                \
         Layout.\
columnSpan: 2\x0d\x0a \
                \
               L\
ayout.preferredH\
eight: 1\x0d\x0a      \
                \
          Layout\
.preferredWidth:\
 0\x0d\x0a            \
                \
    Layout.fillH\
eight: true\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
      }\x0d\x0a\x0d\x0a     \
                \
   GridLayout {\x0d\
\x0a               \
             id:\
 gridLayout1\x0d\x0a  \
                \
          column\
s: 2\x0d\x0a          \
                \
  Layout.fillWid\
th: true\x0d\x0a\x0d\x0a    \
                \
        Button {\
\x0d\x0a              \
                \
  id: bLaserSet\x0d\
\x0a               \
                \
 text: qsTr(\x22Set\
 laser configura\
tion\x22)\x0d\x0a        \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
                \
rightPadding: 15\
\x0d\x0a              \
                \
  leftPadding: 1\
5\x0d\x0a             \
                \
   onClicked: se\
ttingsCtrl.saveP\
arameters()\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
      }\x0d\x0a\x0d\x0a     \
               }\
\x0d\x0a\x0d\x0a            \
        ColumnLa\
yout {\x0d\x0a        \
                \
id: localSetting\
sLayoutL\x0d\x0a      \
                \
  width: 100\x0d\x0a  \
                \
      height: 10\
0\x0d\x0a             \
           Layou\
t.fillHeight: tr\
ue\x0d\x0a            \
            Layo\
ut.columnSpan: 1\
\x0d\x0a\x0d\x0a            \
            Grid\
Layout {\x0d\x0a      \
                \
      id: gridLa\
yout4\x0d\x0a         \
                \
   width: 100\x0d\x0a \
                \
           heigh\
t: 100\x0d\x0a        \
                \
    columns: 2\x0d\x0a\
\x0d\x0a              \
              Te\
xt {\x0d\x0a          \
                \
      id: tRighe\
Scarto\x0d\x0a        \
                \
        text: qs\
Tr(\x22Righe scarto\
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
tfRigheScarto\x0d\x0a \
                \
               t\
ext: settingsBea\
n.pLocalRowMargi\
n\x0d\x0a             \
                \
   validator: In\
tValidator {\x0d\x0a  \
                \
                \
  bottom: 0;\x0d\x0a  \
                \
                \
  top: 20;\x0d\x0a    \
                \
            }\x0d\x0a \
                \
               o\
nEditingFinished\
: settingsBean.p\
LocalRowMargin =\
 tfRigheScarto.t\
ext\x0d\x0a           \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tWaitTimeB\
eforeProcess\x0d\x0a  \
                \
              te\
xt: qsTr(\x22Wait t\
ime before proce\
ss [s]\x22)\x0d\x0a      \
                \
          font.p\
ixelSize: 12\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           TextF\
ield {\x0d\x0a        \
                \
        id: tfWa\
itTimeBeforeProc\
ess\x0d\x0a           \
                \
     text: setti\
ngsBean.pLocalWa\
itTimeBeforeProc\
ess\x0d\x0a           \
                \
     validator: \
IntValidator {\x0d\x0a\
                \
                \
    bottom: 1;\x0d\x0a\
                \
                \
    top: 20;\x0d\x0a  \
                \
              }\x0d\
\x0a               \
                \
 onEditingFinish\
ed: settingsBean\
.pLocalWaitTimeB\
eforeProcess = t\
fWaitTimeBeforeP\
rocess.text\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Text {\x0d\x0a      \
                \
          id: tC\
svFilename\x0d\x0a    \
                \
            text\
: qsTr(\x22Nome fil\
e CSV\x22)\x0d\x0a       \
                \
         Layout.\
minimumWidth: 12\
0\x0d\x0a             \
                \
   font.pixelSiz\
e: 12\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    TextField {\x0d\
\x0a               \
                \
 id: tfCsvFilena\
me\x0d\x0a            \
                \
    text: settin\
gsBean.pLocalCsv\
Filename\x0d\x0a      \
                \
          Layout\
.fillWidth: true\
\x0d\x0a              \
                \
  onEditingFinis\
hed: settingsBea\
n.pLocalCsvFilen\
ame = tfCsvFilen\
ame.text\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Text {\x0d\x0a \
                \
               i\
d: tLaserErrorFi\
lename\x0d\x0a        \
                \
        text: qs\
Tr(\x22Nome file er\
rore laser\x22)\x0d\x0a  \
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
tfLaserErrorFile\
name\x0d\x0a          \
                \
      text: sett\
ingsBean.pLocalL\
aserErrorFilenam\
e\x0d\x0a             \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
           onEdi\
tingFinished: se\
ttingsBean.pLoca\
lLaserErrorFilen\
ame = tfLaserErr\
orFilename.text\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Te\
xt {\x0d\x0a          \
                \
      id: tLaser\
LogFilename\x0d\x0a   \
                \
             tex\
t: qsTr(\x22Nome fi\
le log\x22)\x0d\x0a      \
                \
          font.p\
ixelSize: 12\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           TextF\
ield {\x0d\x0a        \
                \
        id: tfLa\
serLogFilename\x0d\x0a\
                \
                \
text: settingsBe\
an.pLocalLaserLo\
gFilename\x0d\x0a     \
                \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
                \
   onEditingFini\
shed: settingsBe\
an.pLocalLaserLo\
gFilename = tfLa\
serLogFilename.t\
ext\x0d\x0a           \
                \
 }\x0d\x0a\x0d\x0a          \
                \
  Item {\x0d\x0a      \
                \
          id: el\
ement5\x0d\x0a        \
                \
        width: 2\
00\x0d\x0a            \
                \
    height: 200\x0d\
\x0a               \
                \
 Layout.fillHeig\
ht: true\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
   }\x0d\x0a          \
          }\x0d\x0a\x0d\x0a \
                \
   ColumnLayout \
{\x0d\x0a             \
           id: l\
ocalSettingsLayo\
utR\x0d\x0a           \
             wid\
th: 100\x0d\x0a       \
                \
 height: 100\x0d\x0a  \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
      Layout.col\
umnSpan: 1\x0d\x0a\x0d\x0a  \
                \
      GridLayout\
 {\x0d\x0a            \
                \
id: gridLayout5\x0d\
\x0a               \
             wid\
th: 100\x0d\x0a       \
                \
     height: 100\
\x0d\x0a              \
              co\
lumns: 2\x0d\x0a      \
                \
      Layout.col\
umnSpan: 1\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tLoadingPa\
th\x0d\x0a            \
                \
    text: qsTr(\x22\
Loading path\x22)\x0d\x0a\
                \
                \
font.pixelSize: \
12\x0d\x0a            \
                \
}\x0d\x0a\x0d\x0a           \
                \
 TextField {\x0d\x0a  \
                \
              id\
: tfLoadingPath\x0d\
\x0a               \
                \
 text: settingsB\
ean.pLocalLoadin\
gPath\x0d\x0a         \
                \
       Layout.fi\
llWidth: true\x0d\x0a \
                \
               o\
nEditingFinished\
: processCtrl.se\
tLocalLoadingPat\
h(tfLoadingPath.\
text)\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    Button {\x0d\x0a\x0d\x0a\
                \
                \
FileDialog {\x0d\x0a  \
                \
                \
  id: localLoadi\
ngPathFileDialog\
2\x0d\x0a             \
                \
       title: qs\
Tr(\x22Choose a fol\
der\x22)\x0d\x0a         \
                \
           selec\
tFolder: true\x0d\x0a \
                \
                \
   onAccepted: p\
rocessCtrl.setLo\
calLoadingPath(l\
ocalLoadingPathF\
ileDialog2.fileU\
rl)\x0d\x0a           \
                \
     }\x0d\x0a\x0d\x0a      \
                \
          id: bL\
oadingPath\x0d\x0a    \
                \
            text\
: qsTr(\x22Change l\
oading path\x22)\x0d\x0a \
                \
               r\
ightPadding: 15\x0d\
\x0a               \
                \
 leftPadding: 15\
\x0d\x0a              \
                \
  Layout.alignme\
nt: Qt.AlignRigh\
t | Qt.AlignVCen\
ter\x0d\x0a           \
                \
     Layout.colu\
mnSpan: 2\x0d\x0a     \
                \
           onCli\
cked: {\x0d\x0a       \
                \
             loc\
alLoadingPathFil\
eDialog2.folder \
= processCtrl.ge\
tUrlFromNativePa\
th(settingsBean.\
pLocalLoadingPat\
h)\x0d\x0a            \
                \
        localLoa\
dingPathFileDial\
og2.open()\x0d\x0a    \
                \
            }\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Text\
 {\x0d\x0a            \
                \
    id: tDownloa\
dPath\x0d\x0a         \
                \
       text: qsT\
r(\x22Downloading p\
ath\x22)\x0d\x0a         \
                \
       font.pixe\
lSize: 12\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        TextFiel\
d {\x0d\x0a           \
                \
     id: tfDownl\
oadPath\x0d\x0a       \
                \
         text: s\
ettingsBean.pLoc\
alDownloadingPat\
h\x0d\x0a             \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
           onEdi\
tingFinished: se\
ttingsBean.pLoca\
lDownloadingPath\
 = tfDownloadPat\
h.text\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     Button {\x0d\x0a\x0d\
\x0a               \
                \
 FileDialog {\x0d\x0a \
                \
                \
   id: localDown\
loadingPathFileD\
ialog\x0d\x0a         \
                \
           title\
: qsTr(\x22Choose a\
 folder\x22)\x0d\x0a     \
                \
               s\
electFolder: tru\
e\x0d\x0a             \
                \
       onAccepte\
d: processCtrl.s\
etLocalDownloadi\
ngPath(localDown\
loadingPathFileD\
ialog.fileUrl)\x0d\x0a\
                \
                \
}\x0d\x0a\x0d\x0a           \
                \
     id: bDownlo\
adPath\x0d\x0a        \
                \
        text: qs\
Tr(\x22Change downl\
oading path\x22)\x0d\x0a \
                \
               r\
ightPadding: 15\x0d\
\x0a               \
                \
 leftPadding: 15\
\x0d\x0a              \
                \
  Layout.columnS\
pan: 2\x0d\x0a        \
                \
        Layout.a\
lignment: Qt.Ali\
gnRight | Qt.Ali\
gnVCenter\x0d\x0a     \
                \
           onCli\
cked: {\x0d\x0a       \
                \
             loc\
alDownloadingPat\
hFileDialog.fold\
er = processCtrl\
.getUrlFromNativ\
ePath(settingsBe\
an.pLocalDownloa\
dingPath)\x0d\x0a     \
                \
               l\
ocalDownloadingP\
athFileDialog.op\
en()\x0d\x0a          \
                \
      }\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      Button {\x0d\x0a\
                \
                \
id: bLocalSet\x0d\x0a \
                \
               t\
ext: qsTr(\x22Set l\
ocal configurati\
on\x22)\x0d\x0a          \
                \
      Layout.col\
umnSpan: 2\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    onClicked: s\
ettingsCtrl.save\
Parameters()\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           Item \
{\x0d\x0a             \
                \
   id: element2\x0d\
\x0a               \
                \
 width: 200\x0d\x0a   \
                \
             hei\
ght: 200\x0d\x0a      \
                \
          Layout\
.fillHeight: tru\
e\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a            \
            }\x0d\x0a \
                \
   }\x0d\x0a\x0d\x0a        \
            Item\
 {\x0d\x0a            \
            id: \
spacer2\x0d\x0a       \
                \
 width: 0\x0d\x0a     \
                \
   height: 0\x0d\x0a  \
                \
      Layout.fil\
lHeight: true\x0d\x0a \
                \
   }\x0d\x0a\x0d\x0a        \
        }\x0d\x0a\x0d\x0a   \
         }\x0d\x0a\x0d\x0a  \
      }\x0d\x0a\x0d\x0a\x0d\x0a   \
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
