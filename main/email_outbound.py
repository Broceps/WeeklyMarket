import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("weeklymarketnews@gmail.com", "WeeklyMarket2020")
server.sendmail("WeeklyMarketNews@gmail.com",
                "m.r.newsletter.demo@gmail.com",
                "Do you see me...?")
server.quit()