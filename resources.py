# -*- coding: utf-8 -*-

# Resource object code
#
# Created: mer ott 23 10:13:31 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.1)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\xdb\xff\
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
68\x0d\x0a//    flags:\
 Qt.CustomizeWin\
dowHint | Qt.Win\
dow\x0d\x0a\x0d\x0a    Dialo\
g {\x0d\x0a        id:\
 operationDialog\
\x0d\x0a        standa\
rdButtons: Dialo\
g.Ok\x0d\x0a        wi\
dth: 200\x0d\x0a      \
  height: 80\x0d\x0a\x0d\x0a\
        Text {\x0d\x0a\
            id: \
operationDialogT\
ext\x0d\x0a           \
 anchors.centerI\
n: parent\x0d\x0a     \
       text: \x22\x22\x0d\
\x0a        }\x0d\x0a\x0d\x0a  \
  }\x0d\x0a\x0d\x0a    // de\
finizione segnal\
i\x0d\x0a    Connectio\
ns {\x0d\x0a        ta\
rget: mainWindow\
\x0d\x0a        onClos\
ing: {\x0d\x0a        \
    processCtrl.\
closingApplicati\
onSignal()\x0d\x0a    \
    }\x0d\x0a    }\x0d\x0a\x0d\x0a\
    Connections \
{\x0d\x0a        targe\
t: processCtrl\x0d\x0a\
        onShowDi\
alogSignal: {\x0d\x0a \
           opera\
tionDialogText.t\
ext = message\x0d\x0a \
           opera\
tionDialog.visib\
le = true\x0d\x0a     \
   }\x0d\x0a    }\x0d\x0a\x0d\x0a \
   Component.onC\
ompleted: {\x0d\x0a   \
     settingsCtr\
l.initBean()\x0d\x0a  \
      processCtr\
l.initBean()\x0d\x0a  \
  }\x0d\x0a\x0d\x0a    // de\
finizione oggett\
i C++\x0d\x0a    QMLSe\
ttingsBean {\x0d\x0a  \
      id: settin\
gsBean\x0d\x0a    }\x0d\x0a\x0d\
\x0a    QMLProcessB\
ean {\x0d\x0a        i\
d: processBean\x0d\x0a\
        //      \
  onLaserFolderI\
temsChanged: lvC\
ameraFolder.forc\
eLayout()\x0d\x0a     \
   //        onL\
aserFolderItemsC\
hanged: mainWind\
ow.width = (main\
Window.width == \
800 ? 640 : 800)\
\x0d\x0a    }\x0d\x0a\x0d\x0a    Q\
MLSettingsContro\
ller {\x0d\x0a        \
id: settingsCtrl\
\x0d\x0a        pSetti\
ngsBean: setting\
sBean\x0d\x0a    }\x0d\x0a\x0d\x0a\
    QMLProcessCo\
ntroller {\x0d\x0a    \
    id: processC\
trl\x0d\x0a        pPr\
ocessBean: proce\
ssBean\x0d\x0a        \
pSettingsBean: s\
ettingsBean\x0d\x0a   \
 }\x0d\x0a\x0d\x0a    minimu\
mWidth: 1024\x0d\x0a  \
  minimumHeight:\
 768\x0d\x0a    visibl\
e: true\x0d\x0a\x0d\x0a    G\
ridLayout {\x0d\x0a   \
     id: glMain\x0d\
\x0a        anchors\
.fill: parent\x0d\x0a \
       rows: 2\x0d\x0a\
        columns:\
 1\x0d\x0a\x0d\x0a        Ta\
bBar {\x0d\x0a        \
    id: tabBar\x0d\x0a\
            widt\
h: parent.width\x0d\
\x0a            Lay\
out.fillWidth: t\
rue\x0d\x0a           \
 currentIndex: 0\
\x0d\x0a            Ta\
bButton {\x0d\x0a     \
           text:\
 qsTr(\x22Process\x22)\
\x0d\x0a            }\x0d\
\x0a            Tab\
Button {\x0d\x0a      \
          text: \
qsTr(\x22Settings\x22)\
\x0d\x0a            }\x0d\
\x0a            Com\
ponent.onComplet\
ed: tabBar.curre\
ntIndex = 0\x0d\x0a\x0d\x0a \
       }\x0d\x0a\x0d\x0a    \
    StackLayout \
{\x0d\x0a\x0d\x0a           \
 width: parent.w\
idth\x0d\x0a          \
  Layout.fillHei\
ght: true\x0d\x0a     \
       currentIn\
dex: tabBar.curr\
entIndex\x0d\x0a      \
      id: stackL\
ayout\x0d\x0a         \
   Layout.fillWi\
dth: true\x0d\x0a\x0d\x0a   \
         Item {\x0d\
\x0a\x0d\x0a             \
   id: processIt\
em\x0d\x0a\x0d\x0a          \
      GridLayout\
 {\x0d\x0a            \
        id: gMai\
n\x0d\x0a             \
       anchors.r\
ightMargin: 10\x0d\x0a\
                \
    anchors.left\
Margin: 10\x0d\x0a    \
                \
anchors.bottomMa\
rgin: 10\x0d\x0a      \
              an\
chors.topMargin:\
 10\x0d\x0a           \
         anchors\
.fill: parent\x0d\x0a \
                \
   clip: true\x0d\x0a \
                \
   rows: 3\x0d\x0a    \
                \
columns: 1\x0d\x0a\x0d\x0a  \
                \
  GridLayout {\x0d\x0a\
                \
        id: gBod\
y\x0d\x0a             \
           width\
: 100\x0d\x0a         \
               h\
eight: 100\x0d\x0a    \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
    rows: 2\x0d\x0a   \
                \
     columns: 3\x0d\
\x0a\x0d\x0a             \
           TextF\
ield {\x0d\x0a        \
                \
    id: tfFolder\
Path\x0d\x0a          \
                \
  text: settings\
Bean.pLocalLoadi\
ngPath\x0d\x0a        \
                \
    Layout.colum\
nSpan: 2\x0d\x0a      \
                \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
          onEdit\
ingFinished: pro\
cessCtrl.setLoca\
lLoadingPath(tfF\
olderPath.text)\x0d\
\x0a               \
         }\x0d\x0a\x0d\x0a  \
                \
      Button {\x0d\x0a\
\x0d\x0a              \
              Fi\
leDialog {\x0d\x0a    \
                \
            id: \
localLoadingPath\
FileDialog\x0d\x0a    \
                \
            titl\
e: qsTr(\x22Choose \
a folder\x22)\x0d\x0a    \
                \
            sele\
ctFolder: true\x0d\x0a\
                \
                \
onAccepted: proc\
essCtrl.setLocal\
LoadingPath(loca\
lLoadingPathFile\
Dialog.fileUrl)\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              id\
: bChangeFolder\x0d\
\x0a               \
             wid\
th: 120\x0d\x0a       \
                \
     height: 40\x0d\
\x0a               \
             tex\
t: qsTr(\x22Change \
local folder\x22)\x0d\x0a\
                \
            Layo\
ut.minimumWidth:\
 140\x0d\x0a          \
                \
  rightPadding: \
15\x0d\x0a            \
                \
leftPadding: 15\x0d\
\x0a               \
             onC\
licked: {\x0d\x0a     \
                \
           local\
LoadingPathFileD\
ialog.folder = p\
rocessCtrl.getUr\
lFromNativePath(\
settingsBean.pLo\
calLoadingPath)\x0d\
\x0a               \
                \
 localLoadingPat\
hFileDialog.open\
()\x0d\x0a            \
                \
}\x0d\x0a             \
           }\x0d\x0a\x0d\x0a\
                \
        TextFiel\
d {\x0d\x0a           \
                \
 id: tfCsvFilena\
meRO\x0d\x0a          \
                \
  text: settings\
Bean.pLocalCsvFi\
lename\x0d\x0a        \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
        readOnly\
: true\x0d\x0a        \
                \
}\x0d\x0a\x0d\x0a           \
             But\
ton {\x0d\x0a         \
                \
   id: bSendToDe\
vices\x0d\x0a         \
                \
   width: 120\x0d\x0a \
                \
           text:\
 qsTr(\x22Send CSV \
to devices\x22)\x0d\x0a  \
                \
          Layout\
.minimumWidth: 1\
40\x0d\x0a            \
                \
rightPadding: 15\
\x0d\x0a              \
              le\
ftPadding: 15\x0d\x0a \
                \
           onCli\
cked: processCtr\
l.sendCsvFileToD\
evices()\x0d\x0a      \
                \
  }\x0d\x0a\x0d\x0a         \
               B\
utton {\x0d\x0a       \
                \
     id: bRemove\
FromDevices\x0d\x0a   \
                \
         width: \
120\x0d\x0a           \
                \
 text: qsTr(\x22Rem\
ove CSV devices\x22\
)\x0d\x0a             \
               L\
ayout.minimumWid\
th: 140\x0d\x0a       \
                \
     onClicked: \
processCtrl.remo\
veCsvFileFromDev\
ices()\x0d\x0a        \
                \
}\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a       \
             }\x0d\x0a\
\x0d\x0a              \
      RowLayout \
{\x0d\x0a             \
           id: r\
owLayout\x0d\x0a      \
                \
  width: 100\x0d\x0a  \
                \
      height: 45\
0\x0d\x0a             \
           scale\
: 1\x0d\x0a           \
             Lay\
out.fillHeight: \
false\x0d\x0a         \
               v\
isible: true\x0d\x0a  \
                \
      Layout.fil\
lWidth: true\x0d\x0a\x0d\x0a\
                \
        GridLayo\
ut {\x0d\x0a          \
                \
  id: gLaserView\
\x0d\x0a              \
              co\
lumnSpacing: 10\x0d\
\x0a               \
             row\
Spacing: 10\x0d\x0a   \
                \
         Layout.\
columnSpan: 1\x0d\x0a \
                \
           clip:\
 false\x0d\x0a        \
                \
    Layout.rowSp\
an: 1\x0d\x0a         \
                \
   rows: 1\x0d\x0a    \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
            Layo\
ut.fillHeight: t\
rue\x0d\x0a           \
                \
 columns: 3\x0d\x0a\x0d\x0a \
                \
           Text \
{\x0d\x0a             \
                \
   id: tLaser\x0d\x0a \
                \
               t\
ext: qsTr(\x22Laser\
 Folder\x22)\x0d\x0a     \
                \
           Layou\
t.columnSpan: 3\x0d\
\x0a               \
                \
 Layout.preferre\
dWidth: 100\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
     font.pixelS\
ize: 12\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      Text {\x0d\x0a  \
                \
              id\
: tLaserWatcher\x0d\
\x0a               \
                \
 text: qsTr(\x22Wat\
cher\x22)\x0d\x0a        \
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
rWatcher\x0d\x0a      \
                \
          width:\
 30\x0d\x0a           \
                \
     height: 30\x0d\
\x0a               \
                \
 text: \x22\x22\x0d\x0a     \
                \
           Layou\
t.alignment: Qt.\
AlignRight | Qt.\
AlignVCenter\x0d\x0a  \
                \
              La\
yout.preferredHe\
ight: 30\x0d\x0a      \
                \
          Layout\
.preferredWidth:\
 30\x0d\x0a           \
                \
     background:\
 Rectangle {\x0d\x0a  \
                \
                \
  id: rbLaserWat\
cherRect\x0d\x0a      \
                \
              ra\
dius: rbLaserWat\
cher.radius\x0d\x0a   \
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
onLaserWatcherRu\
nningChanged: rb\
LaserWatcher.upd\
ateButton(proces\
sBean.pLaserWatc\
herRunning)\x0d\x0a   \
                \
             }\x0d\x0a\
\x0d\x0a              \
                \
  function updat\
eButton(isRunnin\
g) {\x0d\x0a          \
                \
          if (is\
Running)\x0d\x0a      \
                \
                \
  rbLaserWatcher\
Rect.color = \x22gr\
een\x22\x0d\x0a          \
                \
          else\x0d\x0a\
                \
                \
        rbLaserW\
atcherRect.color\
 = \x22red\x22\x0d\x0a      \
                \
          }\x0d\x0a\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Text\
 {\x0d\x0a            \
                \
    id: tLaserCo\
nnection\x0d\x0a      \
                \
          text: \
qsTr(\x22Connection\
\x22)\x0d\x0a            \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
            Layo\
ut.columnSpan: 2\
\x0d\x0a              \
                \
  font.pixelSize\
: 12\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   RoundButton {\
\x0d\x0a              \
                \
  id: rbLaserCon\
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
.preferredHeight\
: 30\x0d\x0a          \
                \
      Layout.pre\
ferredWidth: 30\x0d\
\x0a               \
                \
 Layout.alignmen\
t: Qt.AlignRight\
 | Qt.AlignVCent\
er\x0d\x0a\x0d\x0a          \
                \
      background\
: Rectangle {\x0d\x0a \
                \
                \
   id: rbLaserCo\
nnectionRect\x0d\x0a  \
                \
                \
  radius: rbLase\
rConnection.radi\
us\x0d\x0a            \
                \
        color: \x22\
red\x22\x0d\x0a          \
                \
      }\x0d\x0a\x0d\x0a     \
                \
           Conne\
ctions {\x0d\x0a      \
                \
              ta\
rget: processBea\
n\x0d\x0a             \
                \
       onLaserCo\
nnectionUpChange\
d: rbLaserConnec\
tion.updateButto\
n(processBean.pL\
aserConnectionUp\
)\x0d\x0a             \
                \
   }\x0d\x0a\x0d\x0a        \
                \
        function\
 updateButton(is\
Connected) {\x0d\x0a  \
                \
                \
  if (isConnecte\
d)\x0d\x0a            \
                \
            rbLa\
serConnectionRec\
t.color = \x22green\
\x22\x0d\x0a             \
                \
       else\x0d\x0a   \
                \
                \
     rbLaserConn\
ectionRect.color\
 = \x22red\x22\x0d\x0a      \
                \
          }\x0d\x0a\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            List\
View {\x0d\x0a        \
                \
        id: lvLa\
serFolder\x0d\x0a     \
                \
           x: 0\x0d\
\x0a               \
                \
 y: 0\x0d\x0a         \
                \
       Layout.mi\
nimumHeight: 180\
\x0d\x0a              \
                \
  clip: true\x0d\x0a  \
                \
              La\
yout.fillHeight:\
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
ean.pLaserFolder\
Items\x0d\x0a         \
                \
       opacity: \
processBean.pLas\
erConnectionUp ?\
 1.0 : 0.4\x0d\x0a    \
                \
            enab\
led: processBean\
.pLaserConnectio\
nUp\x0d\x0a\x0d\x0a         \
                \
       delegate:\
 Item {\x0d\x0a       \
                \
             id:\
 lvLaserFolderIt\
em\x0d\x0a            \
                \
        x: 5\x0d\x0a  \
                \
                \
  width: parent.\
width\x0d\x0a         \
                \
           heigh\
t: 40\x0d\x0a\x0d\x0a       \
                \
             Row\
 {\x0d\x0a            \
                \
            id: \
lvLaserFolderIte\
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
 lvLaserFolderIt\
emText\x0d\x0a        \
                \
                \
    parent: lvLa\
serFolderItem\x0d\x0a \
                \
                \
           text:\
 modelData\x0d\x0a    \
                \
                \
        font.bol\
d: true\x0d\x0a       \
                \
                \
     anchors.ver\
ticalCenter: par\
ent.verticalCent\
er\x0d\x0a\x0d\x0a          \
                \
                \
  Rectangle {\x0d\x0a \
                \
                \
               p\
arent: lvLaserFo\
lderItem\x0d\x0a      \
                \
                \
          width:\
 parent.width\x0d\x0a \
                \
                \
               h\
eight: parent.he\
ight\x0d\x0a          \
                \
                \
      anchors.to\
p: parent.top\x0d\x0a \
                \
                \
               c\
olor: \x22#112233FF\
\x22\x0d\x0a             \
                \
               }\
\x0d\x0a              \
                \
          }\x0d\x0a   \
                \
                \
 }\x0d\x0a            \
                \
    }\x0d\x0a\x0d\x0a       \
                \
         ScrollB\
ar.vertical: Scr\
ollBar {\x0d\x0a      \
                \
              pa\
rent: lvLaserFol\
der\x0d\x0a           \
                \
         anchors\
.top: lvLaserFol\
der.top\x0d\x0a       \
                \
             anc\
hors.bottom: lvL\
aserFolder.botto\
m\x0d\x0a             \
                \
       interacti\
ve: true\x0d\x0a      \
                \
              po\
licy: \x22AlwaysOn\x22\
\x0d\x0a              \
                \
      clip: true\
\x0d\x0a              \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    Item {\x0d\x0a    \
                \
            id: \
element\x0d\x0a       \
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
visible: true\x0d\x0a \
                \
           }\x0d\x0a\x0d\x0a\
                \
            Butt\
on {\x0d\x0a          \
                \
      id: bStart\
LaserWatcher\x0d\x0a  \
                \
              te\
xt: qsTr(\x22Start\x22\
)\x0d\x0a             \
                \
   enabled: !pro\
cessBean.pLaserW\
atcherRunning\x0d\x0a \
                \
               o\
nClicked: proces\
sCtrl.startLaser\
Watcher()\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        Button {\
\x0d\x0a              \
                \
  id: bStopLaser\
Watcher\x0d\x0a       \
                \
         text: q\
sTr(\x22Stop\x22)\x0d\x0a   \
                \
             ena\
bled: processBea\
n.pLaserWatcherR\
unning\x0d\x0a        \
                \
        onClicke\
d: processCtrl.s\
topLaserWatcher(\
)\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a    \
                \
    }\x0d\x0a\x0d\x0a       \
                \
 ToolSeparator {\
\x0d\x0a              \
              id\
: toolSeparator\x0d\
\x0a               \
             top\
Padding: 2\x0d\x0a    \
                \
        Layout.f\
illHeight: true\x0d\
\x0a               \
             Lay\
out.rowSpan: 1\x0d\x0a\
                \
            Layo\
ut.columnSpan: 1\
\x0d\x0a              \
              pa\
dding: 10\x0d\x0a     \
                \
   }\x0d\x0a\x0d\x0a        \
                \
GridLayout {\x0d\x0a  \
                \
          id: gC\
ameraView\x0d\x0a     \
                \
       columnSpa\
cing: 10\x0d\x0a      \
                \
      rowSpacing\
: 10\x0d\x0a          \
                \
  Layout.fillHei\
ght: true\x0d\x0a     \
                \
       rows: 1\x0d\x0a\
                \
            colu\
mns: 3\x0d\x0a\x0d\x0a      \
                \
      Text {\x0d\x0a  \
                \
              id\
: tCamera\x0d\x0a     \
                \
           text:\
 qsTr(\x22Camera Fo\
lder\x22)\x0d\x0a        \
                \
        Layout.c\
olumnSpan: 3\x0d\x0a  \
                \
              La\
yout.preferredWi\
dth: 100\x0d\x0a      \
                \
          Layout\
.fillWidth: true\
\x0d\x0a              \
                \
  font.pixelSize\
: 12\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Text {\x0d\x0a     \
                \
           id: t\
CameraWatcher\x0d\x0a \
                \
               t\
ext: qsTr(\x22Watch\
er\x22)\x0d\x0a          \
                \
      Layout.col\
umnSpan: 2\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    font.pixelSi\
ze: 12\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     RoundButton\
 {\x0d\x0a            \
                \
    id: rbCamera\
Watcher\x0d\x0a       \
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
   id: rbCameraW\
atcherRect\x0d\x0a    \
                \
                \
radius: rbLaserC\
onnection.radius\
\x0d\x0a              \
                \
      color: \x22re\
d\x22\x0d\x0a            \
                \
    }\x0d\x0a\x0d\x0a       \
                \
         Connect\
ions {\x0d\x0a        \
                \
            targ\
et: processBean\x0d\
\x0a               \
                \
     onCameraWat\
cherRunningChang\
ed: rbCameraWatc\
her.updateButton\
(processBean.pCa\
meraWatcherRunni\
ng)\x0d\x0a           \
                \
     }\x0d\x0a\x0d\x0a      \
                \
          functi\
on updateButton(\
isRunning) {\x0d\x0a  \
                \
                \
  if (isRunning)\
\x0d\x0a              \
                \
          rbCame\
raWatcherRect.co\
lor = \x22green\x22\x0d\x0a \
                \
                \
   else\x0d\x0a       \
                \
                \
 rbCameraWatcher\
Rect.color = \x22re\
d\x22\x0d\x0a            \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      Text {\x0d\x0a  \
                \
              id\
: tCameraConnect\
ion\x0d\x0a           \
                \
     text: qsTr(\
\x22Connection\x22)\x0d\x0a \
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
 rbCameraConnect\
ion\x0d\x0a           \
                \
     width: 30\x0d\x0a\
                \
                \
height: 30\x0d\x0a    \
                \
            text\
: \x22\x22\x0d\x0a          \
                \
      Layout.ali\
gnment: Qt.Align\
Right | Qt.Align\
VCenter\x0d\x0a       \
                \
         Layout.\
preferredHeight:\
 30\x0d\x0a           \
                \
     Layout.pref\
erredWidth: 30\x0d\x0a\
\x0d\x0a              \
                \
  background: Re\
ctangle {\x0d\x0a     \
                \
               i\
d: rbCameraConne\
ctionRect\x0d\x0a     \
                \
               r\
adius: rbLaserCo\
nnection.radius\x0d\
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
    onCameraConn\
ectionUpChanged:\
 rbCameraConnect\
ion.updateButton\
(processBean.pCa\
meraConnectionUp\
)\x0d\x0a             \
                \
   }\x0d\x0a\x0d\x0a        \
                \
        function\
 updateButton(is\
Connected) {\x0d\x0a  \
                \
                \
  if (isConnecte\
d)\x0d\x0a            \
                \
            rbCa\
meraConnectionRe\
ct.color = \x22gree\
n\x22\x0d\x0a            \
                \
        else\x0d\x0a  \
                \
                \
      rbCameraCo\
nnectionRect.col\
or = \x22red\x22\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
             }\x0d\x0a\
\x0d\x0a              \
              Li\
stView {\x0d\x0a      \
                \
          id: lv\
CameraFolder\x0d\x0a  \
                \
              La\
yout.minimumHeig\
ht: 180\x0d\x0a       \
                \
         Layout.\
fillHeight: true\
\x0d\x0a              \
                \
  clip: true\x0d\x0a  \
                \
              La\
yout.columnSpan:\
 3\x0d\x0a            \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
            spac\
ing: 4\x0d\x0a        \
                \
        model: p\
rocessBean.pCame\
raFolderItems\x0d\x0a \
                \
               o\
pacity: processB\
ean.pCameraConne\
ctionUp ? 1.0 : \
0.4\x0d\x0a           \
                \
     enabled: pr\
ocessBean.pCamer\
aConnectionUp\x0d\x0a\x0d\
\x0a               \
                \
 delegate: Item \
{\x0d\x0a             \
                \
       id: lvCam\
eraFolderItem\x0d\x0a \
                \
                \
   x: 5\x0d\x0a       \
                \
             wid\
th: parent.width\
\x0d\x0a              \
                \
      height: 40\
\x0d\x0a\x0d\x0a            \
                \
        Row {\x0d\x0a \
                \
                \
       id: lvCam\
eraFolderItemRow\
\x0d\x0a\x0d\x0a            \
                \
            Text\
 {\x0d\x0a            \
                \
                \
padding: 10\x0d\x0a   \
                \
                \
         id: lvC\
ameraFolderItemT\
ext\x0d\x0a           \
                \
                \
 parent: lvCamer\
aFolderItem\x0d\x0a   \
                \
                \
         text: m\
odelData\x0d\x0a      \
                \
                \
      font.bold:\
 true\x0d\x0a         \
                \
                \
   anchors.verti\
calCenter: paren\
t.verticalCenter\
\x0d\x0a\x0d\x0a            \
                \
                \
Rectangle {\x0d\x0a   \
                \
                \
             par\
ent: lvCameraFol\
derItem\x0d\x0a       \
                \
                \
         width: \
parent.width\x0d\x0a  \
                \
                \
              he\
ight: parent.hei\
ght\x0d\x0a           \
                \
                \
     anchors.top\
: parent.top\x0d\x0a  \
                \
                \
              co\
lor: \x22#112233FF\x22\
\x0d\x0a              \
                \
              }\x0d\
\x0a               \
                \
         }\x0d\x0a    \
                \
                \
    spacing: 10\x0d\
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
  anchors.top: l\
vCameraFolder.to\
p\x0d\x0a             \
                \
       anchors.b\
ottom: lvCameraF\
older.bottom\x0d\x0a  \
                \
                \
  interactive: t\
rue\x0d\x0a           \
                \
         policy:\
 \x22AlwaysOn\x22\x0d\x0a   \
                \
                \
 clip: true\x0d\x0a   \
                \
             }\x0d\x0a\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               I\
tem {\x0d\x0a         \
                \
       id: eleme\
nt1\x0d\x0a           \
                \
     width: 0\x0d\x0a \
                \
               h\
eight: 0\x0d\x0a      \
                \
          Layout\
.fillHeight: fal\
se\x0d\x0a            \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
            Layo\
ut.columnSpan: 1\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               B\
utton {\x0d\x0a       \
                \
         id: bSt\
arCameraWatcher\x0d\
\x0a               \
                \
 text: qsTr(\x22Sta\
rt\x22)\x0d\x0a          \
                \
      enabled: !\
processBean.pCam\
eraWatcherRunnin\
g\x0d\x0a             \
                \
   onClicked: pr\
ocessCtrl.startC\
ameraWatcher()\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             But\
ton {\x0d\x0a         \
                \
       id: bStop\
CameraWatcher\x0d\x0a \
                \
               t\
ext: qsTr(\x22Stop\x22\
)\x0d\x0a             \
                \
   enabled: proc\
essBean.pCameraW\
atcherRunning\x0d\x0a \
                \
               o\
nClicked: proces\
sCtrl.stopCamera\
Watcher()\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\
\x0d\x0a\x0d\x0a            \
            }\x0d\x0a\x0d\
\x0a               \
     }\x0d\x0a\x0d\x0a      \
              Fr\
ame {\x0d\x0a         \
               i\
d: fRegeneration\
\x0d\x0a              \
          width:\
 200\x0d\x0a          \
              he\
ight: 200\x0d\x0a     \
                \
   opacity: 1\x0d\x0a \
                \
       padding: \
0\x0d\x0a             \
           leftP\
adding: 0\x0d\x0a     \
                \
   rightPadding:\
 0\x0d\x0a            \
            bott\
omPadding: 0\x0d\x0a  \
                \
      topPadding\
: 0\x0d\x0a           \
             Lay\
out.fillHeight: \
true\x0d\x0a          \
              La\
yout.fillWidth: \
true\x0d\x0a\x0d\x0a        \
                \
GridLayout {\x0d\x0a  \
                \
          id: gR\
egeneration\x0d\x0a   \
                \
         columns\
: 7\x0d\x0a           \
                \
 rows: 2\x0d\x0a      \
                \
      visible: t\
rue\x0d\x0a           \
                \
 anchors.fill: p\
arent\x0d\x0a         \
                \
   Layout.fillHe\
ight: true\x0d\x0a    \
                \
        Layout.f\
illWidth: true\x0d\x0a\
\x0d\x0a              \
              fu\
nction getColor(\
status) {\x0d\x0a     \
                \
           if (s\
tatus === 0)\x0d\x0a  \
                \
                \
  return \x22lightG\
ray\x22\x0d\x0a          \
                \
      else if (s\
tatus === 1)\x0d\x0a  \
                \
                \
  return \x22orange\
\x22\x0d\x0a             \
                \
   else if (stat\
us === 2)\x0d\x0a     \
                \
               r\
eturn \x22green\x22\x0d\x0a \
                \
               e\
lse\x0d\x0a           \
                \
         return \
\x22red\x22\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    Item {\x0d\x0a    \
                \
            id: \
itemErrorFounded\
\x0d\x0a              \
                \
  width: 130\x0d\x0a  \
                \
              he\
ight: 65\x0d\x0a      \
                \
          Layout\
.fillWidth: fals\
e\x0d\x0a             \
                \
   Layout.column\
Span: 1\x0d\x0a       \
                \
         RoundBu\
tton {\x0d\x0a        \
                \
            id: \
rbErrorFounded\x0d\x0a\
                \
                \
    width: 40\x0d\x0a \
                \
                \
   height: 40\x0d\x0a \
                \
                \
   text: \x22\x22\x0d\x0a   \
                \
                \
 anchors.horizon\
talCenter: paren\
t.horizontalCent\
er\x0d\x0a\x0d\x0a          \
                \
          backgr\
ound: Rectangle \
{\x0d\x0a             \
                \
           radiu\
s: parent.radius\
\x0d\x0a              \
                \
          color:\
 processBean.pEr\
rorFileFounded ?\
 \x22red\x22 : \x22lightG\
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
tErrorFounded\x0d\x0a \
                \
                \
   text: qsTr(\x22E\
RROR FOUNDED\x22)\x0d\x0a\
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
onRunning\x0d\x0a     \
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
      id: rbCsvC\
reationRunning\x0d\x0a\
                \
                \
    width: 40\x0d\x0a \
                \
                \
   height: 40\x0d\x0a \
                \
                \
   text: \x22\x22\x0d\x0a   \
                \
                \
 anchors.horizon\
talCenter: paren\
t.horizontalCent\
er\x0d\x0a\x0d\x0a          \
                \
          backgr\
ound: Rectangle \
{\x0d\x0a             \
                \
           radiu\
s: parent.radius\
\x0d\x0a              \
                \
          color:\
 processBean.pCs\
vRegThreadRunnin\
g ? ( processBea\
n.pCsvRegThreadP\
ause ? \x22orange\x22 \
: \x22green\x22 ) : \x22l\
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
 id: tCsvCreatio\
nRunning\x0d\x0a      \
                \
              te\
xt: qsTr(\x22CSV CR\
EATION RUN\x22)\x0d\x0a  \
                \
                \
  anchors.bottom\
: parent.bottom\x0d\
\x0a               \
                \
     anchors.bot\
tomMargin: 0\x0d\x0a  \
                \
                \
  anchors.horizo\
ntalCenter: pare\
nt.horizontalCen\
ter\x0d\x0a           \
                \
     }\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     Item {\x0d\x0a   \
                \
             id:\
 itemSpacer\x0d\x0a   \
                \
             wid\
th: 130\x0d\x0a       \
                \
         height:\
 1\x0d\x0a            \
                \
    Layout.fillH\
eight: false\x0d\x0a  \
                \
              La\
yout.fillWidth: \
true\x0d\x0a          \
                \
      Layout.col\
umnSpan: 3\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         Item {\x0d\
\x0a               \
                \
 id: itemCsvNewE\
mpty\x0d\x0a          \
                \
      width: 130\
\x0d\x0a              \
                \
  height: 65\x0d\x0a  \
                \
              Ro\
undButton {\x0d\x0a   \
                \
                \
 id: rbCsvNewEmp\
ty\x0d\x0a            \
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
.pCsvRegThreadCs\
vNewEmpty ? \x22blu\
e\x22 : \x22lightGray\x22\
\x0d\x0a              \
                \
      }\x0d\x0a       \
                \
         }\x0d\x0a    \
                \
            Text\
 {\x0d\x0a            \
                \
        id: tCsv\
NewEmpty\x0d\x0a      \
                \
              te\
xt: qsTr(\x22NEW CS\
V MANUALLY\x22)\x0d\x0a  \
                \
                \
  anchors.bottom\
: parent.bottom\x0d\
\x0a               \
                \
     anchors.bot\
tomMargin: 0\x0d\x0a  \
                \
                \
  anchors.horizo\
ntalCenter: pare\
nt.horizontalCen\
ter\x0d\x0a           \
                \
     }\x0d\x0a        \
                \
    }\x0d\x0a\x0d\x0a       \
                \
     ColumnLayou\
t {\x0d\x0a           \
                \
     id: columnL\
ayout\x0d\x0a         \
                \
       width: 10\
0\x0d\x0a             \
                \
   height: 100\x0d\x0a\
                \
                \
spacing: 0\x0d\x0a\x0d\x0a  \
                \
              Ch\
eckBox {\x0d\x0a      \
                \
              id\
: cbStop\x0d\x0a      \
                \
              te\
xt: qsTr(\x22Stop\x22)\
\x0d\x0a              \
                \
      padding: 1\
\x0d\x0a              \
                \
      onCheckedC\
hanged: processC\
trl.changeStopRe\
questValue(cbSto\
p.checked)\x0d\x0a    \
                \
            }\x0d\x0a\x0d\
\x0a               \
                \
 CheckBox {\x0d\x0a   \
                \
                \
 id: cbPause\x0d\x0a  \
                \
                \
  text: qsTr(\x22Pa\
use\x22)\x0d\x0a         \
                \
           paddi\
ng: 1\x0d\x0a         \
                \
           onChe\
ckedChanged: pro\
cessCtrl.changeP\
auseRequestValue\
(cbPause.checked\
)\x0d\x0a             \
                \
   }\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Item {\x0d\x0a     \
                \
           id: i\
temCleanLocalFol\
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
nLocalFolderStat\
us\x0d\x0a            \
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
lor: gRegenerati\
on.getColor(proc\
essBean.pCsvRegT\
hreadCleanLocalF\
olderStatus)\x0d\x0a  \
                \
                \
  }\x0d\x0a           \
                \
     }\x0d\x0a        \
                \
        Text {\x0d\x0a\
                \
                \
    id: tCleanLo\
calFolderStatus\x0d\
\x0a               \
                \
     text: qsTr(\
\x22CLEAN LOCAL FOL\
DER\x22)\x0d\x0a         \
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
      id: itemCl\
eanCameraFolderS\
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
  id: rbCleanCam\
eraFolderStatus\x0d\
\x0a               \
                \
     width: 40\x0d\x0a\
                \
                \
    height: 40\x0d\x0a\
                \
                \
    text: \x22\x22\x0d\x0a  \
                \
                \
  anchors.horizo\
ntalCenter: pare\
nt.horizontalCen\
ter\x0d\x0a\x0d\x0a         \
                \
           backg\
round: Rectangle\
 {\x0d\x0a            \
                \
            radi\
us: parent.radiu\
s\x0d\x0a             \
                \
           color\
: gRegeneration.\
getColor(process\
Bean.pCsvRegThre\
adCleanCameraFol\
derStatus)\x0d\x0a    \
                \
                \
}\x0d\x0a             \
                \
   }\x0d\x0a          \
                \
      Text {\x0d\x0a  \
                \
                \
  id: tCleanCame\
raFolderStatus\x0d\x0a\
                \
                \
    text: qsTr(\x22\
CLEAN CAMERA FOL\
DER\x22)\x0d\x0a         \
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
acer2\x0d\x0a         \
                \
       width: 13\
0\x0d\x0a             \
                \
   height: 1\x0d\x0a  \
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
n: 5\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Item {\x0d\x0a     \
                \
           id: i\
temRenameLaserIt\
emsStatus\x0d\x0a     \
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
      id: rbRena\
meLaserItemsStat\
us\x0d\x0a            \
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
lor: gRegenerati\
on.getColor(proc\
essBean.pCsvRegT\
hreadRenameLaser\
ItemsStatus)\x0d\x0a  \
                \
                \
  }\x0d\x0a           \
                \
     }\x0d\x0a        \
                \
        Text {\x0d\x0a\
                \
                \
    id: tRenameL\
aserItemsStatus\x0d\
\x0a               \
                \
     text: qsTr(\
\x22RENAME LASER IT\
EMS\x22)\x0d\x0a         \
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
      id: itemDo\
wnloadItemsStatu\
s\x0d\x0a             \
                \
   width: 130\x0d\x0a \
                \
               h\
eight: 65\x0d\x0a     \
                \
           Round\
Button {\x0d\x0a      \
                \
              id\
: rbDownloadItem\
sStatus\x0d\x0a       \
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
   color: gRegen\
eration.getColor\
(processBean.pCs\
vRegThreadDownlo\
adItemsStatus)\x0d\x0a\
                \
                \
    }\x0d\x0a         \
                \
       }\x0d\x0a      \
                \
          Text {\
\x0d\x0a              \
                \
      id: tDownl\
oadItemsStatus\x0d\x0a\
                \
                \
    text: qsTr(\x22\
DOWNLOAD\x22)\x0d\x0a    \
                \
                \
anchors.bottom: \
parent.bottom\x0d\x0a \
                \
                \
   anchors.botto\
mMargin: 0\x0d\x0a    \
                \
                \
anchors.horizont\
alCenter: parent\
.horizontalCente\
r\x0d\x0a             \
                \
   }\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Item {\x0d\x0a     \
                \
           id: i\
temCleanLaserFol\
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
nLaserFolderStat\
us\x0d\x0a            \
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
lor: gRegenerati\
on.getColor(proc\
essBean.pCsvRegT\
hreadCleanLaserF\
olderStatus)\x0d\x0a  \
                \
                \
  }\x0d\x0a           \
                \
     }\x0d\x0a        \
                \
        Text {\x0d\x0a\
                \
                \
    id: tCleanLa\
serFolderStatus\x0d\
\x0a               \
                \
     text: qsTr(\
\x22CLEAN LASER FOL\
DER\x22)\x0d\x0a         \
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
      id: itemCs\
vCreationProcess\
Status\x0d\x0a        \
                \
        width: 1\
30\x0d\x0a            \
                \
    height: 65\x0d\x0a\
                \
                \
RoundButton {\x0d\x0a \
                \
                \
   id: rbCsvCrea\
tionProcessStatu\
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
readCsvCreationP\
rocessStatus)\x0d\x0a \
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
ationProcessStat\
us\x0d\x0a            \
                \
        text: qs\
Tr(\x22CREATION CSV\
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
   id: itemSendC\
svToLaserStatus\x0d\
\x0a               \
                \
 width: 130\x0d\x0a   \
                \
             hei\
ght: 65\x0d\x0a       \
                \
         Layout.\
columnSpan: 1\x0d\x0a \
                \
               R\
oundButton {\x0d\x0a  \
                \
                \
  id: rbSendCsvT\
oLaserStatus\x0d\x0a  \
                \
                \
  width: 40\x0d\x0a   \
                \
                \
 height: 40\x0d\x0a   \
                \
                \
 text: \x22\x22\x0d\x0a     \
                \
               a\
nchors.horizonta\
lCenter: parent.\
horizontalCenter\
\x0d\x0a\x0d\x0a            \
                \
        backgrou\
nd: Rectangle {\x0d\
\x0a               \
                \
         radius:\
 parent.radius\x0d\x0a\
                \
                \
        color: g\
Regeneration.get\
Color(processBea\
n.pCsvRegThreadS\
endCsvToLaserSta\
tus)\x0d\x0a          \
                \
          }\x0d\x0a   \
                \
             }\x0d\x0a\
                \
                \
Text {\x0d\x0a        \
                \
            id: \
tSendCsvToLaserS\
tatus\x0d\x0a         \
                \
           text:\
 qsTr(\x22SEND CSV \
LASER\x22)\x0d\x0a       \
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
SendCsvToCameraS\
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
  id: rbSendCsvT\
oCameraStatus\x0d\x0a \
                \
                \
   width: 40\x0d\x0a  \
                \
                \
  height: 40\x0d\x0a  \
                \
                \
  text: \x22\x22\x0d\x0a    \
                \
                \
anchors.horizont\
alCenter: parent\
.horizontalCente\
r\x0d\x0a\x0d\x0a           \
                \
         backgro\
und: Rectangle {\
\x0d\x0a              \
                \
          radius\
: parent.radius\x0d\
\x0a               \
                \
         color: \
gRegeneration.ge\
tColor(processBe\
an.pCsvRegThread\
SendCsvToCameraS\
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
: tSendCsvToCame\
raStatus\x0d\x0a      \
                \
              te\
xt: qsTr(\x22SEND C\
SV CAMERA\x22)\x0d\x0a   \
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
   }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a    \
                \
    }\x0d\x0a         \
           }\x0d\x0a\x0d\x0a\
                \
    GridLayout {\
\x0d\x0a              \
          id: gF\
ooter\x0d\x0a         \
               w\
idth: 100\x0d\x0a     \
                \
   height: 100\x0d\x0a\
\x0d\x0a              \
          Item {\
\x0d\x0a              \
              La\
yout.fillHeight:\
 false\x0d\x0a        \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
    }\x0d\x0a\x0d\x0a       \
             }\x0d\x0a\
\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a        \
        }\x0d\x0a     \
       }\x0d\x0a\x0d\x0a    \
        Item {\x0d\x0a\
                \
id: settings\x0d\x0a  \
              La\
yout.fillHeight:\
 true\x0d\x0a         \
       Layout.fi\
llWidth: true\x0d\x0a\x0d\
\x0a               \
 GridLayout {\x0d\x0a \
                \
   id: gridLayou\
t\x0d\x0a             \
       layoutDir\
ection: Qt.LeftT\
oRight\x0d\x0a        \
            anch\
ors.right: paren\
t.right\x0d\x0a       \
             anc\
hors.bottom: par\
ent.bottom\x0d\x0a    \
                \
anchors.left: pa\
rent.left\x0d\x0a     \
               a\
nchors.top: pare\
nt.top\x0d\x0a        \
            anch\
ors.rightMargin:\
 10\x0d\x0a           \
         anchors\
.leftMargin: 10\x0d\
\x0a               \
     anchors.bot\
tomMargin: 10\x0d\x0a \
                \
   anchors.topMa\
rgin: 10\x0d\x0a      \
              co\
lumnSpacing: 50\x0d\
\x0a               \
     rowSpacing:\
 50\x0d\x0a           \
         columns\
: 2\x0d\x0a\x0d\x0a         \
           Colum\
nLayout {\x0d\x0a     \
                \
   id: cameraSet\
tingsLayout\x0d\x0a   \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
     GridLayout \
{\x0d\x0a             \
               i\
d: gridLayout2\x0d\x0a\
                \
            Layo\
ut.fillHeight: t\
rue\x0d\x0a           \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
     columns: 2\x0d\
\x0a               \
             col\
umnSpacing: 5\x0d\x0a\x0d\
\x0a               \
             Tex\
t {\x0d\x0a           \
                \
     id: tCamera\
Path\x0d\x0a          \
                \
      text: qsTr\
(\x22Camera path\x22)\x0d\
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
         id: tfC\
ameraPath\x0d\x0a     \
                \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
                \
   text: setting\
sBean.pCameraRem\
otePath\x0d\x0a       \
                \
         onEditi\
ngFinished: proc\
essCtrl.setCamer\
aRemotePath(tfCa\
meraPath.text)\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             But\
ton {\x0d\x0a\x0d\x0a       \
                \
         FileDia\
log {\x0d\x0a         \
                \
           id: c\
ameraFileDialog\x0d\
\x0a               \
                \
     title: qsTr\
(\x22Choose a folde\
r\x22)\x0d\x0a           \
                \
         selectF\
older: true\x0d\x0a   \
                \
                \
 onAccepted: pro\
cessCtrl.setCame\
raRemotePath(cam\
eraFileDialog.fi\
leUrl)\x0d\x0a        \
                \
        }\x0d\x0a\x0d\x0a   \
                \
             id:\
 bCameraFolder\x0d\x0a\
                \
                \
text: qsTr(\x22Chan\
ge camera folder\
\x22)\x0d\x0a            \
                \
    Layout.minim\
umWidth: 140\x0d\x0a  \
                \
              ri\
ghtPadding: 15\x0d\x0a\
                \
                \
leftPadding: 15\x0d\
\x0a               \
                \
 Layout.alignmen\
t: Qt.AlignRight\
 | Qt.AlignVCent\
er\x0d\x0a            \
                \
    Layout.colum\
nSpan: 2\x0d\x0a      \
                \
          onClic\
ked: {\x0d\x0a        \
                \
            came\
raFileDialog.fol\
der = processCtr\
l.getUrlFromNati\
vePath(settingsB\
ean.pCameraRemot\
ePath)\x0d\x0a        \
                \
            came\
raFileDialog.ope\
n()\x0d\x0a           \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      }\x0d\x0a\x0d\x0a     \
                \
       Text {\x0d\x0a \
                \
               i\
d: tCameraPollin\
gTimeMs\x0d\x0a       \
                \
         text: q\
sTr(\x22Polling tim\
e [ms]\x22)\x0d\x0a      \
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
  id: tfCameraPo\
llingTimeMs\x0d\x0a   \
                \
             tex\
t: settingsBean.\
pCameraPollingTi\
meMs\x0d\x0a          \
                \
      Layout.col\
umnSpan: 1\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    validator: I\
ntValidator {\x0d\x0a \
                \
                \
   bottom: 100;\x0d\
\x0a               \
                \
     top: 100000\
;\x0d\x0a             \
                \
   }\x0d\x0a          \
                \
      onEditingF\
inished: setting\
sBean.pCameraPol\
lingTimeMs = tfC\
ameraPollingTime\
Ms.text\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      Item {\x0d\x0a  \
                \
              id\
: element4\x0d\x0a    \
                \
            Layo\
ut.columnSpan: 2\
\x0d\x0a              \
                \
  Layout.fillWid\
th: false\x0d\x0a     \
                \
           Layou\
t.fillHeight: tr\
ue\x0d\x0a            \
                \
    Layout.prefe\
rredWidth: 0\x0d\x0a  \
                \
              La\
yout.preferredHe\
ight: 1\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a\
                \
        }\x0d\x0a\x0d\x0a   \
                \
     GridLayout \
{\x0d\x0a             \
               i\
d: gridLayout3\x0d\x0a\
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a\x0d\x0a          \
                \
  Button {\x0d\x0a    \
                \
            id: \
bCameraSet\x0d\x0a    \
                \
            text\
: qsTr(\x22Set came\
ra configuration\
\x22)\x0d\x0a            \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
            righ\
tPadding: 15\x0d\x0a  \
                \
              le\
ftPadding: 15\x0d\x0a \
                \
               o\
nClicked: settin\
gsCtrl.saveParam\
eters()\x0d\x0a       \
                \
     }\x0d\x0a        \
                \
}\x0d\x0a             \
       }\x0d\x0a\x0d\x0a    \
                \
ColumnLayout {\x0d\x0a\
                \
        id: lase\
rSettingsLayout\x0d\
\x0a               \
         Layout.\
fillWidth: true\x0d\
\x0a\x0d\x0a             \
           GridL\
ayout {\x0d\x0a       \
                \
     id: glLaser\
\x0d\x0a              \
              La\
yout.fillHeight:\
 true\x0d\x0a         \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
       columns: \
2\x0d\x0a             \
               c\
olumnSpacing: 5\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tLase\
rIp\x0d\x0a           \
                \
     text: qsTr(\
\x22Laser IP\x22)\x0d\x0a   \
                \
             Lay\
out.minimumWidth\
: 120\x0d\x0a         \
                \
       Layout.fi\
llWidth: false\x0d\x0a\
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
: tfLaserIp\x0d\x0a   \
                \
             tex\
t: settingsBean.\
pLaserIp\x0d\x0a      \
                \
          Layout\
.columnSpan: 1\x0d\x0a\
                \
                \
Layout.fillWidth\
: true\x0d\x0a        \
                \
        placehol\
derText: \x22Laser \
IP address\x22\x0d\x0a   \
                \
             inp\
utMask: \x22000.000\
.000.000\x22\x0d\x0a     \
                \
           onEdi\
tingFinished: se\
ttingsBean.pLase\
rIp = text\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         Text {\x0d\
\x0a               \
                \
 id: tLaserPort\x0d\
\x0a               \
                \
 text: qsTr(\x22Las\
er port\x22)\x0d\x0a     \
                \
           Layou\
t.minimumWidth: \
120\x0d\x0a           \
                \
     font.pixelS\
ize: 12\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      TextField \
{\x0d\x0a             \
                \
   id: tfLaserPo\
rt\x0d\x0a            \
                \
    text: \x22%0\x22.a\
rg(settingsBean.\
pLaserPort)\x0d\x0a   \
                \
             Lay\
out.columnSpan: \
1\x0d\x0a             \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
           place\
holderText: \x22Las\
er Port\x22\x0d\x0a      \
                \
          inputM\
ask: \x2200000\x22\x0d\x0a  \
                \
              on\
EditingFinished:\
 settingsBean.pL\
aserPort = tfLas\
erPort.text\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Text {\
\x0d\x0a              \
                \
  id: tLaserPoll\
ingTimeMs\x0d\x0a     \
                \
           text:\
 qsTr(\x22Polling t\
ime [ms]\x22)\x0d\x0a    \
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
    id: tfLaserP\
ollingTimeMs\x0d\x0a  \
                \
              te\
xt: settingsBean\
.pLaserPollingTi\
meMs\x0d\x0a          \
                \
      Layout.col\
umnSpan: 1\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    validator: I\
ntValidator {\x0d\x0a \
                \
                \
   bottom: 100;\x0d\
\x0a               \
                \
     top: 100000\
;\x0d\x0a             \
                \
   }\x0d\x0a          \
                \
      onEditingF\
inished: setting\
sBean.pLaserPoll\
ingTimeMs = tfLa\
serPollingTimeMs\
.text\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
    Text {\x0d\x0a    \
                \
            id: \
tLaserRemotePath\
\x0d\x0a              \
                \
  text: qsTr(\x22La\
ser remote path\x22\
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
 id: tfLaserRemo\
tePath\x0d\x0a        \
                \
        text: se\
ttingsBean.pLase\
rRemotePath\x0d\x0a   \
                \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
                \
     onEditingFi\
nished: settings\
Bean.pLaserRemot\
ePath = tfLaserR\
emotePath.text\x0d\x0a\
                \
            }\x0d\x0a\x0d\
\x0a               \
             Ite\
m {\x0d\x0a           \
                \
     id: element\
3\x0d\x0a             \
                \
   Layout.column\
Span: 2\x0d\x0a       \
                \
         Layout.\
preferredHeight:\
 1\x0d\x0a            \
                \
    Layout.prefe\
rredWidth: 0\x0d\x0a  \
                \
              La\
yout.fillHeight:\
 true\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
}\x0d\x0a\x0d\x0a           \
             Gri\
dLayout {\x0d\x0a     \
                \
       id: gridL\
ayout1\x0d\x0a        \
                \
    columns: 2\x0d\x0a\
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a\x0d\x0a          \
                \
  Button {\x0d\x0a    \
                \
            id: \
bLaserSet\x0d\x0a     \
                \
           text:\
 qsTr(\x22Set laser\
 configuration\x22)\
\x0d\x0a              \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
                \
          rightP\
adding: 15\x0d\x0a    \
                \
            left\
Padding: 15\x0d\x0a   \
                \
             onC\
licked: settings\
Ctrl.saveParamet\
ers()\x0d\x0a         \
                \
   }\x0d\x0a\x0d\x0a        \
                \
}\x0d\x0a\x0d\x0a           \
         }\x0d\x0a\x0d\x0a  \
                \
  ColumnLayout {\
\x0d\x0a              \
          id: lo\
calSettingsLayou\
t\x0d\x0a             \
           width\
: 100\x0d\x0a         \
               h\
eight: 100\x0d\x0a    \
                \
    Layout.fillH\
eight: true\x0d\x0a   \
                \
     Layout.colu\
mnSpan: 1\x0d\x0a\x0d\x0a   \
                \
     GridLayout \
{\x0d\x0a             \
               i\
d: gridLayout4\x0d\x0a\
                \
            widt\
h: 100\x0d\x0a        \
                \
    height: 100\x0d\
\x0a               \
             col\
umns: 2\x0d\x0a\x0d\x0a     \
                \
       Text {\x0d\x0a \
                \
               i\
d: tRigheScarto\x0d\
\x0a               \
                \
 text: qsTr(\x22Rig\
he scarto\x22)\x0d\x0a   \
                \
             Lay\
out.minimumWidth\
: 120\x0d\x0a         \
                \
       font.pixe\
lSize: 12\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        TextFiel\
d {\x0d\x0a           \
                \
     id: tfRighe\
Scarto\x0d\x0a        \
                \
        text: se\
ttingsBean.pLoca\
lRowMargin\x0d\x0a    \
                \
            vali\
dator: IntValida\
tor {\x0d\x0a         \
                \
           botto\
m: 0;\x0d\x0a         \
                \
           top: \
20;\x0d\x0a           \
                \
     }\x0d\x0a        \
                \
        onEditin\
gFinished: setti\
ngsBean.pLocalRo\
wMargin = tfRigh\
eScarto.text\x0d\x0a  \
                \
              La\
yout.fillWidth: \
true\x0d\x0a          \
                \
  }\x0d\x0a\x0d\x0a         \
                \
   Text {\x0d\x0a     \
                \
           id: t\
CsvFilename\x0d\x0a   \
                \
             tex\
t: qsTr(\x22Nome fi\
le CSV\x22)\x0d\x0a      \
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
  id: tfCsvFilen\
ame\x0d\x0a           \
                \
     text: setti\
ngsBean.pLocalCs\
vFilename\x0d\x0a     \
                \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
                \
   onEditingFini\
shed: settingsBe\
an.pLocalCsvFile\
name = tfCsvFile\
name.text\x0d\x0a     \
                \
       }\x0d\x0a\x0d\x0a    \
                \
        Text {\x0d\x0a\
                \
                \
id: tLaserErrorF\
ilename\x0d\x0a       \
                \
         text: q\
sTr(\x22Nome file e\
rrore laser\x22)\x0d\x0a \
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
 tfLaserErrorFil\
ename\x0d\x0a         \
                \
       text: set\
tingsBean.pLocal\
LaserErrorFilena\
me\x0d\x0a            \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
            onEd\
itingFinished: s\
ettingsBean.pLoc\
alLaserErrorFile\
name = tfLaserEr\
rorFilename.text\
\x0d\x0a              \
              }\x0d\
\x0a\x0d\x0a             \
               T\
ext {\x0d\x0a         \
                \
       id: tLoad\
ingPath\x0d\x0a       \
                \
         text: q\
sTr(\x22Loading pat\
h\x22)\x0d\x0a           \
                \
     font.pixelS\
ize: 12\x0d\x0a       \
                \
     }\x0d\x0a\x0d\x0a      \
                \
      TextField \
{\x0d\x0a             \
                \
   id: tfLoading\
Path\x0d\x0a          \
                \
      text: sett\
ingsBean.pLocalL\
oadingPath\x0d\x0a    \
                \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
                \
    onEditingFin\
ished: processCt\
rl.setLocalLoadi\
ngPath(tfLoading\
Path.text)\x0d\x0a    \
                \
        }\x0d\x0a\x0d\x0a   \
                \
         Button \
{\x0d\x0a\x0d\x0a           \
                \
     FileDialog \
{\x0d\x0a             \
                \
       id: local\
LoadingPathFileD\
ialog2\x0d\x0a        \
                \
            titl\
e: qsTr(\x22Choose \
a folder\x22)\x0d\x0a    \
                \
                \
selectFolder: tr\
ue\x0d\x0a            \
                \
        onAccept\
ed: processCtrl.\
setLocalLoadingP\
ath(localLoading\
PathFileDialog2.\
fileUrl)\x0d\x0a      \
                \
          }\x0d\x0a\x0d\x0a \
                \
               i\
d: bLoadingPath\x0d\
\x0a               \
                \
 text: qsTr(\x22Cha\
nge loading path\
\x22)\x0d\x0a            \
                \
    rightPadding\
: 15\x0d\x0a          \
                \
      leftPaddin\
g: 15\x0d\x0a         \
                \
       Layout.al\
ignment: Qt.Alig\
nRight | Qt.Alig\
nVCenter\x0d\x0a      \
                \
          Layout\
.columnSpan: 2\x0d\x0a\
                \
                \
onClicked: {\x0d\x0a  \
                \
                \
  localLoadingPa\
thFileDialog2.fo\
lder = processCt\
rl.getUrlFromNat\
ivePath(settings\
Bean.pLocalLoadi\
ngPath)\x0d\x0a       \
                \
             loc\
alLoadingPathFil\
eDialog2.open()\x0d\
\x0a               \
                \
 }\x0d\x0a            \
                \
}\x0d\x0a\x0d\x0a           \
                \
 Text {\x0d\x0a       \
                \
         id: tDo\
wnloadPath\x0d\x0a    \
                \
            text\
: qsTr(\x22Download\
ing path\x22)\x0d\x0a    \
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
DownloadPath\x0d\x0a  \
                \
              te\
xt: settingsBean\
.pLocalDownloadi\
ngPath\x0d\x0a        \
                \
        Layout.f\
illWidth: true\x0d\x0a\
                \
                \
onEditingFinishe\
d: settingsBean.\
pLocalDownloadin\
gPath = tfDownlo\
adPath.text\x0d\x0a   \
                \
         }\x0d\x0a\x0d\x0a  \
                \
          Button\
 {\x0d\x0a\x0d\x0a          \
                \
      FileDialog\
 {\x0d\x0a            \
                \
        id: loca\
lDownloadingPath\
FileDialog\x0d\x0a    \
                \
                \
title: qsTr(\x22Cho\
ose a folder\x22)\x0d\x0a\
                \
                \
    selectFolder\
: true\x0d\x0a        \
                \
            onAc\
cepted: processC\
trl.setLocalDown\
loadingPath(loca\
lDownloadingPath\
FileDialog.fileU\
rl)\x0d\x0a           \
                \
     }\x0d\x0a\x0d\x0a      \
                \
          id: bD\
ownloadPath\x0d\x0a   \
                \
             tex\
t: qsTr(\x22Change \
downloading path\
\x22)\x0d\x0a            \
                \
    rightPadding\
: 15\x0d\x0a          \
                \
      leftPaddin\
g: 15\x0d\x0a         \
                \
       Layout.co\
lumnSpan: 2\x0d\x0a   \
                \
             Lay\
out.alignment: Q\
t.AlignRight | Q\
t.AlignVCenter\x0d\x0a\
                \
                \
onClicked: {\x0d\x0a  \
                \
                \
  localDownloadi\
ngPathFileDialog\
.folder = proces\
sCtrl.getUrlFrom\
NativePath(setti\
ngsBean.pLocalDo\
wnloadingPath)\x0d\x0a\
                \
                \
    localDownloa\
dingPathFileDial\
og.open()\x0d\x0a     \
                \
           }\x0d\x0a  \
                \
          }\x0d\x0a\x0d\x0a \
                \
           Butto\
n {\x0d\x0a           \
                \
     id: bLocalS\
et\x0d\x0a            \
                \
    text: qsTr(\x22\
Set local config\
uration\x22)\x0d\x0a     \
                \
           Layou\
t.columnSpan: 2\x0d\
\x0a               \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
                \
         onClick\
ed: settingsCtrl\
.saveParameters(\
)\x0d\x0a             \
               }\
\x0d\x0a\x0d\x0a\x0d\x0a\x0d\x0a        \
                \
}\x0d\x0a             \
       }\x0d\x0a\x0d\x0a    \
                \
ColumnLayout {\x0d\x0a\
                \
        id: temp\
Layout\x0d\x0a        \
                \
width: 100\x0d\x0a    \
                \
    height: 100\x0d\
\x0a               \
         Layout.\
fillHeight: true\
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
           }\x0d\x0a  \
          }\x0d\x0a\x0d\x0a\x0d\
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
