import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 50
    height: 50
    radius: 8

    property alias iconSource: icon.source
    property string tooltip
    signal clicked()

    color: mouseArea.containsMouse ? "#1f2b38" : "#34495e" // Hover effect

    Image {
        id: icon
        width: 30
        height: 30
        anchors.centerIn: parent
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
        onClicked: parent.clicked()
    }

    ToolTip {
        visible: mouseArea.containsMouse
        text: parent.tooltip
    }
}
