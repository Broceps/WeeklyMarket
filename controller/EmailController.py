import smtplib
from email.message import EmailMessage



class EmailController:
    email_un = open("../_files/email_un.txt").read()
    email_pw = open("../_files/email_pw.txt").read()
    email_recipient = "m.r.newsletter.demo@gmail.com"

    def email_sendout(self):
        msg = """Subject: One More Time! \n
Ahri must go on!"""

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.email_un, self.email_pw)
        server.sendmail(self.email_un, [self.email_recipient], msg)
        server.quit()


c = EmailController()
c.email_sendout()













