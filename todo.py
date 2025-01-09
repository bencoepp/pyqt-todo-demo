from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty

class Todo(QObject):
    # -------------------
    # Signals
    # -------------------
    titleChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    dueDateChanged = pyqtSignal(str)
    authorChanged = pyqtSignal(str)
    createdChanged = pyqtSignal(str)
    updatedChanged = pyqtSignal(str)
    doneChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        # -------------------
        # Default property values
        # -------------------
        self._title = "Bill Smith"
        self._description = "555 3264"
        self._dueDate = ""
        self._author = "Ben Cöppicus"
        self._created = ""
        self._updated = ""
        self._done = False

    # -------------------
    # Title
    # -------------------
    @pyqtProperty(str, notify=titleChanged)
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if self._title != value:
            self._title = value
            self.titleChanged.emit(value)

    # -------------------
    # Description
    # -------------------
    @pyqtProperty(str, notify=descriptionChanged)
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if self._description != value:
            self._description = value
            self.descriptionChanged.emit(value)

    # -------------------
    # Due Date
    # -------------------
    @pyqtProperty(str, notify=dueDateChanged)
    def dueDate(self):
        return self._dueDate

    @dueDate.setter
    def dueDate(self, value):
        if self._dueDate != value:
            self._dueDate = value
            self.dueDateChanged.emit(value)

    # -------------------
    # Author
    # -------------------
    @pyqtProperty(str, notify=authorChanged)
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if self._author != value:
            self._author = value
            self.authorChanged.emit(value)

    # -------------------
    # Created
    # -------------------
    @pyqtProperty(str, notify=createdChanged)
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        if self._created != value:
            self._created = value
            self.createdChanged.emit(value)

    # -------------------
    # Updated
    # -------------------
    @pyqtProperty(str, notify=updatedChanged)
    def updated(self):
        return self._updated

    @updated.setter
    def updated(self, value):
        if self._updated != value:
            self._updated = value
            self.updatedChanged.emit(value)

    # -------------------
    # Done
    # -------------------
    @pyqtProperty(bool, notify=doneChanged)
    def done(self):
        return self._done

    @done.setter
    def done(self, value):
        if self._done != value:
            self._done = value
            self.doneChanged.emit(value)

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