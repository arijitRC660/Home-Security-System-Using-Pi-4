import imaplib




def readMail(offset) : 
    val = 'U'
    
    Grant = str(offset)+" Grant"
    Deny = str(offset)+" Deny"

    MY_EMAIL= "your_MAIL-ID@gmail.com"
    EMAIL_PWD = "your_mail_password" #password for email 
    SMTP_SERVER = "imap.gmail.com"  #server for email inbox
    SMTP_PORT = 993


    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(MY_EMAIL,EMAIL_PWD)
    mail.list()
    mail.select('inbox')
    #'(FROM "Arijit Roy Chowdhury" SUBJECT "1")'


 
    print("Reading mails....")
   
    
    try : 
     result, data = mail.search(None, '(FROM "Name Assigned with your mail-ID| example- Jhon paul" SUBJECT "Alert!!!")' )

     ids = data[0] # data is a listy
     id_list = ids.split() # ids is a space separated string
     latest_email_id = id_list[-1] # get the latest

     result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822)             for the given ID

     raw_email = data[0][1]
     msg = raw_email.decode()
    
     if Grant in msg : 
         val = 'G'
     elif Deny in msg : 
         val = 'D'

    except  : 
     #if there is any kind of delay or anykind of connectivity issues
     print("Something Went wrong")
     
        
       
    return val

