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
EMAIL = "pranita@careercatalystconsulting.in"
PASSWORD = "Mangalbatuk0202#"

SUBJECT = "Exclusive H-1B Opportunity with Tier II Product-Based Petitioner"
EMAIL_TEMPLATE = """
<div style="font-size: 10pt; font-family: Verdana,Geneva,sans-serif;">
<div id="v1_rc_sig"><br />
<p>&nbsp;</p>
<table style="max-width: 600px; margin: 0 auto; padding: 10px; background-color: #ffff; border-radius: 10px; box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.1);" border="0" width="100%" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td style="text-align: center; padding-bottom: 20px; border-bottom: 1px solid #eee; border-radius: 5px;"><img style="width: 580px; height: 200px; border-radius: 5px;" src="https://raw.githubusercontent.com/Shourya-8416/Carrier-Catalyst/refs/heads/main/Untitled%20design%20(4).jpg" alt="CCGC" width="580" height="326" /></td>
</tr>
<tr>
<td style="padding: 20px; color: #000000;">
<div><span style="font-size: 13.3333px;">&nbsp;</span></div>
<div><span style="font-size: 13.3333px;">Dear {first_name},</span></div>
<div><span style="font-size: 13.3333px;">&nbsp;</span></div>
<div><span style="font-size: 13.3333px;">We are reaching out as you recently enquired with us through our ad about H-1B sponsorship opportunities. At <strong>Career Catalyst Global Consulting(CCGC)</strong>, we specialize in <strong>H-1B Sourcing and Consulting</strong>, with a proven track record of <strong>130+ CAP approvals across 15 verified U.S.-based petitioners</strong>.</span></div>
<div><span style="font-size: 13.3333px;">&nbsp;</span></div>
<div><span style="font-size: 13.3333px;"><strong>What&rsquo;s New?</strong></span></div>
<div><span style="font-size: 13.3333px;">Enrollments are now open for H-1B nominations with our newly added <strong>Tier II product-based petitioner</strong>, offering excellent deliverables and unmatched quality.</span></div>
<div><span style="font-size: 13.3333px;">&nbsp;</span></div>
<div><span style="font-size: 13.3333px;"><strong>Why Choose CCGC?</strong></span></div>
<ul>
<li><span style="font-size: 13.3333px;">Work with <strong>top-tier petitioners</strong> known for successful H-1B filings.</span></li>
<li><span style="font-size: 13.3333px;">Comprehensive <strong>support throughout the process</strong>.</span></li>
<li><span style="font-size: 13.3333px;">Limited slots available on a <strong>first-come, first-served basis</strong>.</span></li>
</ul>
<div><span style="font-size: 13.3333px;"><strong>How to Get Started?</strong></span></div>
<ul>
<li><span style="font-size: 13.3333px;">Share your <strong>resume with us for eligibility evaluation at</strong> <a href="mailto:info@careercatalystconsulting.in" rel="noreferrer">info@careercatalystconsulting.in</a>.</span></li>
<li><span style="font-size: 13.3333px;">Attend one of our <strong>exclusive webinars</strong> to learn about the H-1B process and our offerings.</span></li>
</ul>
<div><span style="font-size: 13.3333px;">&nbsp;</span></div>
<div><span style="font-size: 13.3333px;">We look forward to assisting you in achieving your career goals.</span></div>
<p><span style="font-size: 10pt;">You can connect with us on the below mentioned numbers.</span></p>
<ul>
<li><span style="font-size: 10pt;">Pranita&nbsp; &nbsp; &nbsp; :&nbsp; +918928794435</span></li>
<li><span style="font-size: 10pt;">Raj&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :&nbsp; +919198530196</span></li>
</ul>
<p><span style="font-size: 10pt;">Join our H-1B WhatsApp Channel for the latest updates and client testimonies!</span></p>
<div style="text-align: center; margin-bottom: 20px;"><a style="display: inline-block; padding: 12px 24px; background-color: #0c4642; color: #fff; text-decoration: none; border-radius: 5px;" href="https://whatsapp.com/channel/0029VagKcf14NVih9Gh3ko0a" target="_blank" rel="noopener noreferrer">Join WhatsApp Channel</a></div>
<div><span style="font-size: 13.3333px;">Our webinars are held  <strong>Everyday at 9 PM IST</strong>. This is your chance to ask questions, understand the process, and take the next step toward your H-1B nomination.</span></div>
&nbsp;
<div style="text-align: center; margin-bottom: 20px;"><a style="display: inline-block; padding: 12px 24px; background-color: #0c4642; color: #fff; text-decoration: none; border-radius: 5px;" href="https://us05web.zoom.us/j/87139389958" target="_blank" rel="noopener noreferrer">Join Zoom Meeting</a></div>
<p><span style="font-size: 10pt;">We look forward to e-meet you.</span></p>
<div style="text-align: left; font-family: Verdana, Geneva, sans-serif; font-size: 10pt; color: #000; margin-bottom: 20px;">
<div style="display: flex; align-items: center;">
<div style="margin-right: 10px;"><img style="width: 100px; height: 100px; vertical-align: middle;" src="https://raw.githubusercontent.com/Shourya-8416/Carrier-Catalyst/refs/heads/main/Calendar.png" alt="Calendar Icon" /></div>
<div>
<p style="margin: 0; font-weight: bold;">Date &amp; time</p>
<p style="margin: 0;">Everyday &nbsp; 9:00 PM - 10:30 PM (GMT+5:30)</p>
<div style="margin-top: 10px;"><span>Add to :</span>  <a href="https://www.google.com/calendar/render?action=TEMPLATE&text=H-1B+Process+Webinar&dates=20250110T153000Z/20250110T170000Z&details=Learn+about+the+H-1B+process%2C+application+steps%2C+and+get+your+queries+answered+in+an+interactive+Q%26A+session.+Join+the+meeting+via+Zoom+at+https://us05web.zoom.us/j/87139389958&location=Online+via+Zoom&recur=RRULE:FREQ=DAILY&sf=true&output=xml" 
       target="_blank" 
       style="margin-right: 10px; text-decoration: none; font-size: 12px; color: #0072c6;">Google</a>
    <a href="https://outlook.live.com/calendar/0/deeplink/compose?path=/calendar/action/compose&rru=addevent&startdt=2025-01-10T15:30:00.000Z&enddt=2025-01-10T17:00:00.000Z&subject=H-1B+Process+Webinar&location=Online+via+Zoom&body=Learn+about+the+H-1B+process%2C+application+steps%2C+and+get+your+queries+answered+in+an+interactive+Q%26A+session.+Join+the+meeting+via+Zoom+at+https://us05web.zoom.us/j/87139389958&rrule=RRULE:FREQ=DAILY" 
       target="_blank" 
       style="margin-right: 10px; text-decoration: none; font-size: 12px; color: #0072c6;">Outlook</a>
    <a href="data:text/calendar;charset=utf8,BEGIN:VCALENDAR%0AVERSION:2.0%0ABEGIN:VEVENT%0AUID:unique-id%0ADTSTAMP:20250110T153000Z%0ADTSTART:20250110T153000Z%0ADTEND:20250110T170000Z%0ARRULE:FREQ=DAILY%0ASUMMARY:H-1B+Process+Webinar%0ADESCRIPTION:Learn+about+the+H-1B+process%2C+application+steps%2C+and+get+your+queries+answered+in+an+interactive+Q%26A+session.+Join+the+meeting+via+Zoom+at+https://us05web.zoom.us/j/87139389958%0ALOCATION:Online+via+Zoom%0AEND:VEVENT%0AEND:VCALENDAR" 
       download="H-1B_Process_Webinar_Recurring.ics" 
       target="_blank" 
       style="margin-right: 10px; text-decoration: none; font-size: 12px; color: #0072c6;">iCal</a>
    <a href="https://calendar.yahoo.com/?v=60&view=d&title=H-1B+Process+Webinar&st=20250110T210000Z&et=20250110T223000Z&desc=Learn+about+the+H-1B+process%2C+application+steps%2C+and+get+your+queries+answered+in+an+interactive+Q%26A+session.+Join+the+meeting+via+Zoom+at+https://us05web.zoom.us/j/87139389958&in_loc=Online+via+Zoom&recur=RRULE:FREQ=DAILY" 
       target="_blank" 
       style="text-decoration: none; font-size: 12px; color: #0072c6;">Yahoo</a>
</div>
</div>
</div>
<div style="text-align: center; color: red;"><span style="font-size: 13.3333px;"><strong>Act quickly&mdash;slots are filling fast!</strong></span></div>
<p><span style="font-size: 10pt;"><strong>Best Regards,</strong></span><span style="font-size: 10pt;"></span><br /><strong>Pranita Jajodia</strong></p>
<p><span style="font-size: 10pt;"><strong>Career Catalyst Global Consulting India Pvt LTD</strong> </span><br /><span style="font-size: 10pt;"><strong>Phone :</strong> +918928794435/+919198530196 </span><br /><span style="font-size: 10pt;"><strong>E-mail :</strong> <a href="mailto:info@careercatalystconsulting.in" rel="noreferrer">info@careercatalystconsulting.in</a> </span><br /><span style="font-size: 10pt;"><strong>Website :</strong> <a href="https://careercatalystconsulting.in" target="_blank" rel="noopener noreferrer">https://careercatalystconsulting.in</a> </span><br /><span style="font-size: 10pt;"></span> <span style="font-size: 10pt;"><strong>Headquarters :</strong> Borivali (W), Mumbai-400092 </span></p>
<h2 style="text-align: center;">Please visit our website!</h2>
<div style="text-align: center; margin-bottom: 20px;"><a style="margin-right: 10px;" href="https://careercatalystconsulting.in/" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/Shourya-8416/Carrier-Catalyst/refs/heads/main/WhatsApp%20Image%202024-10-18%20at%2018.55.42_52f79c2b.jpg" alt="CCGC" width="40" height="40" /></a></div>
</td>
</tr>
<tr>
<td style="padding-top: 20px; border-top: 1px solid #eee; background-color: #0c4642; color: #fff; text-align: center; border-radius: 5px;">
<p>Follow us on social media:</p>
<div style="margin-bottom: 10px;"><a style="margin-right: 10px;" href="https://www.facebook.com/careercatalystglobalconsulting" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/Shourya-8416/Carrier-Catalyst/refs/heads/main/facebook%20(4).png" alt="Facebook" width="40" height="40" /></a> <a style="margin-right: 10px;" href="https://www.linkedin.com/company/careercatalystin/" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/Shourya-8416/Carrier-Catalyst/refs/heads/main/linkedin%20(1).png" alt="LinkedIn" width="40" height="40" /></a> <a href="https://www.instagram.com/careercatalystin/" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/Shourya-8416/Carrier-Catalyst/refs/heads/main/instagram%20(2).png" alt="Instagram" width="40" height="40" /></a></div>
<p>&copy; 2024 CareerCatalystGlobalConsulting. All rights reserved.</p>
</td>
</tr>
</tbody>
</table>
</div>
</div>"""

# Shortened for brevity
PDF_PATH = r"C:\Users\shourya\OneDrive\Desktop\Email Script\Career Catalyst Consulting Brochure.pdf"
email_data = pd.read_csv(r"C:\Users\shourya\OneDrive\Desktop\Email Script\Extra_new(09-01-2025).csv")




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