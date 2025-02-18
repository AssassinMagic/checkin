import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

Rectangle {
    color: "#18392B"
    anchors.fill: parent
    Material.theme: Material.Dark

    Column {
        anchors.fill: parent
        spacing: 10
        padding: 10

        Row {
            spacing: 10
            width: parent.width

            Button {
                text: "+"
                width: searchField.height
                height: searchField.height
                Material.background: Material.White
                Material.foreground: Material.Black
                onClicked: {
                    // Example user info, replace with actual data from the database
                    attendanceBackend.addUser({ "name": "New User", "email": "new.user@example.com", "skateSize": "9", "timeSlot": "12:00 PM - 1:00 PM" })
                }
            }

            TextField {
                id: searchField
                placeholderText: "Search..."
                width: parent.width - searchField.height - 10
                padding: 10
                font.pixelSize: 16
                Material.background: Material.White
                Material.foreground: Material.Black
            }
        }

        UserLog {
            width: parent.width
            height: parent.height - 100
        }
    }
}
