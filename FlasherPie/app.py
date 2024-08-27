import os
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from .ui_form import Ui_Widget
from .button import CustomButton
from .openOcd import OpenOcd
from .cmdExecutor import CommandExecutor
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
        self.ui.menuButton.setOrientation(CustomButton.VerticalTopToBottom)
        self.ui.flashButton.setOrientation(CustomButton.VerticalTopToBottom)
        self.ui.eraseButton.setOrientation(CustomButton.VerticalTopToBottom)
        self.ui.exitButton.setOrientation(CustomButton.VerticalTopToBottom)

        self.ui.powerButton.setOrientation(CustomButton.VerticalBottomToTop)
        self.ui.upButton.setOrientation(CustomButton.VerticalBottomToTop)
        self.ui.downButton.setOrientation(CustomButton.VerticalTopToBottom)
        self.ui.enterButton.setOrientation(CustomButton.VerticalBottomToTop)

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

        self.ui.powerButton.held.connect(self.powerButton_onclick)
        self.ui.upButton.clicked.connect(self.upButton_onclick)
        self.ui.downButton.clicked.connect(self.downButton_onclick)
        self.ui.enterButton.clicked.connect(self.enterButton_onclick)

    def _load_data(self, row: int = 0) -> None:
        self.ui.flashListWidget.clear()

        for memory_card_path in get_memory_card_paths():
            self.openocd.load_data(memory_card_path)

        self.source_dirs = self.openocd.source_dirs()
        if not self.source_dirs:
            return

        self.ui.flashListWidget.addItems(
            [os.path.basename(source_dir) for source_dir in self.source_dirs]
        )
        self.ui.flashListWidget.setCurrentRow(row)

        config = self.openocd.get_config(self.source_dirs[row])

        self.ui.titleLabel.setText(config.get("title", ""))
        self.ui.versionLabel.setText(config.get("version", ""))
        self.ui.dateLabel.setText(config.get("date", ""))
        self.ui.descriptionLabel.setText(config.get("description", ""))

    def menuButton_onclick(self) -> None:
        pass

    def flashButton_onclick(self) -> None:
        self.ui.logListWidget.clear()

        if not self.source_dirs:
            return
        row = self.ui.flashListWidget.currentRow()
        self.openocd.flash(self.source_dirs[row], self.ui.logListWidget.addItem)

    def eraseButton_onclick(self) -> None:
        self.ui.logListWidget.clear()

        if not self.source_dirs:
            return
        row = self.ui.flashListWidget.currentRow()
        self.openocd.erase(self.source_dirs[row], self.ui.logListWidget.addItem)

    def exitButton_onclick(self) -> None:
        pass

    def powerButton_onclick(self) -> None:
        self.ui.logListWidget.clear()

        shutdown_cmd = 'for i in {5..1}; do echo "Shutting down in $i seconds..."; sleep 1; done; shutdown -h now'
        executor = CommandExecutor(shutdown_cmd, self.ui.logListWidget.addItem)
        executor.run()

    def upButton_onclick(self) -> None:
        count = self.ui.flashListWidget.count()
        if count == 0:
            return
        row = self.ui.flashListWidget.currentRow()
        self._load_data((row - 1) % count)

    def downButton_onclick(self) -> None:
        count = self.ui.flashListWidget.count()
        if count == 0:
            return
        row = self.ui.flashListWidget.currentRow()
        self._load_data((row + 1) % count)

    def enterButton_onclick(self) -> None:
        pass
