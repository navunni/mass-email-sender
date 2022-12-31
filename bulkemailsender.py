import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from string import Template
import pandas as pd

e = pd.read_csv("file_name.csv")
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login('youremail@gmail.com','yourpassword')


body = ("""

Hi there 

Body of the email 

Thank You
""")
subject = "Internship Opportunities"
fromaddr = 'navaneeth12245@gmail.com
for index, row in e.iterrows()
  
