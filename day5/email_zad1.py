import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = ''
smpt_port = 587
email_address = ''
password = ""
to = ""

wiadomosc = MIMEMultipart()
wiadomosc['From'] = email_address
wiadomosc['To'] = to
wiadomosc['Subject'] = "Dodatki"

tresc = "Ze szkolenia Comarch"
wiadomosc.attach(MIMEText(tresc, "plain"))

try:
    with smtplib.SMTP(smtp_server, smpt_port) as server:
        server.starttls()
        server.login(email_address, password)
        server.sendmail(email_address, to, wiadomosc.as_string())
        print("E-mail został wysłany")
except Exception as e:
    print(f"Błąd {e}")
