import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
email = "mervesen1095@gmail.com"
emailsifre = ""
mesaj ["From"] = "mervesen1095@gmail.com"
mailatilacaklar = ["mervesen1095@gmail.com"]
mesaj ["Subject"] = "Toplu mesaj"

yazi = """
smtp ile mesaj gönderme
"""
mesajgovdesi = MIMEText(yazi, "plain")
mesaj.attach(mesajgovdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("mervesen1095@gmail.com", "")
    
    for herbirmail in mailatilacaklar:
        mail.sendmail(mesaj["From"], herbirmail, mesaj.as_string())
        print("{} adresine mail gönderildi..")
    print("Mailler başarıyla gönderildi..")
    mail.close()
    
except:
    sys.stderr.write("Bir sorun oluştu...")
    sys.stderr.flush()
