from PySide6.QtCore import QCoreApplication, QRect, QMetaObject
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLabel,
    QFormLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from .button import CustomButton


class Ui_FlasherPie:
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(480, 800)
        Widget.setStyleSheet("background-color: rgb(127, 127, 127);")

        self.setupMainWidget(Widget)
        self.setupRightSideButtons(Widget)
        self.setupLeftSideButtons(Widget)
        self.setupTopBar(Widget)
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    def setupMainWidget(self, parent):
        self.widget = QWidget(parent)
        self.widget.setGeometry(QRect(40, 30, 401, 761))
        self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.flashListWidget = QListWidget(self.widget)
        self.flashListWidget.setStyleSheet(
            "background-color: rgb(200, 200, 200); color: black;"
        )
        self.layout.addWidget(self.flashListWidget)

        self.formLayout = QFormLayout()
        self.setupForm(self.widget)
        self.layout.addLayout(self.formLayout)

        self.logListWidget = QListWidget(self.widget)
        self.logListWidget.setStyleSheet(
            "background-color: rgb(50, 50, 50); color: white;"
        )
        self.layout.addWidget(self.logListWidget)

    def setupForm(self, parent):
        self.label = QLabel(parent)
        self.label.setStyleSheet("color: black;")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.titleLabel = QLabel(parent)
        self.titleLabel.setStyleSheet("color: black;")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleLabel)

        self.label_2 = QLabel(parent)
        self.label_2.setStyleSheet("color: black;")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.versionLabel = QLabel(parent)
        self.versionLabel.setStyleSheet("color: black;")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.versionLabel)

        self.label_3 = QLabel(parent)
        self.label_3.setStyleSheet("color: black;")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.dateLabel = QLabel(parent)
        self.dateLabel.setStyleSheet("color: black;")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateLabel)

        self.label_4 = QLabel(parent)
        self.label_4.setStyleSheet("color: black;")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.descriptionLabel = QLabel(parent)
        self.descriptionLabel.setStyleSheet("color: black;")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.descriptionLabel)

    def setupRightSideButtons(self, parent):
        self.widgetRight = QWidget(parent)
        self.widgetRight.setGeometry(QRect(440, 0, 41, 801))
        self.layoutRight = QVBoxLayout(self.widgetRight)
        self.layoutRight.setContentsMargins(0, 0, 0, 0)

        self.powerButton = CustomButton(self.widgetRight)
        self.powerButton.setObjectName("powerButton")
        self.layoutRight.addWidget(self.powerButton)

        self.upButton = CustomButton(self.widgetRight)
        self.upButton.setObjectName("upButton")
        self.layoutRight.addWidget(self.upButton)

        self.downButton = CustomButton(self.widgetRight)
        self.downButton.setObjectName("downButton")
        self.layoutRight.addWidget(self.downButton)

        self.enterButton = CustomButton(self.widgetRight)
        self.enterButton.setObjectName("enterButton")
        self.layoutRight.addWidget(self.enterButton)

    def setupLeftSideButtons(self, parent):
        self.widgetLeft = QWidget(parent)
        self.widgetLeft.setGeometry(QRect(0, 0, 41, 801))
        self.layoutLeft = QVBoxLayout(self.widgetLeft)
        self.layoutLeft.setContentsMargins(0, 0, 0, 0)

        self.menuButton = CustomButton(self.widgetLeft)
        self.menuButton.setObjectName("menuButton")
        self.layoutLeft.addWidget(self.menuButton)

        self.flashButton = CustomButton(self.widgetLeft)
        self.flashButton.setObjectName("flashButton")
        self.layoutLeft.addWidget(self.flashButton)

        self.eraseButton = CustomButton(self.widgetLeft)
        self.eraseButton.setObjectName("eraseButton")
        self.layoutLeft.addWidget(self.eraseButton)

        self.exitButton = CustomButton(self.widgetLeft)
        self.exitButton.setObjectName("exitButton")
        self.layoutLeft.addWidget(self.exitButton)

    def setupTopBar(self, parent):
        self.widgetTop = QWidget(parent)
        self.widgetTop.setGeometry(QRect(40, 0, 401, 22))
        self.horizontalLayout = QHBoxLayout(self.widgetTop)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.label_5 = QLabel(self.widgetTop)
        self.label_5.setStyleSheet("color: black;")
        self.horizontalLayout.addWidget(self.label_5)

        self.timeLabel = QLabel(self.widgetTop)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_8 = QLabel(self.widgetTop)
        self.label_8.setStyleSheet("color: black;")
        self.horizontalLayout.addWidget(self.label_8)

        self.powerLabel = QLabel(self.widgetTop)
        self.powerLabel.setObjectName("powerLabel")
        self.horizontalLayout.addWidget(self.powerLabel)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Flasher Pie"))
        self.label.setText(QCoreApplication.translate("Widget", "Qurilma:"))
        self.label_2.setText(QCoreApplication.translate("Widget", "Versiya:"))
        self.label_3.setText(QCoreApplication.translate("Widget", "Sana:"))
        self.label_4.setText(QCoreApplication.translate("Widget", "Tavsif:"))
        self.label_5.setText(QCoreApplication.translate("Widget", "Vaqt:"))
        self.timeLabel.setText(QCoreApplication.translate("Widget", "16:00"))
        self.label_8.setText(QCoreApplication.translate("Widget", "Quvvat:"))
        self.powerLabel.setText(QCoreApplication.translate("Widget", "50%"))
