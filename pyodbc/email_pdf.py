from os import path
from glob import glob
from read_db import retrive_dict
from pprint import pprint
import smtplib

# Multi-purpose Internet Mail Extension
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Return list of all pdf files in folder
def find_pdf(dr, ext):
    return glob(path.join(dr,'*.{}'.format(ext)))

def email_pdfs():
    db = retrive_dict()
    files = find_pdf('.','pdf')
    fromaddr = 'robertjanzenbc@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = 'FISA BC Fact Sheet'


    for f in files:
        # Find school name from pdf file name
        school_name = f.split("\\")[1].split(".")[0]

        # toaddr
        msg['To'] =

email_pdfs()
