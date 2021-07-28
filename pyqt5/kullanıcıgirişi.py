import sys
import sqlite3
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglantiolustur()
        self.init_ui()
    def baglantiolustur(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler(kullanıcıadı TEXT,parola TEXT)")
        baglanti.commit()

    def init_ui(self):
        self.kullaniciadi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazialani = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullaniciadi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazialani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.show()
    def login(self):
        adi = self.kullaniciadi.text()
        par = self.parola.text()
        self.cursor.execute("Select * From üyeler Where kullanıcıadı = ? and parola = ?",(adi,par))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.yazialani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.yazialani.setText("Hoşgeldiniz" + adi)

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())