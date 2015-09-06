# Import smtplib for the actual sending function

import smtplib

# Import the email modules we'll need

from email.mime.text import MIMEText

#define variables

textfile = 'lyric.txt'
smtp_server = 'smtp.gmail.com'
me = 'sky22357168@gmail.com'
you = 'sky22357168@gmail.com'


# Open a plain text file for reading.  For this example, assume that

# the text file contains only ASCII characters.

fp = open(textfile, 'rb')
# Create a text/plain message

msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address

# you == the recipient's email address

msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me  
msg['To'] = you 

# Send the message via our own SMTP server, but don't include the

# envelope header.

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login("你的帳號", "你的密碼")
s.sendmail(me, [you], msg.as_string())
s.quit()
