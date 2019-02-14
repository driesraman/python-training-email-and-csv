from MailMessage import MailMessage
from CsvReader import CsvReader
import config


## Read the users from a csv file
print("Started reading user file...")

obj_users = CsvReader()
obj_users.set_file("user_data.csv")
obj_users.load_data()

print("Done!")


# Send the e-mails to the users
print("Started sending e-mail...")

obj_mail = MailMessage()

obj_mail.set_mail_template_file("templates/email_message.html")

for user_data in obj_users.get_data():
    obj_mail.add_user(user_data["email"], user_data["first_name"], user_data["total"])


#user_email = config.MAIL_CONFIG["user"] + "@" + config.MAIL_CONFIG["domain"]
#
#obj_mail.add_user(user_email, "Dries", 50.123456)
#obj_mail.add_user(user_email, "Joris", 20.1)
#obj_mail.add_user(user_email, "Robbe", 60.56)

obj_mail.mail_messages()

print("done")
