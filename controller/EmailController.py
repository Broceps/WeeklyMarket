import smtplib


class EmailController:
    email_un = open("../_files/email_un.txt").read()
    email_pw = open("../_files/email_pw.txt").read()


    def email_sendout(self, email_recipient, email_msg):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.email_un, self.email_pw)
        server.sendmail(self.email_un, email_recipient, email_msg)
        server.quit()

email_recipient = "m.r.newsletter.demo@gmail.com"
email_msg = "2"

c = EmailController()
c.email_sendout(email_recipient, email_msg)
