# sending emails with attachments

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'uthmaanbreda@gmail.com'
receiver_email_id = ['thapelo@lifechoices.co.za', 'aaliyahjar13@gmail.com', 'abdulmalikmohamed360@gmail.com']
password = input("Enter your password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
# dot join adds the rest of the email addresses
msg['To'] = ', '.join(receiver_email_id)
msg['Subject'] = subject
body = "Hi FRIEND how are you. I am doing FINE thank you for asking!!!\n"
body = body + "How was the taxi/bus yesterday?"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(sender_email_id, password)

# message to be sent


# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)

# terminating the session
s.quit()
