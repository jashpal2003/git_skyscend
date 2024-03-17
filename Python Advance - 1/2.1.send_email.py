import smtplib
# from anup_password import MAIL_PASSWORD
# #
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# # # # # #
from email import encoders
from email.mime.base import MIMEBase
#
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#
server.login('anupdchavda@gmail.com', 'asdasfds')
#
sender = 'anupdchavda@gmail.com'
receiver = 'anup.chavda@skyscendbs.com'
# # # #
# message ="""
# Hi,
# How are you?
# Skyscend has many trainings to offer!
# www.skyscendbs.com"""
# #
# server.sendmail(sender, receiver, message)
# #
# server.quit()

#
# #
msg2 = MIMEMultipart()
print("MSG2", msg2)
msg = MIMEMultipart("")
print("MSG", msg)
msg['subject'] = 'Test Python Email - Attachment'
msg['From'] = sender
msg['To'] = receiver
# # msg['Cc']
# msg['Bcc']
# #
# #
text = """
Hi,
How are you?
Skyscend has many trainings to offer!
www.skyscendbs.com"""
#
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.skyscendbs.com/training">Skyscend Training</a>
       has many other trainings to offer as well.
        <br/>
       You can go through the attachment for <b>Python Material.</b>
    </p>
  </body>
</html>"""
# #
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
# # # #
msg.attach(part1)
msg.attach(part2)
# # #
filename = "Python.pdf"  # In same directory as script
# #
# # Open PDF file in binary mode
with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
#
encoders.encode_base64(part)
# # #
# # # # Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
# # # #
msg.attach(part)
# # # # #
server.sendmail(sender, receiver, msg.as_string())
#
            server.quit()
