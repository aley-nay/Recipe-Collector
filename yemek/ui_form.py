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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_anapencere(object):
    def setupUi(self, anapencere):
        if not anapencere.objectName():
            anapencere.setObjectName(u"anapencere")
        anapencere.resize(601, 339)
        self.centralwidget = QWidget(anapencere)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 451, 61))
        font = QFont()
        font.setFamilies([u"Andina Demo"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
"font: 20pt \"Andina Demo\";\n"
"color:#f4cccc")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 110, 581, 251))
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget{background: white;}\n"
"QTableWidget::item{background: white;  border: 2px solid #f4cccc;}\n"
"QTableWidget::item::pressed{background:  #e06666;}\n"
"QTableWidget::item::hover{background:  #e06666;}\n"
"QHeaderView::section { background-color:#f4cccc; color:#e06666; font-weight:800}\n"
"QTableView QTableCornerButton::section{ background-color:#f4cccc }\n"
"QTableWidget::item:selected{ background-color: #e06666 }\n"
"")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 70, 581, 40))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"A Year Without Rain"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"\n"
"color: black;\n"
"font: 14pt \"A Year Without Rain\";")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_panel = QPushButton(self.horizontalLayoutWidget)
        self.btn_panel.setObjectName(u"btn_panel")
        self.btn_panel.setMaximumSize(QSize(200, 16777215))
        self.btn_panel.setStyleSheet(u"QPushButton {\n"
"font: 500 10pt \"Arimo Medium\";\n"
"font-weight:400;\n"
"color: white;\n"
"background: #f4cccc;\n"
"color:white;\n"
"border: 2px solid #f4cccc;\n"
"padding: 5px;}\n"
"QPushButton:hover {\n"
"background-color: #ea9999;\n"
"border: 2px solid #ea9999;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #e06666;\n"
"border: 2px solid #e06666;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_panel)

        anapencere.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(anapencere)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 601, 21))
        anapencere.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(anapencere)
        self.statusbar.setObjectName(u"statusbar")
        anapencere.setStatusBar(self.statusbar)

        self.retranslateUi(anapencere)

        QMetaObject.connectSlotsByName(anapencere)
    # setupUi

    def retranslateUi(self, anapencere):
        anapencere.setWindowTitle(QCoreApplication.translate("anapencere", u"anapencere", None))
        self.label.setText(QCoreApplication.translate("anapencere", u"Y\u00f6re Y\u00f6re, Yiye Yiye", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("anapencere", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("anapencere", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("anapencere", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("anapencere", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("anapencere", u"5", None));
        self.label_2.setText(QCoreApplication.translate("anapencere", u"Yemek Listesi", None))
        self.btn_panel.setText(QCoreApplication.translate("anapencere", u"Yemek Paneli Giri\u015f", None))
    # retranslateUi

