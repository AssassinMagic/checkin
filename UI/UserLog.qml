import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: parent.width
    height: parent.height
    color: "#18392B"

    Column {
        spacing: 10
        width: parent.width
        height: parent.height

        // Hardcoded user information
        Rectangle {
            width: parent.width
            height: 100
            color: "#FFFFFF"
            radius: 10
            border.color: "#CCCCCC"
            border.width: 1
            Row {
                anchors.fill: parent
                anchors.margins: 10
                spacing: 20
                Column {
                    Text {
                        text: "John Doe"
                        font.pixelSize: 20
                    }
                    Text {
                        text: "john.doe@example.com"
                        font.pixelSize: 16
                    }
                }
                Column {
                    Text {
                        text: "Skate Size: 10"
                        font.pixelSize: 16
                    }
                    Text {
                        text: "Time Slot: 10:00 AM - 11:00 AM"
                        font.pixelSize: 16
                    }
                }
            }
        }

        Rectangle {
            width: parent.width
            height: 100
            color: "#FFFFFF"
            radius: 10
            border.color: "#CCCCCC"
            border.width: 1
            Row {
                anchors.fill: parent
                anchors.margins: 10
                spacing: 20
                Column {
                    Text {
                        text: "Jane Smith"
                        font.pixelSize: 20
                    }
                    Text {
                        text: "jane.smith@example.com"
                        font.pixelSize: 16
                    }
                }
                Column {
                    Text {
                        text: "Skate Size: 8"
                        font.pixelSize: 16
                    }
                    Text {
                        text: "Time Slot: 11:00 AM - 12:00 PM"
                        font.pixelSize: 16
                    }
                }
            }
        }
    }
}