import smtplib
import ssl

host="smtp.gmail.com"
port=465
password = "niym jhbu vvqu vhoj"
userName = "shoham.kolan@gmail.com"
rec = "shoham.kolan@gmail.com"
msg = """\
Subject:How are you
I am fine
"""
context=ssl.create_default_context()
with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(userName,password)
    server.sendmail(userName,rec,msg)