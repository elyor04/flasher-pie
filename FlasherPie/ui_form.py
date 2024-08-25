# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from .button import OrientedButton

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(480, 800)
        Widget.setStyleSheet(u"background-color: rgb(127, 127, 127);")
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 401, 781))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.flashListWidget = QListWidget(self.widget)
        self.flashListWidget.setObjectName(u"flashListWidget")
        self.flashListWidget.setStyleSheet(u"background-color: rgb(200, 200, 200);")

        self.verticalLayout_3.addWidget(self.flashListWidget)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleLabel)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.versionLabel = QLabel(self.widget)
        self.versionLabel.setObjectName(u"versionLabel")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.versionLabel)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.dateLabel = QLabel(self.widget)
        self.dateLabel.setObjectName(u"dateLabel")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dateLabel)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.descriptionLabel = QLabel(self.widget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.descriptionLabel)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_3)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.logListWidget = QListWidget(self.widget)
        self.logListWidget.setObjectName(u"logListWidget")
        self.logListWidget.setStyleSheet(u"background-color: rgb(50, 50, 50);")

        self.verticalLayout_3.addWidget(self.logListWidget)

        self.widget1 = QWidget(Widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(440, 0, 41, 801))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.powerButton = OrientedButton(self.widget1)
        self.powerButton.setObjectName(u"powerButton")

        self.verticalLayout_2.addWidget(self.powerButton)

        self.upButton = OrientedButton(self.widget1)
        self.upButton.setObjectName(u"upButton")

        self.verticalLayout_2.addWidget(self.upButton)

        self.downButton = OrientedButton(self.widget1)
        self.downButton.setObjectName(u"downButton")

        self.verticalLayout_2.addWidget(self.downButton)

        self.enterButton = OrientedButton(self.widget1)
        self.enterButton.setObjectName(u"enterButton")

        self.verticalLayout_2.addWidget(self.enterButton)

        self.widget2 = QWidget(Widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 0, 41, 801))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuButton = OrientedButton(self.widget2)
        self.menuButton.setObjectName(u"menuButton")

        self.verticalLayout.addWidget(self.menuButton)

        self.flashButton = OrientedButton(self.widget2)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.eraseButton = OrientedButton(self.widget2)
        self.eraseButton.setObjectName(u"eraseButton")

        self.verticalLayout.addWidget(self.eraseButton)

        self.exitButton = OrientedButton(self.widget2)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout.addWidget(self.exitButton)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Qurilma:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Versiya:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Sana:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Tavsif:", None))
    # retranslateUi

