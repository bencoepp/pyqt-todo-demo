from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex, pyqtSlot
from todo import Todo
import datetime
import json

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
        self.loadTodosFromJson()

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
        new_todo.created = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        new_todo.updated = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        new_todo.done = done

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._todos.append(new_todo)
        self.endInsertRows()
        self.saveTodosToJson()
    
    @pyqtSlot(str, str, str, str, str, str, bool, int)
    def update(self, title, description, dueDate, author, created, updated, done, index):
        updated_todo = Todo()
        updated_todo.title = title
        updated_todo.description = description
        updated_todo.dueDate = dueDate
        updated_todo.author = author
        updated_todo.created = created
        updated_todo.updated = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        updated_todo.done = done

        self._todos[index] = updated_todo
        self.loadData()
    
    @pyqtSlot(bool, int)
    def updateDone(self, done, index):
        updated_todo = self._todos[index]
        updated_todo.done = done
        updated_todo.updated = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self._todos[index] = updated_todo
        self.loadData()

    @pyqtSlot(int)
    def delete(self, index):
        self._todos.pop(index)
        self.loadData()
    
    def loadData(self):
        self.beginResetModel()
        self.saveTodosToJson()

        self.endResetModel()

    def saveTodosToJson(self):
        data = []
        for todo in self._todos:
            data.append({
                "title": todo.title,
                "description": todo.description,
                "dueDate": todo.dueDate,
                "author": todo.author,
                "created": todo.created,
                "updated": todo.updated,
                "done": todo.done
            })
        
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def loadTodosFromJson(self):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            # In case your file is empty or doesn't contain a list,
            # safely ensure data is a list
            if not isinstance(data, list):
                data = []

            # Reset model to notify any attached views
            self.beginResetModel()
            self._todos.clear()

            for item in data:
                new_todo = Todo()
                new_todo.title = item.get("title", "")
                new_todo.description = item.get("description", "")
                new_todo.dueDate = item.get("dueDate", "")
                new_todo.author = item.get("author", "")
                new_todo.created = item.get("created", "")
                new_todo.updated = item.get("updated", "")
                new_todo.done = item.get("done", False)
                self._todos.append(new_todo)

            self.endResetModel()

        except FileNotFoundError:
            print(f"File not found: {"data.json"}")
        except json.JSONDecodeError as e:
            print(f"JSON decode error in {"data.json"}: {e}")