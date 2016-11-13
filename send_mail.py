import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
addr_to   = input("Kellele kiri läheb? ")
addr_from = input("Kes kirja saadab? ")
 
smtp_server = "smtp.gmail.com"
smtp_user   = addr_from
smtp_pass   = getpass.getpass("Sisesta parool: ")

age = input("Kui vanaks kirja saaja saab? ")
msg = MIMEMultipart('alternative')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = age + ". hällipäev"

text = "Palun kasuta normaalset meilboksi."
html = """\
<html>
<head>
  <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <div class="email-background" style="max-width: 500px;background-color: #73f;text-align: center;font-family: sans-serif;color: rgba(255, 255, 255, 0.7);padding: 10px 20px;">
    <div class="pre-header" style="color: #73f;font-size: 1px;">
      Südamlikud ja musikaalsed õnnesoovid!
    </div>
    <div class="email-container" style="background: rgba(255, 255, 255, 0.1);border-radius: 5px;overflow: hidden;box-shadow: 0px 0px 15px 0px rgba(0, 0, 0, 0.5);">
      <h1 style="line-height: 1.3;">Kallis sõber!<br>
        Palju õnne!</h1>
      <img src="http://i.imgur.com/mEsGzqE.jpg" style="max-width: 100%;box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);">
      <p style="font-size: 18px;line-height: 1.4;">Olgu uus aasta soojem ja seksikam kui eelmine.</p>
      <div class="vid-button" style="padding: 10px;"> <a href="https://www.youtube.com/watch?v=TZJUjKTJt4o" style="text-decoration: none;font-size: 22px;display: inline block;background: #f51;color: rgba(255, 255, 255, 0.7);padding: 10px 20px;border-radius: 5px;">Vaata tervitusvideot!</a></div>
      <p style="font-size: 18px;line-height: 1.4;">Musi püksi!<br>
        Kaspar</p>
    </div>
  </div>
</body>
</html>
"""
 
part_plain = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
 
msg.attach(part_plain)
msg.attach(part_html)

try:
  server = smtplib.SMTP_SSL(smtp_server, 465)
  server.ehlo()
  server.login(smtp_user, smtp_pass)
  server.sendmail(addr_from, addr_to, msg.as_string())
  server.close()
  print("Saadetud!")
except:
  print("Midagi läks valesti.")