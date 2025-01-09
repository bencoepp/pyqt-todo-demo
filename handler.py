from PyQt6.QtCore import QObject, pyqtSlot

class Handler(QObject):
    @pyqtSlot(str)
    def handleSignal(self, message: str):
        print("Received from QML:", message)
    @pyqtSlot(str,str,str,str,str,str,bool)
    def saveTodo(self, title: str, description: str, dueDate: str, auther: str, created: str, updated: str, done: bool):
        print("Saving data: " + title)