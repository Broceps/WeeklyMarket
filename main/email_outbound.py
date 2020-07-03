import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com,", 465)
server.login("WeeklyMarketNews@gmail.com", "WeeklyMarket2020")
server.sendmail("WeeklyMarketNews@gmail.com",
                "martin.eriksson7@outlook.com",
                "Do you see me...?")
server.quit()