import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine

from handler import Handler

def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    handler = Handler()

    engine.load(QUrl("main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    root_object = engine.rootObjects()[0]

    root_object.onSaveBtnClicked.connect(handler.handleSignal)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()