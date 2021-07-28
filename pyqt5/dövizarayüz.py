import sys
import requests
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QTextEdit


def cev():
    url = "https://www.doviz.com/"

    first_currency = pencere.birinci_dvz.toPlainText()
    second_currency = pencere.ikinci_dvz.toPlainText()
    amount = int(pencere.miktar.toPlainText())

    response = requests.get(url)

    infos = response.json()

    firstValue = infos["rates"][first_currency]
    secondValue = infos["rates"][second_currency]
    sonuc = (secondValue / firstValue) * amount
    return str(sonuc)


class arayuz(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.bir = QLabel("birinci pb:")
        self.iki = QLabel("ikinci pb:")
        self.birinci_dvz = QTextEdit()
        self.ikinci_dvz = QTextEdit()
        self.buton = QPushButton("çevir")
        self.deger_yazi = QLabel("değer : ")
        self.deger = QTextEdit()
        self.miktar_yazi = QLabel("miktar:")
        self.miktar = QTextEdit()
        h_box = QHBoxLayout()
        h_box.addWidget(self.miktar_yazi)
        h_box.addWidget(self.miktar)
        h_box.addWidget(self.bir)
        h_box.addWidget(self.birinci_dvz)

        h_box.addWidget(self.iki)
        h_box.addWidget(self.ikinci_dvz)

        h_box.addWidget(self.buton)

        h_box.addWidget(self.deger_yazi)
        h_box.addWidget(self.deger)

        self.setGeometry(1000, 500, 100, 100)
        self.setLayout(h_box)
        self.setWindowTitle("döviz")
        self.show()
        self.buton.clicked.connect(self.cevir)

    def cevir(self):
        self.deger.setText(cev())


app = QApplication(sys.argv)

pencere = arayuz()

sys.exit(app.exec_())