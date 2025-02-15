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

    property string currTime: "00:00:00"
    property QtObject backend
    property bool isCollapsed: false // Sidebar toggle state

    Row {
        anchors.fill: parent

        // Sidebar (Collapsible)
        Rectangle {
            id: sidebar
            width: isCollapsed ? 50 : 150
            height: parent.height
            color: "#2c3e50" // Dark Sidebar Color

            Behavior on width { NumberAnimation { duration: 125 } } // Smooth Collapse/Expand Animation

            Column {
                anchors.fill: parent
                spacing: 10
                padding: 10

                Button {
                    text: "🏠 Home"
                    width: sidebar.width - 20
                    height: 50
                    onClicked: contentLoader.source = "HomePage.qml"
                }

                Button {
                    text: "📁 Files"
                    width: sidebar.width - 20
                    height: 50
                    onClicked: contentLoader.source = "FilesPage.qml"
                }

                Button {
                    text: "⚙️ Settings"
                    width: sidebar.width - 20
                    height: 50
                    onClicked: contentLoader.source = "SettingsPage.qml"
                }

                Button {
                    text: "📄 Attendance"
                    width: sidebar.width - 20
                    height: 50
                    onClicked: contentLoader.source = "AttendancePage.qml"
                }

                // Sidebar Toggle Button
                Button {
                    text: isCollapsed ? ">>" : "<<"
                    width: isCollapsed ? 40 : 60
                    height: 40
                    background: Rectangle {
                        color: "#34495e"
                        radius: 10
                    }
                    onClicked: isCollapsed = !isCollapsed
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
        function onUpdated(msg) {
            currTime = msg;
        }
        function onLoadPage(page) {
            contentLoader.source = page;
        }
    }
}
