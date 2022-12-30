import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from string import Template
import pandas as pd

e = pd.read_csv("FILE_NAME.csv")
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login('YOUREMAIL@gmail.com','YOURPASSWORD')
