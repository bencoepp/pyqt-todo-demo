from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex, pyqtSlot
from todo import Todo

class TodoHandler(QAbstractListModel):
    TITLE_ROLE = Qt.ItemDataRole.UserRole + 1
    DESCRIPTION_ROLE = Qt.ItemDataRole.UserRole + 2
    DUEDATE_ROLE = Qt.ItemDataRole.UserRole + 3
    AUTHOR_ROLE = Qt.ItemDataRole.UserRole + 4
    CREATED_ROLE = Qt.ItemDataRole.UserRole + 5
    UPDATED_ROLE = Qt.ItemDataRole.UserRole + 6
    DONE_ROLE = Qt.ItemDataRole.UserRole + 7

    def __init__(self, parent=None):
        super().__init__(parent)
        self._todos = []

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self._todos)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount()):
            return None

        todo = self._todos[index.row()]

        if role == self.TITLE_ROLE:
            return todo.title
        elif role == self.DESCRIPTION_ROLE:
            return todo.description
        elif role == self.DUEDATE_ROLE:
            return todo.dueDate
        elif role == self.AUTHOR_ROLE:
            return todo.author
        elif role == self.CREATED_ROLE:
            return todo.created
        elif role == self.UPDATED_ROLE:
            return todo.updated
        elif role == self.DONE_ROLE:
            return todo.done

        return None

    def roleNames(self):
        roles = super().roleNames()
        roles[self.TITLE_ROLE] = b"title"
        roles[self.DESCRIPTION_ROLE] = b"description"
        roles[self.DUEDATE_ROLE] = b"dueDate"
        roles[self.AUTHOR_ROLE] = b"author"
        roles[self.CREATED_ROLE] = b"created"
        roles[self.UPDATED_ROLE] = b"updated"
        roles[self.DONE_ROLE] = b"done"
        return roles

    @pyqtSlot(str, str, str, str, str, str, bool)
    def create(self, title, description, dueDate, author, created, updated, done):
        new_todo = Todo()
        new_todo.title = title
        new_todo.description = description
        new_todo.dueDate = dueDate
        new_todo.author = author
        new_todo.created = created
        new_todo.updated = updated
        new_todo.done = done

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._todos.append(new_todo)
        self.endInsertRows()