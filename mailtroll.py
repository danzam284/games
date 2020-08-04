import os
import smtplib
import imghdr
from email.message import EmailMessage
import re
import time
import random

#keep in mind, you must use a gmail for it to work properly

EMAIL_ADDRESS = 'ENTER EMAIL ADDRESS'
EMAIL_PASSWORD = 'ENTER EMAIL PASSWORD'
EMAIL_TO = 'ENTER EMAIL YOUR TROLLING'
mess = 1


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	while(1 < 2):
		a = str(random.randint(0, 900000))
		time.sleep(3)
		msg = EmailMessage()
		msg['Subject'] = a
		msg['From'] = EMAIL_ADDRESS
		msg.set_content('Hello')
		msg['To'] = EMAIL_TO	
		smtp.send_message(msg)
		print("Message " + str(mess) + " sent")
		mess = mess + 1