import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = 'yourPassword'
SENDER = 'yourGmail@gmail.com'
RECEIVER = 'ReceiverEmail'

def send_email(file_path):
    print('Begin to send email')
    email_message = EmailMessage()
    email_message['Subject'] = 'New customer showed up!'
    email_message.set_content('Hey, we just saw a new customer!')

    with open(file_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    print('Email sent')
    gmail.quit()
