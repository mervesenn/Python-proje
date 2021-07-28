import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.checkbox = QCheckBox("Python'u seviyor musunuz?")
        self.yazialani = QLabel()
        self.buton = QPushButton("Bana tıkla")
        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.setWindowTitle("Check Box")
        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazialani))
        self.show()
    def click(self,checkbox,yazialani):
        if checkbox:
            yazialani.setText("Python'ı seviyorsun çok güzel")
        else:
            yazialani.setText("Neden sevmiyorsun?")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())