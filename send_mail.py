from smtplib import SMTP, SMTPAuthenticationError
#import smtplib


host = "smtp.gmail.com"
port = "587"
username = "dries.raman.test@gmail.com"
passwd = "YmN381uDfswT"

from_email = username # For readability only
to_email = [from_email] # For readability only

email_conn = SMTP(host,port)

email_conn.ehlo()
email_conn.starttls()

try:
    email_conn.login(username, passwd)
    email_conn.sendmail(from_email, to_email, "Test message.")
    print("Message sent...")
except SMTPAuthenticationError as e:
    print("Could not log in. Message was: '" + str(e.smtp_error) + "'")
except Exception as e:
    print("Some error occured. Message was: '" + str(e) + "'")

email_conn.quit()
