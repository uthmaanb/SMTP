# basic email


import smtplib
# please note go to https://myaccount.google.com/lesssecureapps and
# turn it off to allow gmail to send
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'uthmaanbreda@gmail.com'
receiver_email_id = input("Enter receiver's email: ")
password = input("Enter senders email password: ")
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent
message = "Hi FRIEND how are you. I am doing FINE thank you for asking!!!\n"
message = message + "How was the taxi/bus yesterday?"
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()
