import smtplib

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= , password=)