from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, 

class Todo(QObject):
    titleChanged = pyqtSignal(str)
    descriptionChanged = pyqtSignal(str)
    dueDateChanged = pyqtSignal(str)
    authorChanged = pyqtSignal(str)
    createdChanged = pyqtSignal(str)
    updatedChanged = pyqtSignal(str)
    doneChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(Todo, self).__init__(parent)

        self._title = "A nice todo"
        self._description = "555 3264"
        self._dueDate = ""
        self._author = "Ben Cöppicus"
        self._created = ""
        self._updated = ""
        self._done = False

    def getTitle(self):
        return self._title

    def setTitle(self, value):
        if self._title != value:
            self._title = value
            self.titleChanged.emit(value)

    title = Property(str, fget=getTitle, fset=setTitle, notify=titleChanged)

    def getDescription(self):
        return self._description

    def setDescription(self, value):
        if self._description != value:
            self._description = value
            self.descriptionChanged.emit(value)

    description = Property(
        str, fget=getDescription, fset=setDescription, notify=descriptionChanged
    )

    def getDueDate(self):
        return self._dueDate

    def setDueDate(self, value):
        if self._dueDate != value:
            self._dueDate = value
            self.dueDateChanged.emit(value)

    dueDate = Property(str, fget=getDueDate, fset=setDueDate, notify=dueDateChanged)

    def getAuthor(self):
        return self._author

    def setAuthor(self, value):
        if self._author != value:
            self._author = value
            self.authorChanged.emit(value)

    author = Property(str, fget=getAuthor, fset=setAuthor, notify=authorChanged)

    def getCreated(self):
        return self._created

    def setCreated(self, value):
        if self._created != value:
            self._created = value
            self.createdChanged.emit(value)

    created = Property(str, fget=getCreated, fset=setCreated, notify=createdChanged)

    def getUpdated(self):
        return self._updated

    def setUpdated(self, value):
        if self._updated != value:
            self._updated = value
            self.updatedChanged.emit(value)

    updated = Property(str, fget=getUpdated, fset=setUpdated, notify=updatedChanged)

    def getDone(self):
        return self._done

    def setDone(self, value):
        if self._done != value:
            self._done = value
            self.doneChanged.emit(value)

    done = Property(bool, fget=getDone, fset=setDone, notify=doneChanged)

    # --- CRUD Method Stubs ---
    @Slot()
    def create(self):
        # TODO: implement create logic
        print("Create called")

    @Slot()
    def read(self):
        # TODO: implement read logic
        print("Read called")

    @Slot()
    def update(self):
        # TODO: implement update logic
        print("Update called")

    @Slot()
    def delete(self):
        # TODO: implement delete logic
        print("Delete called")