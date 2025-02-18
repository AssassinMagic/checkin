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
                        text: model.user_email
                        font.pixelSize: 16
                    }
                }
                Column {
                    Text {
                        text: "Skate Size: " + model.skate_size
                        font.pixelSize: 16
                    }
                    Text {
                        text: "Time Slot: " + model.skate_time
                        font.pixelSize: 16
                    }
                }
            }
        }
    }

    ListModel {
        id: userModel
        // Example data, replace with actual data from the database
        ListElement { name: "John Doe"; user_email: "john.doe@example.com"; skate_size: "10"; skate_size: "10:00 AM - 11:00 AM" }
        ListElement { name: "Jane Smith"; user_email: "jane.smith@example.com"; skate_size: "8"; skate_size: "11:00 AM - 12:00 PM" }
    }
}