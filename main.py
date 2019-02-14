from MailMessage import MailMessage
import config


print("Started sending e-mail...")

obj_mail = MailMessage()

obj_mail.set_mail_template_file("templates/email_message.html")

user_email = config.MAIL_CONFIG["user"] + "@" + config.MAIL_CONFIG["domain"]

obj_mail.add_user(user_email, "Dries", 50.123456)
obj_mail.add_user(user_email, "Joris", 20.1)
obj_mail.add_user(user_email, "Robbe", 60.56)

obj_mail.mail_messages()

print("done")
