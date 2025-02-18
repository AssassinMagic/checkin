import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    visible: true
    width: 800
    height: 500
    title: "Evergreen Technologies"
    Material.theme: Material.Dark

    property QtObject backend

    Row {
        anchors.fill: parent

        // Fixed Sidebar
        Rectangle {
            id: sidebar
            width: 50
            height: parent.height
            color: "#2c3e50" // Dark Sidebar Color

            Column {
                anchors.fill: parent
                spacing: 10
                padding: 10

                SidebarButton {
                    iconSource: "icons/home.svg"
                    tooltip: "Home"
                    onClicked: contentLoader.source = "HomePage.qml"
                }

                SidebarButton {
                    iconSource: "icons/folder.svg"
                    tooltip: "Files"
                    onClicked: contentLoader.source = "FilesPage.qml"
                }

                SidebarButton {
                    iconSource: "icons/settings.svg"
                    tooltip: "Settings"
                    onClicked: contentLoader.source = "SettingsPage.qml"
                }

                SidebarButton {
                    iconSource: "icons/attendance.svg"
                    tooltip: "Attendance"
                    onClicked: contentLoader.source = "AttendancePage.qml"
                }
            }
        }

        // Main content area (Updates when page switches)
        Rectangle {
            id: mainContent
            width: parent.width - sidebar.width
            height: parent.height
            color: "#ecf0f1" // Light Background Color

            Loader {
                id: contentLoader
                anchors.fill: parent
                source: "HomePage.qml" // Default page
            }
        }
    }

    // Connect Backend Signals for Dynamic Page Loading
    Connections {
        target: backend
        function onLoadPage(page) {
            contentLoader.source = page;
        }
    }
}
