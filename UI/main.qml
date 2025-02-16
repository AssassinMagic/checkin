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

    property bool isCollapsed: true // Sidebar initially collapsed


    Row {
        anchors.fill: parent

        // Sidebar (Collapsible)
        Rectangle {
            id: sidebar
            width: isCollapsed ? 60 : 200
            height: parent.height
            color: "#2c3e50" // Dark Sidebar Color

            Behavior on width { NumberAnimation { duration: 150 } } // Smooth Collapse/Expand Animation

            Column {
                anchors.fill: parent
                spacing: 15
                padding: 10

                SidebarButton {
                    iconSource: "qrc:/icons/home.svg"
                    tooltip: "Home"
                    onClicked: contentLoader.source = "HomePage.qml"
                }

                SidebarButton {
                    iconSource: "qrc:/icons/folder.svg"
                    tooltip: "Files"
                    onClicked: contentLoader.source = "FilesPage.qml"
                }

                SidebarButton {
                    iconSource: "qrc:/icons/settings.svg"
                    tooltip: "Settings"
                    onClicked: contentLoader.source = "SettingsPage.qml"
                }

                SidebarButton {
                    iconSource: "qrc:/icons/attendance.svg"
                    tooltip: "Attendance"
                    onClicked: contentLoader.source = "AttendancePage.qml"
                }

                SidebarButton {
                    id: sidebarToggleButton
                    iconSource: isCollapsed ? "qrc:/icons/toggle_off.svg" : "qrc:/icons/toggle_on.svg"
                    tooltip: "Toggle Sidebar"
                    onClicked: {
                        isCollapsed = !isCollapsed
                        sidebarToggleButton.iconSource = isCollapsed ? "qrc:/icons/toggle_off.svg" : "qrc:/icons/toggle_on.svg"
                    }
                }
            }
        }

        // Main content area
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
}
