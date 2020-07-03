import smtplib
from email.message import EmailMessage



class EmailController:
    email_un = open("../_files/email_un.txt").read()
    email_pw = open("../_files/email_pw.txt").read()

    def email_sendout(self, header, msg, recipient):
        msg_template = """Subject: Your weekly update on {0}! \n{1}"""
        msg_final = msg_template.format(header,msg)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.email_un, self.email_pw)
        server.sendmail(self.email_un, [recipient], msg_final)
        server.quit()













