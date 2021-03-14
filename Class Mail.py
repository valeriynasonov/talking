import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class Mail():

    def __init__(self, login, password, smtp, imap):
        self.login = login
        self.password = password
        self.smtp = smtp
        self.imap = imap

    def send_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.passwоrd)
        ms.sendmail(ms.login, self, msg.as_string())
        ms.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        result, data = mail.uid('search', None, "All")
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

def mail_work(login, password, smtp, imap):
    mail = Mail(login, password, smtp, imap)
    while True:
        action = input("Если Вы хотите отправить письмо введите 1, если прочитать - 0")
        if action == 1:
            recipients = input("Укажите e-mail, на который хотите отправить письмо")
            subject = input("Введите заголовок письма")
            message = input("Введите текст сообщения")
            mail.send_message(recipients, subject, message)
        elif action == 2:
            mail.receive_message()

if __name__ == "__main__":
    login = input("Введите логин от Вашего электронного почтового ящика")
    password = input("Введите пароль от Вашей почты")
    server = input("Укажите сервер, на котором размещена Ваша почта")
    smtp = "smtp" + server
    imap = "imap" + server
    mail_work(login, password, smtp, imap)

