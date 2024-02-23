# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yemekekle.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_yemekekle(object):
    def setupUi(self, yemekekle):
        if not yemekekle.objectName():
            yemekekle.setObjectName(u"yemekekle")
        yemekekle.resize(606, 564)
        self.centralwidget = QWidget(yemekekle)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 591, 271))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setFamilies([u"A Year Without Rain"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"font: 500 10pt \"A Year Without Rain\";\n"
"color: black;\n"
"font-weight: 800\n"
"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.yemek_id = QLineEdit(self.verticalLayoutWidget_3)
        self.yemek_id.setObjectName(u"yemek_id")
        self.yemek_id.setEnabled(True)
        self.yemek_id.setStyleSheet(u"border: 2px solid #f4cccc;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.yemek_id)

        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 500 10pt \"A Year Without Rain\";\n"
"color: black;\n"
"font-weight: 800")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.yemek_turu = QLineEdit(self.verticalLayoutWidget_3)
        self.yemek_turu.setObjectName(u"yemek_turu")
        self.yemek_turu.setStyleSheet(u"border: 2px solid #f4cccc;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.yemek_turu)


        self.horizontalLayout_3.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 500 10pt \"A Year Without Rain\";\n"
"color: black;\n"
"font-weight: 800")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.yemek_yoresi = QLineEdit(self.verticalLayoutWidget_3)
        self.yemek_yoresi.setObjectName(u"yemek_yoresi")
        self.yemek_yoresi.setStyleSheet(u"border: 2px solid #f4cccc;")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.yemek_yoresi)

        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(5, 50))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"font: 500 10pt \"A Year Without Rain\";\n"
"color: black;\n"
"font-weight: 800")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.yemek_adi = QLineEdit(self.verticalLayoutWidget_3)
        self.yemek_adi.setObjectName(u"yemek_adi")
        self.yemek_adi.setStyleSheet(u"border: 2px solid #f4cccc;")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.yemek_adi)


        self.horizontalLayout_3.addLayout(self.formLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 500 10pt \"A Year Without Rain\";\n"
"color: black;\n"
"font-weight: 800")

        self.verticalLayout_2.addWidget(self.label_4)

        self.yemek_tarifi = QTextEdit(self.verticalLayoutWidget_3)
        self.yemek_tarifi.setObjectName(u"yemek_tarifi")
        self.yemek_tarifi.setStyleSheet(u"border: 2px solid #f4cccc;")

        self.verticalLayout_2.addWidget(self.yemek_tarifi)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_guncelle = QPushButton(self.verticalLayoutWidget_3)
        self.btn_guncelle.setObjectName(u"btn_guncelle")
        self.btn_guncelle.setStyleSheet(u"QPushButton {\n"
"font: 500 10pt \"Arimo Medium\";\n"
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

        self.horizontalLayout_2.addWidget(self.btn_guncelle)

        self.btn_sil = QPushButton(self.verticalLayoutWidget_3)
        self.btn_sil.setObjectName(u"btn_sil")
        self.btn_sil.setStyleSheet(u"QPushButton {\n"
"font: 500 10pt \"Arimo Medium\";\n"
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

        self.horizontalLayout_2.addWidget(self.btn_sil)

        self.btn_getir = QPushButton(self.verticalLayoutWidget_3)
        self.btn_getir.setObjectName(u"btn_getir")
        self.btn_getir.setStyleSheet(u"QPushButton {\n"
"font: 500 10pt \"Arimo Medium\";\n"
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

        self.horizontalLayout_2.addWidget(self.btn_getir)

        self.btn_yeni = QPushButton(self.verticalLayoutWidget_3)
        self.btn_yeni.setObjectName(u"btn_yeni")
        self.btn_yeni.setStyleSheet(u"QPushButton {\n"
"font: 500 10pt \"Arimo Medium\";\n"
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

        self.horizontalLayout_2.addWidget(self.btn_yeni)

        self.btn_kaydet = QPushButton(self.verticalLayoutWidget_3)
        self.btn_kaydet.setObjectName(u"btn_kaydet")
        self.btn_kaydet.setStyleSheet(u"QPushButton {\n"
"font: 500 10pt \"Arimo Medium\";\n"
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

        self.horizontalLayout_2.addWidget(self.btn_kaydet)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

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
        self.tableWidget.setGeometry(QRect(10, 300, 591, 251))
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget{background: white;}\n"
"QTableWidget::item{background: white;  border: 2px solid #f4cccc;}\n"
"QTableWidget::item::pressed{background:  #e06666;}\n"
"QTableWidget::item::hover{background:  #e06666;}\n"
"QHeaderView::section { background-color:#f4cccc; color:#e06666; font-weight:800}\n"
"QTableView QTableCornerButton::section{ background-color:#f4cccc }\n"
"QTableWidget::item:selected{ background-color: #e06666 }\n"
"")
        yemekekle.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(yemekekle)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 606, 21))
        yemekekle.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(yemekekle)
        self.statusbar.setObjectName(u"statusbar")
        yemekekle.setStatusBar(self.statusbar)

        self.retranslateUi(yemekekle)

        QMetaObject.connectSlotsByName(yemekekle)
    # setupUi

    def retranslateUi(self, yemekekle):
        yemekekle.setWindowTitle(QCoreApplication.translate("yemekekle", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("yemekekle", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("yemekekle", u"Yemek T\u00fcr\u00fc", None))
        self.label_6.setText(QCoreApplication.translate("yemekekle", u"Yemek Y\u00f6resi", None))
        self.label_7.setText(QCoreApplication.translate("yemekekle", u"Yemek Ad\u0131", None))
        self.label_4.setText(QCoreApplication.translate("yemekekle", u"Yemek Tarifi", None))
        self.btn_guncelle.setText(QCoreApplication.translate("yemekekle", u"G\u00fcncelle", None))
        self.btn_sil.setText(QCoreApplication.translate("yemekekle", u"Sil", None))
        self.btn_getir.setText(QCoreApplication.translate("yemekekle", u"Getir", None))
        self.btn_yeni.setText(QCoreApplication.translate("yemekekle", u"Yeni", None))
        self.btn_kaydet.setText(QCoreApplication.translate("yemekekle", u"Kaydet", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("yemekekle", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("yemekekle", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("yemekekle", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("yemekekle", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("yemekekle", u"5", None));
    # retranslateUi

