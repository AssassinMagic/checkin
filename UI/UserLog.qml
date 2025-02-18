import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: parent.width
    height: parent.height
    color: "#18392B"

    ListView {
        id: userListView
        width: parent.width
        height: parent.height
        clip: true
        model: userModel
        delegate: Rectangle {
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
                        text: model.name
                        font.pixelSize: 20
                    }
                    Text {
                        text: model.email
                        font.pixelSize: 16
                    }
                }
                Column {
                    Text {
                        text: "Skate Size: " + model.skateSize
                        font.pixelSize: 16
                    }
                    Text {
                        text: "Time Slot: " + model.timeSlot
                        font.pixelSize: 16
                    }
                }
            }
        }
    }

    ListModel {
        id: userModel
        // Example data, replace with actual data from the database
        ListElement { name: "John Doe"; email: "john.doe@example.com"; skateSize: "10"; timeSlot: "10:00 AM - 11:00 AM" }
        ListElement { name: "Jane Smith"; email: "jane.smith@example.com"; skateSize: "8"; timeSlot: "11:00 AM - 12:00 PM" }
    }
}