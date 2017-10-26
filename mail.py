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

    fr = 'x'
    to = 'x'

    msg = MIMEMultipart()
    msg['From'] = fr
    msg['To'] = to
    msg['Subject'] = 'INFRASAFE CHECK'

    server.login("x", "x")

    body = commands.getoutput('df')
    msg.attach(MIMEText(body, 'plain'))

    server.sendmail(fr, to, msg.as_string())
    server.quit()


if __name__ == "__main__":
    main()