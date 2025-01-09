from PyQt6.QtCore import QObject, pyqtSlot

class Handler(QObject):
    @pyqtSlot(str)
    def handleSignal(self, message: str):
        print("Received from QML:", message)