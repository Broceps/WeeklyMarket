import smtplib


class EmailController:
    email_un = open("../_files/email_un.txt").read()
    email_pw = open("../_files/email_pw.txt").read()
    email_sender = "WeeklyMarketNews@gmail.com"
    email_recipient = "m.r.newsletter.demo@gmail.com"
    email_msg = "1"

    def email_sendout(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_un, email_pw)
        server.sendmail(email_sender, email_recipient, email_msg)
        server.quit()
