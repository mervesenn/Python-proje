import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.filmismi = QPushButton("Film isimlerini getir")
        self.filmrating = QPushButton("Film ratinglerini getir")
        self.yazialani = QTextEdit()

        h_box = QHBoxLayout()
        h_box.addWidget(self.filmismi)
        h_box.addWidget(self.filmrating)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addWidget(self.yazialani)

        self.setWindowTitle("Filmler")
        self.setLayout(v_box)

        self.filmismi.clicked.connect(self.filmismiClick)
        self.filmrating.clicked.connect(self.filmratingClick)
        self.show()
    def filmismiClick(self):
        self.yazialani.clear()
        filmisimleri = soup.find_all("td",{"class":"titleColumn"})
        for i in filmisimleri:
            filmisimleri = i.find("a").text
            self.yazialani.insertPlainText(filmisimleri+"\n")
    def filmratingClick(self):
        self.yazialani.clear()
        filmratingleri = soup.find_all("td",{"class","ratingColumn imdbRating"})
        for i in filmratingleri:
            i = i.text
            i = i.strip()
            self.yazialani.insertPlainText(i+"\n")
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
