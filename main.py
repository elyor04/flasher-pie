import sys
from FlasherPie import FlasherPie
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FlasherPie()
    win.show()
    sys.exit(app.exec())
