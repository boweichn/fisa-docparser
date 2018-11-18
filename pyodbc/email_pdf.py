from os import path, rename
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
    # Create database object
    db = retrive_dict()

    # Retreive list of pdf filenames
    files = find_pdf('./prepared_fact_sheets','pdf')

    # Setup email
    msg = MIMEMultipart()
    from_address = 'robertjanzenbc@gmail.com'
    msg['From'] = from_address
    msg['Subject'] = 'FISA BC Fact Sheet'
    body = 'Please electronically fill out the attached form, and return to FISA BC.'

    # Loop through all pdfs in the prepared_fact_sheets folder
    for f in files:
        # Find school name from pdf file name
        school_name = f.split("\\")[1].split(".")[0]
        for row in db:

            # Rename email_addr to: to_address for production
            email_addr = 'NA'
            if (school_name == row['SCHOOL']):
                try:
                    email_addr = row['Email']
                except:
                    print('Email address not found for: '+school_name)

                to_address = 'robertjanzenbc@gmail.com' # Remove this line for production
                msg['To'] = to_address
                break

        # Rename email_addr to: to_address for production
        if (email_addr == 'NA'):
            continue

        # Compose the rest of the email and attach the correct pdf
        # pdf names will be exactly the same as the school names in the database
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(f, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % f.split('\\')[1]) # Clean up file name
        msg.attach(part)

        # Send email, for Gmail you must enable "Allow less secure apps" in security settings
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)

            # Encryption is being used
            server.starttls()

            # Store gmail password in a separate text file called passwords.py
            server.login(from_address, EMAIL_PASS)
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()

            # Move pdf to completed folder
            attachment.close()
            rename(f, ".\\emailed_fact_sheets\\"+f.split('\\')[1])
        except Exception as e:
            print(e)

email_pdfs()
