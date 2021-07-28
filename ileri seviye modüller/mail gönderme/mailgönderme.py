import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
mesaj["From"] = "mervesen1095@gmail.com"
mesaj["To"] = "mervesen1095@gmail.com"
mesaj["Subject"] = "Smtp Mail Gönderme"
yazı = """
Smtp ile mail gönderiyorum.
Merve Şen
"""

mesajgövdesi = MIMEText(yazı,"plain")
mesaj.attach(mesajgövdesi)
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("mervesen1095@gmail.com","")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail başarıyla gönderildi.")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()

