from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from .ui_form import Ui_Widget
from .button import OrientedButton
from .openOcd import OpenOcd
from .memoryCard import get_memory_card_paths


class FlasherPie(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.openocd = OpenOcd()

        self.ui.setupUi(self)
        self._init_ui()
        self._load_data()

    def _init_ui(self) -> None:
        self.ui.menuButton.setOrientation(OrientedButton.VerticalTopToBottom)
        self.ui.flashButton.setOrientation(OrientedButton.VerticalTopToBottom)
        self.ui.eraseButton.setOrientation(OrientedButton.VerticalTopToBottom)
        self.ui.exitButton.setOrientation(OrientedButton.VerticalTopToBottom)

        self.ui.powerButton.setOrientation(OrientedButton.VerticalBottomToTop)
        self.ui.upButton.setOrientation(OrientedButton.VerticalBottomToTop)
        self.ui.downButton.setOrientation(OrientedButton.VerticalTopToBottom)
        self.ui.enterButton.setOrientation(OrientedButton.VerticalBottomToTop)

        self.ui.menuButton.setText("Menyu")
        self.ui.flashButton.setText("Yozish")
        self.ui.eraseButton.setText("Tozalash")
        self.ui.exitButton.setText("Chiqish")

        self.ui.powerButton.setText("O'chirish")
        self.ui.upButton.setIcon(QIcon("./FlasherPie/resources/pointer.png"))
        self.ui.downButton.setIcon(QIcon("./FlasherPie/resources/pointer.png"))
        self.ui.enterButton.setText("Kirish")

        self.ui.menuButton.clicked.connect(self.menuButton_onclick)
        self.ui.flashButton.clicked.connect(self.flashButton_onclick)
        self.ui.eraseButton.clicked.connect(self.eraseButton_onclick)
        self.ui.exitButton.clicked.connect(self.exitButton_onclick)

        self.ui.powerButton.clicked.connect(self.powerButton_onclick)
        self.ui.upButton.clicked.connect(self.upButton_onclick)
        self.ui.downButton.clicked.connect(self.downButton_onclick)
        self.ui.enterButton.clicked.connect(self.enterButton_onclick)

    def _load_data(self) -> None:
        for memory_card_path in get_memory_card_paths():
            self.openocd.load_data(memory_card_path)

    def menuButton_onclick(self) -> None:
        pass

    def flashButton_onclick(self) -> None:
        pass

    def eraseButton_onclick(self) -> None:
        pass

    def exitButton_onclick(self) -> None:
        pass

    def powerButton_onclick(self) -> None:
        pass

    def upButton_onclick(self) -> None:
        pass

    def downButton_onclick(self) -> None:
        pass

    def enterButton_onclick(self) -> None:
        pass
