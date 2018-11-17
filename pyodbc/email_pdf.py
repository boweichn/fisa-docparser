from os import path
from glob import glob
from read_db import retrive_dict
from pprint import pprint
from passwords import *

# Multi-purpose Internet Mail Extension
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Return list of all pdf files in folder
def find_pdf(dr, ext):
    return glob(path.join(dr,'*.{}'.format(ext)))

def email_pdfs():
    db = retrive_dict()
    files = find_pdf('.','pdf')
    msg = MIMEMultipart()
    from_address = 'robertjanzenbc@gmail.com'
    msg['From'] = from_address
    msg['Subject'] = 'FISA BC Fact Sheet'
    body = 'Please electronically fill out the attached form, and return to FISA BC.'

    for f in files:
        # Find school name from pdf file name
        school_name = f.split("\\")[1].split(".")[0]
        for row in db:
            if (school_name == row['SCHOOL']):
                # Use this email address when testing is done
                # email_addr = row['Email']
                to_address = 'rjanzen20@my.bcit.ca'
                msg['To'] = to_address
                break

        # Compose the rest of the email and attach the correct pdf
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(f, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % f)
        msg.attach(part)

        # Send email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.ehlo()
            server.starttls()
            server.login(from_address, EMAIL_PASS)
            text = msg.as_string()
            server.sendmail(from_address, to_address)
            serer.quit()
        except:
            print('Unable to send email!')

email_pdfs()
