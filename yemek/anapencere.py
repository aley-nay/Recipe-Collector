import sys
import pyodbc
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox

from ui_form import Ui_anapencere
from ui_yemekekle import Ui_yemekekle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_anapencere()
        self.ui.setupUi(self)
        self.ui.btn_panel.clicked.connect(self.veritabani_baglantisi)

        self.setWindowTitle("Yöre Yöre / Yiye Yiye")
        self.getir_yemek2()  # anasayfada çağır

    def veritabani_baglantisi(self):
        server = 'DESKTOP-0G2M7JA\SQLEXPRESS'
        database = 'yemekler_db'
        username = 'aleyna'
        password = '123'

        # MSSQL veritabanına bağlan
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              f'SERVER={server};'
                              f'DATABASE={database};'
                              f'UID={username};'
                              f'PWD={password}')

        # Bağlantı üzerinden bir cursor oluştur
        cursor = conn.cursor()
        self.w = yemekgirWindow(self, cursor)
        self.w.show()

    def getir_yemek2(self):
        try:
            server = 'DESKTOP-0G2M7JA\SQLEXPRESS'
            database = 'yemekler_db'
            username = 'aleyna'
            password = '123'
            # veritabanı bağlantısı
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  f'SERVER={server};'
                                  f'DATABASE={database};'
                                  f'UID={username};'
                                  f'PWD={password}')

            # cursor oluştur
            cursor = conn.cursor()

            # yemek tablosundaki her şeyi seç
            query = "SELECT * FROM yemek"
            cursor.execute(query)

            # sütun adlarını al
            sutun = [column[0] for column in cursor.description]

            # tableWidgettan sütun adları al
            self.ui.tableWidget.setColumnCount(len(sutun))
            self.ui.tableWidget.setHorizontalHeaderLabels(sutun)

            # sorgu sonucundaki satırları, tableWidgeta yerleştir
            self.ui.tableWidget.setRowCount(0)
            for row_index, row_data in enumerate(cursor.fetchall()):
                self.ui.tableWidget.insertRow(row_index)
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tableWidget.setItem(row_index, col_index, item)

            sutun_genislik = [30, 80, 150, 150, 150, 150]  # tableWidgettaki sütunların genişliği
            for col_index, width in enumerate(sutun_genislik):
                self.ui.tableWidget.setColumnWidth(col_index, width)
        finally:
            cursor.close()
            conn.close()

#panel sayfası
class yemekgirWindow(QMainWindow):
    def __init__(self, mainWindow, mycursor, parent=None):
        super().__init__(parent)
        self.ui = Ui_yemekekle() #yemekekle.py'daki class
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint) #sekme/tab üstündeki küçült, büyült, kapat işaretleri
        self.mainWindow = mainWindow
        self.cursor = mycursor

        self.setWindowTitle("Yöre Yöre / Yiye Yiye")
        #x butona tıklayınca x fonksiyonu çalıştır
        self.ui.btn_guncelle.clicked.connect(self.guncelle_yemek)
        self.ui.btn_yeni.clicked.connect(self.yeni_yemek)
        self.ui.btn_kaydet.clicked.connect(self.kaydet_yemek)
        self.ui.btn_getir.clicked.connect(self.getir_yemek)
        self.ui.btn_sil.clicked.connect(self.sil_yemek)
        self.getir_yemek()

    def kaydet_yemek(self):
        yemek_id = self.ui.yemek_id.text()
        yemek_turu = self.ui.yemek_turu.text()
        yemek_yoresi  = self.ui.yemek_yoresi.text()
        yemek_adi = self.ui.yemek_adi.text()
        yemek_tarifi = self.ui.yemek_tarifi.toPlainText()

        if not yemek_id or not yemek_turu or not yemek_yoresi or not yemek_adi or not yemek_tarifi:
            QMessageBox.warning(self, "Uyarı", "Tüm alanları doldurun.")
            return

        try:
            server = 'DESKTOP-0G2M7JA\SQLEXPRESS'
            database = 'yemekler_db'
            username = 'aleyna'
            password = '123'
            # MSSQL veritabanına bağlan
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  f'SERVER={server};'
                                  f'DATABASE={database};'
                                  f'UID={username};'
                                  f'PWD={password}')
            cursor = conn.cursor()

            # Ekleme işlemi
            query = "INSERT INTO yemek (id, yemek_turu, yemek_yoresi, yemek_adi, yemek_tarifi) VALUES (?, ?, ?, ?, ?)" #veritabanı= injectiona karşı koruma
            cursor.execute(query, (yemek_id, yemek_turu, yemek_yoresi, yemek_adi, yemek_tarifi)) #lineedit değişkenler kullanıcıdan gelen
            conn.commit()  #veritabanına kaydet
            QMessageBox.information(self, "Başarı", "yemek başarıyla kaydedildi.")
            self.getir_yemek()
        except pyodbc.Error as e:
            print(f'Hata: {e}')
            QMessageBox.critical(self, "Hata", "yemek kaydetme hatası.")

    def guncelle_yemek(self):
        try:
            server = 'DESKTOP-0G2M7JA\SQLEXPRESS'
            database = 'yemekler_db'
            username = 'aleyna'
            password = '123'
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  f'SERVER={server};'
                                  f'DATABASE={database};'
                                  f'UID={username};'
                                  f'PWD={password}')
            cursor = conn.cursor()
            yemek_id = self.ui.yemek_id.text()
            yemek_turu = self.ui.yemek_turu.text()
            yemek_yoresi  = self.ui.yemek_yoresi.text()
            yemek_adi = self.ui.yemek_adi.text()
            yemek_tarifi = self.ui.yemek_tarifi.toPlainText()

            if not yemek_id:
                QMessageBox.warning(self, "Uyarı", "Lütfen bir yemek ID girin.")
                return

            # Güncelleme işlemi
            query = "UPDATE yemek SET yemek_turu=?, yemek_yoresi=?, yemek_adi=?, yemek_tarifi=? WHERE id=?" #veritabanı= injectiona karşı koruma
            cursor.execute(query, (yemek_turu, yemek_yoresi, yemek_adi, yemek_tarifi, yemek_id)) #lineedit değişkenler kullanıcıdan gelen
            conn.commit() #veritabanına kaydet
            QMessageBox.information(self, "Başarı", "yemek bilgileri başarıyla güncellendi.")
            self.getir()

        except pyodbc.Error as e:
            print(f'Hata: {e}')
            QMessageBox.critical(self, "Hata", "yemek bilgileri güncelleme hatası.")

        finally:
            cursor.close()
            conn.close()


    def yeni_yemek(self):
        pass

    def getir_yemek(self):
        try:
            server = 'DESKTOP-0G2M7JA\SQLEXPRESS'
            database = 'yemekler_db'
            username = 'aleyna'
            password = '123'
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  f'SERVER={server};'
                                  f'DATABASE={database};'
                                  f'UID={username};'
                                  f'PWD={password}')
            cursor = conn.cursor()
            query = "SELECT * FROM yemek"
            cursor.execute(query)
            sutun = [column[0] for column in cursor.description] #veritabanındaki sütun adlarını çeken sorgu
            self.ui.tableWidget.setColumnCount(len(sutun))  #tablewidgetin sütun sayısı, veritabanındaki sütun sayısına eşitle
            self.ui.tableWidget.setHorizontalHeaderLabels(sutun) #sorgudan gelen sütun adlarını, tablewidget'ın sütun başlıkları yap
            self.ui.tableWidget.setRowCount(0) #sütun sayısını sıfırlar, yeni sütun sayıları eklemek için
            for row_index, row_data in enumerate(cursor.fetchall()): #veritabanındaki sütunları çek
                self.ui.tableWidget.insertRow(row_index) #sorgudaki satır kadar tableWidgeta yeni satır ekler
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data)) #her sütun için yeni bir tableWidgetitem oluştur
                    self.ui.tableWidget.setItem(row_index, col_index, item) #hücrelere yerleştirme

            sutun_genislik = [30, 80, 150, 150, 150, 150] #px olarak genişlik
            for col_index, width in enumerate(sutun_genislik):
                self.ui.tableWidget.setColumnWidth(col_index, width)
        finally:
            cursor.close()
            conn.close()

    def sil_yemek(self):
        try:
            server = 'DESKTOP-0G2M7JA\SQLEXPRESS'
            database = 'yemekler_db'
            username = 'aleyna'
            password = '123'
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  f'SERVER={server};'
                                  f'DATABASE={database};'
                                  f'UID={username};'
                                  f'PWD={password}')
            cursor = conn.cursor()
            secili_veri = self.ui.tableWidget.currentRow() #currentRow seçili olan veri

            if secili_veri == -1: #hiçbir veri seçilmemişse
                QMessageBox.warning(self, "Uyarı", "Lütfen silmek istediğiniz satırı seçin.")
                return

            yemek_id = self.ui.tableWidget.item(secili_veri, 0).text() #id sütunundaki veriyi al

            self.ui.tableWidget.removeRow(secili_veri) #seçilen satırı kaldırıp tableWidgetı günceller
            query = "DELETE FROM yemek WHERE id=?" #yemek tableından sil
            cursor.execute(query, (yemek_id,))
            conn.commit() #veritabanına kaydet
            QMessageBox.information(self, "Başarı", "yemek bilgileri başarıyla silindi.")

        except pyodbc.Error as e:
            print(f'Hata: {e}')
            QMessageBox.critical(self, "Hata", "yemek bilgileri silme hatası.")

        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
