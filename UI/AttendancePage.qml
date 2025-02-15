import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

Rectangle {
    color: "#18392B"
    anchors.fill: parent
    Material.theme: Material.Dark

    Column {
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        spacing: 10
        padding: 10

        Row {
            spacing: 10
            width: parent.width

            Button {
                text: "+"
                width: 30
                height: 30
                background: Rectangle {
                    color: "#FFFFFF"
                    radius: 10
                    border.color: "#CCCCCC"
                    border.width: 1
                }
            }

            TextField {
                placeholderText: "Search..."
                width: parent.width - 50
                background: Rectangle {
                    color: "#FFFFFF"
                    radius: 10
                    border.color: "#CCCCCC"
                    border.width: 1
                }
                padding: 10
                font.pixelSize: 16
            }
        }

        UserLog {
            width: parent.width
            height: parent.height - 100
        }
    }
}
