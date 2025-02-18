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
                onClicked: addUserDialog.open()
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

    Dialog {
        id: addUserDialog
        title: "Search User"
        modal: true
        standardButtons: Dialog.Ok | Dialog.Cancel
        onAccepted: {
            attendanceBackend.searchUserByEmail(emailField.text)
        }

        Column {
            spacing: 10
            padding: 10

            TextField {
                id: emailField
                placeholderText: "Email"
                width: parent.width
                font.pixelSize: 16
                Material.background: Material.White
                Material.foreground: Material.Black
            }
        }
    }
}
