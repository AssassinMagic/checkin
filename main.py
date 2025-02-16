import sys
import threading
from time import strftime, gmtime, sleep

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

import resources_rc  # Import the compiled resources

class Backend(QObject):
    updated = pyqtSignal(str, arguments=['updater'])
    loadPageSignal = pyqtSignal(str, arguments=['loadPage'])

    def __init__(self):
        super().__init__()

    def updater(self, curr_time):
        """Update time in QML."""
        self.updated.emit(curr_time)

    def bootUp(self):
        """Start a background thread to update time."""
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()

    def _bootUp(self):
        """Continuously update time."""
        while True:
            curr_time = strftime("%H:%M:%S", gmtime())
            self.updater(curr_time)
            sleep(1)  # Update every second

    @pyqtSlot(str)
    def loadPage(self, page_name):
        """Signal to load a new page dynamically."""
        print(f"Switching to page: {page_name}")
        self.loadPageSignal.emit(page_name)


# Ensure QML uses the software renderer
QQuickWindow.setSceneGraphBackend('software')

# Start the PyQt6 application
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

# Initialize backend **before** loading QML
backend = Backend()
context = engine.rootContext()
context.setContextProperty("backend", backend)  # Ensure QML sees `backend`

# Load the QML UI
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')

# Start clock updater
backend.bootUp()

# Run the application
sys.exit(app.exec())
