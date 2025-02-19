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
                    console.log("Opening addUserDialog")
                    addUserDialog.open()
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
        }

        Dialog {
            id: addUserDialog
            title: "Add User"
            modal: true
            standardButtons: Dialog.Ok | Dialog.Cancel
            onAccepted: {
                console.log("User added")
            }

            Column {
                spacing: 10
                TextField {
                    id: emailField
                    placeholderText: "Enter email"
                }
            }
        }
    }
}
