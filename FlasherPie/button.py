from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QStylePainter,
    QStyleOptionButton,
    QStyle,
    QWidget,
)
from PySide6.QtCore import Qt, QEvent, QTimer, QSize, Signal
from PySide6.QtGui import QPaintEvent, QMouseEvent, QTransform, QPointingDevice


class CustomButton(QPushButton):
    Horizontal = 0
    VerticalTopToBottom = 1
    VerticalBottomToTop = 2

    held = Signal()

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)

        self._orientation = CustomButton.Horizontal
        self._timer = QTimer(self)

        self._initialize_stylesheet()

        self._timer.setInterval(2000)
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._emit_held)

        self.pressed.connect(self._start_timer)
        self.released.connect(self._stop_timer)

    def _initialize_stylesheet(self) -> None:
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50; /* Green background */
                border: none; /* Remove borders */
                color: black; /* Black text */
                padding: 10px 20px; /* Adjusted padding for QPushButton */
                text-align: center; /* Centered text */
                margin: 4px 2px; /* Some space around the button */
                border-radius: 8px; /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green when hovered */
            }
            QPushButton:pressed {
                background-color: #3e8e41;
                padding-top: 12px; /* Simulate button press effect */
                padding-bottom: 8px;
            }
            QPushButton:disabled {
                background-color: #ccc;
            }
            """
        )

    def sizeHint(self) -> QSize:
        size = super().sizeHint()
        if self._orientation != CustomButton.Horizontal:
            return QSize(size.height(), size.width())
        return size

    def minimumSizeHint(self) -> QSize:
        min_size = super().minimumSizeHint()
        if self._orientation != CustomButton.Horizontal:
            return QSize(min_size.height(), min_size.width())
        return min_size

    def orientation(self) -> int:
        return self._orientation

    def setOrientation(self, orientation: int) -> None:
        if orientation not in (
            CustomButton.Horizontal,
            CustomButton.VerticalTopToBottom,
            CustomButton.VerticalBottomToTop,
        ):
            raise ValueError("Invalid orientation value")
        if self._orientation != orientation:
            self._orientation = orientation
            self.updateGeometry()
            self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QStylePainter(self)
        transform = QTransform()
        option = QStyleOptionButton()
        self.initStyleOption(option)

        if self._orientation == CustomButton.Horizontal:
            painter.drawControl(QStyle.CE_PushButton, option)
            return
        elif self._orientation == CustomButton.VerticalTopToBottom:
            transform.rotate(90)
            transform.translate(0, -self.width())
        elif self._orientation == CustomButton.VerticalBottomToTop:
            transform.rotate(-90)
            transform.translate(-self.height(), 0)

        painter.setTransform(transform)
        option.rect = option.rect.transposed()
        painter.drawControl(QStyle.CE_PushButton, option)

    def simulate_button_click(self) -> None:
        center_point = self.rect().center()
        press_event = QMouseEvent(
            QEvent.MouseButtonPress,
            center_point,
            self.mapToGlobal(center_point),
            Qt.LeftButton,
            Qt.LeftButton,
            Qt.NoModifier,
            QPointingDevice.primaryPointingDevice(),
        )
        QApplication.sendEvent(self, press_event)

        QTimer.singleShot(100, self.release_button)

    def release_button(self) -> None:
        center_point = self.rect().center()
        release_event = QMouseEvent(
            QEvent.MouseButtonRelease,
            center_point,
            self.mapToGlobal(center_point),
            Qt.LeftButton,
            Qt.LeftButton,
            Qt.NoModifier,
            QPointingDevice.primaryPointingDevice(),
        )
        QApplication.sendEvent(self, release_event)

    def _start_timer(self) -> None:
        self._timer.start()

    def _stop_timer(self) -> None:
        if self._timer.isActive():
            self._timer.stop()

    def _emit_held(self) -> None:
        if self.isDown():
            self.held.emit()
