import smtplib

#simple program to send email easily cerner_2^5_2020
server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # 465 is the port number
server.login('UserName email id', 'Password')
from_email_id = ''  #from email id /sender email id
to_email_id = ""  # to email Id ,It can be single email Id or List of email Id's
msg = 'Your text goes here or the message to be sent'
server.sendmail(from_email_id, to_email_id, msg)
server.quit()

# make sure to allow Allow less secure apps :ON of the sender email id  cerner_2^5_2020
