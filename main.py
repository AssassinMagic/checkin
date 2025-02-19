import sys
import threading

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from attendance import AttendanceBackend

class Backend(QObject):
    loadPageSignal = pyqtSignal(str, arguments=['loadPage'])

    def __init__(self):
        super().__init__()

    @pyqtSlot(str)
    def loadPage(self, page_name):
        """Signal to load a new page dynamically."""
        self.loadPageSignal.emit(page_name)


if __name__ == "__main__":
    # Start the PyQt6 application
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Initialize backend **before** loading QML
    backend = Backend()
    attendance_backend = AttendanceBackend()

    engine.rootContext().setContextProperty("backend", backend)
    engine.rootContext().setContextProperty("attendanceBackend", attendance_backend)

    # Load the QML UI
    engine.quit.connect(app.quit)
    engine.load('UI/main.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    attendance_backend.start_card_reader()

    # Run the application
    sys.exit(app.exec())
