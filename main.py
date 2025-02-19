import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtQml import QQmlApplicationEngine, QQmlDebuggingEnabler
from attendance import AttendanceBackend
import time
from PyQt6.QtCore import QTimer

class Backend(QObject):
    loadPageSignal = pyqtSignal(str, arguments=['loadPage'])

    def __init__(self):
        super().__init__()

    @pyqtSlot(str)
    def loadPage(self, page_name):
        """Signal to load a new page dynamically."""
        self.loadPageSignal.emit(page_name)

def test_signal():
    print("📡 Emitting test signal to QML...")
    attendance_backend.addUserSignal.emit({
        "name": "Test User",
        "user_email": "test@example.com",
        "skate_size": "42",
        "skate_time": "10:00 AM"
    })

if __name__ == "__main__":
    QQmlDebuggingEnabler()

    # Start the PyQt6 application
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Initialize backend **before** loading QML
    backend = Backend()
    attendance_backend = AttendanceBackend()

    engine.rootContext().setContextProperty("backend", backend)
    engine.rootContext().setContextProperty("attendanceBackend", attendance_backend)
    print("✅ attendanceBackend registered in QML")

    QTimer.singleShot(5000, test_signal)

    attendance_backend.addUserSignal.connect(lambda _: backend.loadPageSignal.emit("UserLog.qml"))
    attendance_backend.addUserSignal.connect(lambda user_info: print(f"📡 Signal emitted with: {user_info}"))


    # Load the QML UI
    engine.quit.connect(app.quit)
    engine.load('UI/main.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    # Start the card reader after the QML UI is loaded
    print("Starting card reader...")
    attendance_backend.start_card_reader()

    # Run the application
    sys.exit(app.exec())
