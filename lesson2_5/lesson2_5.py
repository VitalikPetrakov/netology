"""Создать класс для работы с почтой;
Создать методы для отправки и получения писем;
Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
Переменные должны быть названы по стандарту PEP8;
Весь остальной код должен соответствовать стандарту PEP8;
Класс должен инициализироваться в конструкции. if __name__ == '__main__'"""

import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# GMAIL_SMTP = "smtp.gmail.com"
# GMAIL_IMAP = "imap.gmail.com"
#
# l = 'vitalik.petrakov123123@gmail.com'
# passwORD = 'Vp65852341'
# subject = 'Subject'
# recipients = ['vitalik.petrakov@mail.ru', 'vitalik.petrakov@gmail.com']
# message = 'Test message'
# header = None
#
#
# #send message
# msg = MIMEMultipart()
# msg['From'] = l
# msg['To'] = ', '.join(recipients)
# msg['Subject'] = subject
# msg.attach(MIMEText(message))
#
# ms = smtplib.SMTP(GMAIL_SMTP, 587)
# # identify ourselves to smtp gmail client
# ms.ehlo()
# # secure our email with tls encryption
# ms.starttls()
# # re-identify ourselves as an encrypted connection
# ms.ehlo()
#
# ms.login(l, passwORD)
# ms.sendmail(l, recipients, msg.as_string())
#
# ms.quit()
#send end


#recieve
# mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
# mail.login(l, passwORD)
# mail.list()
# mail.select("inbox")
# criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
# result, data = mail.uid('search', None, criterion)
# assert data[0], 'There are no letters with current header'
# latest_email_uid = data[0].split()[-1]
# result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
# raw_email = data[0][1]
# email_message = email.message_from_string(raw_email)
# mail.logout()
#end recieve


class SendMailer:
    def __init__(self, login, password, header=None):
        self.login = login
        self.password = password
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"
        self.header = header
        self.recipients = []

    def add_address_to_list_recipients(self, mail_address):
        self.recipients.append(mail_address)

    def make_massage(self, subject, message):
        self.message = message
        self.subject = subject
        self.message = MIMEMultipart()
        self.message['From'] = self.login
        self.message['To'] = ', '.join(self.recipients)
        self.message['Subject'] = self.subject
        self.message.attach(MIMEText(message))

    def send_massage(self):
        mail_send = smtplib.SMTP(self.gmail_smtp, 587)
        mail_send.ehlo()
        mail_send.starttls()
        mail_send.ehlo()
        mail_send.login(self.login, self.password)
        mail_send.sendmail(self.login, self.recipients, self.message.as_string())
        mail_send.quit()

    def get_mail(self):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        print(email_message)
        mail.logout()

if __name__ == '__main__':
    my_sendmailer = SendMailer('vitalik.petrakov123123@gmail.com', 'Vp65852341')
    my_sendmailer.add_address_to_list_recipients('vitalik.petrakov@mail.ru')
    my_sendmailer.add_address_to_list_recipients('vitalik.petrakov@gmail.com')
    my_sendmailer.make_massage('test massage from python', 'my massage from python=)')
    # my_sendmailer.send_massage()
    my_sendmailer.get_mail()