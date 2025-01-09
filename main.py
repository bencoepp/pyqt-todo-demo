import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt6.QtWidgets import QApplication
from todo import Todo

def main():
    app = QApplication(sys.argv)
    
    qmlRegisterType(Todo, "Demo", 1, 0, "Todo")
    
    engine = QQmlApplicationEngine()

    engine.load(QUrl("main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    root = engine.rootObjects()[0]

    sys.exit(app.exec())

if __name__ == "__main__":
    main()