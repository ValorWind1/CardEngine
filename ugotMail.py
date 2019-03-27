# import os
import smtplib
import config
from tkinter import messagebox
#
# EMAIL_ADDRESS = os.environ.get("skyjdani@gmail.com")
# EMAIL_PASSWORD = os.environ.get("rzwjaneemlbtivbv")
#
# with smtplib.SMTP("smtp.gmail.com":587 ) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#
#     smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
#
#     subject = " Card game Engine Welcomes you!"
#     body = "We are happy that you're using our engine!"
#
#     msg= f"Subject: {subject}\n\n{body}"
#
#     smtp.sendmail(EMAIL_ADDRESS, "skyjdani@gmail.com" ,msg)


def send_email(subject , msg ):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject:{}\n\n{}".format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print ("email failed to send")

def main():
    subject = " Card game Engine Welcomes you!"
    msg= " We are happy that you're using our engine!"
    send_email(subject,msg)
    messagebox.showinfo("Email Status:","Success: Email sent!")

if __name__ == '__main__':
    main()