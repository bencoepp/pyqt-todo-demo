from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty

class TodoHandler(QObject):
    # -------------------
    # Signals
    # -------------------
    dataChanged = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        # -------------------
        # Default property values
        # -------------------
        self._data = []
    
    # -------------------
    # Title
    # -------------------
    @pyqtProperty(list, notify=dataChanged)
    def data(self):
        return self._data

    # -------------------
    # CRUD Method Stubs
    # -------------------
    @pyqtSlot()
    def create(self):
        # TODO: implement create logic
        print("Create called")

    @pyqtSlot()
    def read(self):
        # TODO: implement read logic
        print("Read called")

    @pyqtSlot()
    def update(self):
        # TODO: implement update logic
        print("Update called")

    @pyqtSlot()
    def delete(self):
        # TODO: implement delete logic
        print("Delete called")