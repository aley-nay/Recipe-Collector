# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_anapencere(object):
    def setupUi(self, anapencere):
        if not anapencere.objectName():
            anapencere.setObjectName(u"anapencere")
        anapencere.resize(1017, 600)
        self.centralwidget = QWidget(anapencere)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(290, 220, 401, 171))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.butonMusterigir = QPushButton(self.gridLayoutWidget)
        self.butonMusterigir.setObjectName(u"butonMusterigir")

        self.gridLayout_2.addWidget(self.butonMusterigir, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 130, 461, 61))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        anapencere.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(anapencere)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1017, 21))
        anapencere.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(anapencere)
        self.statusbar.setObjectName(u"statusbar")
        anapencere.setStatusBar(self.statusbar)

        self.retranslateUi(anapencere)

        QMetaObject.connectSlotsByName(anapencere)
    # setupUi

    def retranslateUi(self, anapencere):
        anapencere.setWindowTitle(QCoreApplication.translate("anapencere", u"anapencere", None))
        self.label_2.setText(QCoreApplication.translate("anapencere", u"M\u00fc\u015fteri Giri\u015f", None))
        self.butonMusterigir.setText(QCoreApplication.translate("anapencere", u"m\u00fc\u015fteri gir", None))
        self.label.setText(QCoreApplication.translate("anapencere", u"Aleynaynay", None))
    # retranslateUi

