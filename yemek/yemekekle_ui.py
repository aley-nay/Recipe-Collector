# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musteriekle.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_yemekekle(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 631)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 581, 211))
        self.gridLayout_2 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit_dTarihi = QLineEdit(self.formLayoutWidget)
        self.lineEdit_dTarihi.setObjectName(u"lineEdit_dTarihi")

        self.gridLayout_2.addWidget(self.lineEdit_dTarihi, 7, 1, 1, 1)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.lineEdit_id = QLineEdit(self.formLayoutWidget)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_id, 0, 1, 1, 1)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_ad = QLineEdit(self.formLayoutWidget)
        self.lineEdit_ad.setObjectName(u"lineEdit_ad")

        self.gridLayout_2.addWidget(self.lineEdit_ad, 1, 1, 1, 1)

        self.lineEdit_tcno = QLineEdit(self.formLayoutWidget)
        self.lineEdit_tcno.setObjectName(u"lineEdit_tcno")

        self.gridLayout_2.addWidget(self.lineEdit_tcno, 6, 1, 1, 1)

        self.lineEdit_soyad = QLineEdit(self.formLayoutWidget)
        self.lineEdit_soyad.setObjectName(u"lineEdit_soyad")

        self.gridLayout_2.addWidget(self.lineEdit_soyad, 2, 1, 1, 1)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)

        self.pushButton_update = QPushButton(self.formLayoutWidget)
        self.pushButton_update.setObjectName(u"pushButton_update")

        self.gridLayout_2.addWidget(self.pushButton_update, 0, 2, 1, 1)

        self.pushButton_yeni = QPushButton(self.formLayoutWidget)
        self.pushButton_yeni.setObjectName(u"pushButton_yeni")

        self.gridLayout_2.addWidget(self.pushButton_yeni, 1, 2, 1, 1)

        self.pushButton_kaydet = QPushButton(self.formLayoutWidget)
        self.pushButton_kaydet.setObjectName(u"pushButton_kaydet")

        self.gridLayout_2.addWidget(self.pushButton_kaydet, 2, 2, 1, 1)

        self.pushButton_Getir2 = QPushButton(self.formLayoutWidget)
        self.pushButton_Getir2.setObjectName(u"pushButton_Getir2")

        self.gridLayout_2.addWidget(self.pushButton_Getir2, 6, 2, 1, 1)

        self.pushButton_sil = QPushButton(self.formLayoutWidget)
        self.pushButton_sil.setObjectName(u"pushButton_sil")

        self.gridLayout_2.addWidget(self.pushButton_sil, 7, 2, 1, 1)

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
        self.tableWidget.setGeometry(QRect(10, 210, 581, 401))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 606, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tc Kimlik NO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ad", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soyad", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Do\u011fum Tarihi", None))
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.pushButton_yeni.setText(QCoreApplication.translate("MainWindow", u"Yeni", None))
        self.pushButton_kaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.pushButton_Getir2.setText(QCoreApplication.translate("MainWindow", u"Getir", None))
        self.pushButton_sil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
    # retranslateUi

