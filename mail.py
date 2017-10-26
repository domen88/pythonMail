#!/usr/bin/env python
#
# Mail sender.
#
# dscotece, msolimando
#

import commands
import smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText

def main():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    msg = MIMEMultipart()
    msg['From'] = 'x'
    msg['To'] = 'x'
    msg['Subject'] = 'INFRASAFE CHECK'

    server.login("x", "x")

    body = commands.getoutput('df')
    msg.attach(MIMEText(body, 'plain'))

    server.sendmail("x", "x", msg.as_string())
    server.quit()


if __name__ == "__main__":
    main()