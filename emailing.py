import smtplib , ssl
import os
from email.message import EmailMessage
import imghdr


def send_email(image_path):

    email_message = EmailMessage()
    email_message["Subject"] = "New Nigga detected"
    email_message.set_content("Yo bro we found a thief")

    with open(image_path,"rb") as file :
        content = file.read()
    email_message.add_attachment(content,maintype = "image" , subtype= imghdr.what(None,content))

    host = "smtp.gmail.com"
    port = 587
    gmail = smtplib.SMTP(host,port)

    username= "adishfab@gmail.com"
    reciever= "adishfab@gmail.com"
    password = os.getenv("Password of mail ..")
    "rpkl jynv gowk xjve"
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username,password)
    gmail.sendmail(username,reciever,email_message.as_string())
    print("Mail sent")
    gmail.quit()


# if __name__ == "__main__" :
    # send_email()