import smtplib
import imaplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import time

logging.basicConfig(filename="email_log.txt", level=logging.INFO)

SMTP_SERVER = "smtp.hostinger.com"
SMTP_PORT = 587
IMAP_SERVER = "imap.hostinger.com"
IMAP_PORT = 993
EMAIL = "#"
PASSWORD = "#"

SUBJECT = "Exclusive H-1B Opportunity with Tier II Product-Based Petitioner"
EMAIL_TEMPLATE = """
YOUR EMAIL TEMPLATE"""

# Shortened for brevity
PDF_PATH = r"DOCUMENT/PATH.pdf" //REPLACE "DOCUMENTS/PATH" WITH THE ACTUAL PATH
email_data = pd.read_csv(r"LEADS.CSV/PATH") //REPLACE "LEADS.CSV/PATH"WITH THE ACTUAL PATH




def send_email(recipient, first_name):
    message = MIMEMultipart()
    message["From"] = f"Career Catalyst Consulting <{EMAIL}>"
    message["To"] = recipient
    message["Subject"] = SUBJECT
    body = EMAIL_TEMPLATE.format(first_name=first_name)
    message.attach(MIMEText(body, "html"))

    try:
        with open(PDF_PATH, "rb") as pdf_file:
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(pdf_file.read())
            encoders.encode_base64(attachment)
            attachment.add_header("Content-Disposition", "attachment; filename=Career Catalyst Consulting Brochure.pdf")
            message.attach(attachment)
    except FileNotFoundError:
        print("Attachment not found.")
        return

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(message)
        print(f"Email sent to {recipient}")
       
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")


# Send emails
for _, row in email_data.iterrows():
    send_email(row["Email"], row["First Name"])
