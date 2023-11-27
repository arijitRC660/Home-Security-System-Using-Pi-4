#sending messages using ttls encryption 
import os
import imghdr
import smtplib
from email.message import EmailMessage

import random

#for the email address
def sendMail(counter:int) :
    offset = random.randint(1, 100)
    user = "your-mail-id@gmail.com"
    password = "mail password"
    receiver = 'mail of the receiver'

    

#for image attachment
    
    with open("./temp_faces/Person" + str(counter) + ".jpg", 'rb') as f : 
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

#setting up EmailMessage class for sending mail
    msg = EmailMessage() 
    msg['Subject'] = 'Alert!!!'
    msg['From'] = user
    msg['To'] = receiver

    c = str(offset)
    msg.set_content('Unknown person detected.'+'\nOffset value: '+str(offset)+'\nReply within 5 Minutes...')


    msg.add_attachment(file_data , maintype='image', subtype=file_type, filename=file_name)




    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
 
    #for login 
        smtp.login(user , password)

    #the secong mail id will be for the receiver
        smtp.send_message(msg)

    print(" An unknown person detected")
    print(" Mail has send successfully!!") 

    #value  = readMail_SSL.readMail(offset)

    os.remove("./temp_faces/Person" + str(counter) + ".jpg")

    return offset




