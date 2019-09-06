import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMailer:
    def __init__(self, login, password, header=None):
        self.message = MIMEMultipart()
        self.login = login
        self.password = password
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"
        self.header = header
        self.recipients = []

    def add_address_to_list_recipients(self, mail_address):
        self.recipients.append(mail_address)

    def make_massage(self, subject, text):
        self.message['From'] = self.login
        self.message['To'] = ', '.join(self.recipients)
        self.message['Subject'] = subject
        self.message.attach(MIMEText(text))

    def send_massage(self):
        mail_send = smtplib.SMTP(self.gmail_smtp, 587)
        mail_send.ehlo()
        mail_send.starttls()
        mail_send.ehlo()
        mail_send.login(self.login, self.password)
        mail_send.sendmail(self.login, self.recipients,
                           self.message.as_string())
        mail_send.quit()

    def get_mail(self):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        if self.header:
            criterion = f'(HEADER Subject "{self.header}")'
        else:
            criterion = f'(HEADER Subject "All")'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = str(data[0][1])
        email_message = email.message_from_string(raw_email)
        print(email_message)
        mail.logout()


if __name__ == '__main__':
    my_sendmailer = SendMailer('vitalik.petrakov123123@gmail.com',
                               'Vp65852341')
    my_sendmailer.add_address_to_list_recipients('vitalik.petrakov@mail.ru')
    my_sendmailer.add_address_to_list_recipients('vitalik.petrakov@gmail.com')
    my_sendmailer.make_massage('test massage from python',
                               'my massage from python=)')
    # my_sendmailer.send_massage()
    my_sendmailer.get_mail()
