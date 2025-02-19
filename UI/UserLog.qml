import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

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
        delegate: Item {
            width: parent.width
            height: 100
            Column {
                spacing: 5
                Text {
                    text: "Name: " + model.name
                    font.pixelSize: 16
                }
                Text {
                    text: "Email: " + model.user_email
                    font.pixelSize: 16
                }
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

    ListModel {
        id: userModel
    }

    Connections {
        target: attendanceBackend
        function onAddUser(user_info) {
            userModel.append(user_info)
        }
    }
}