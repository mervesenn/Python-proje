import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from PyQt5.QtWidgets import QWidget,QTextEdit,QLineEdit,QLabel,QPushButton,QHBoxLayout,QVBoxLayout,QApplication

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.kullaniciadi_l = QLabel("Kullanıcı Adı:")
        self.kullaniciadi = QLineEdit()
        self.alici_l = QLabel("Alıcı:")
        self.alici = QLineEdit()
        self.konu_l = QLabel("Konu:")
        self.konu = QLineEdit()
        self.yazi_l = QLabel("Mesaj:")
        self.yazi = QTextEdit()
        self.gonder = QPushButton("Gönder")
        self.parola_l = QLabel("Şifre:")
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)

        v_box = QVBoxLayout()
        v_box.addWidget(self.alici_l)
        v_box.addWidget(self.alici)
        v_box.addWidget(self.konu_l)
        v_box.addWidget(self.konu)
        v_box.addWidget(self.yazi_l)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.kullaniciadi_l)
        v_box.addWidget(self.kullaniciadi)
        v_box.addWidget(self.parola_l)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.gonder)

        self.setWindowTitle("Mail Programı")
        self.setGeometry(400,400,400,400)
        self.setLayout(v_box)
        self.show()
        self.gonder.clicked.connect(self.mailgonder)

    def mailgonder(self):
        mesaj = MIMEMultipart
        mesaj["From"] = self.kullaniciadi.text()
        mesaj["To"] = self.alici.text()
        mesaj["Subject"] = self.konu.text()
        mesajgovdesi = MIMEText(self.yazi.toPlainText(),"plain")
        mesaj.attach(mesajgovdesi)

        try:
            mail = smtplib.smtp("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.kullaniciadi.text(),self.parola.text())
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            mail.close()
        except:
            sys.stderr.write("Hata oluştu")
            sys.stderr.flush()


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
