import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp = smtplib.SMTP("smtp-mail.outlook.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("fourrunnersfourall@outlook.com", "4run4all")

msg = MIMEMultipart()
msg["From"] = "fourrunnersfourall@outlook.com"
msg["To"] = "evanlewis982@gmail.com"
msg["Subject"] = "Hi"
msg.attach(MIMEText("hey this is a test!"))

smtp.sendmail("fourrunnersfourall@outlook.com", "evanlewis982@gmail.com", msg.as_string())
smtp.quit()
