from MailMessage import MailMessage


print("Started sending e-mail...")

obj_mail = MailMessage()

obj_mail.set_mail_template_file("templates/email_message.txt")

obj_mail.add_user("dries.raman.test@gmail.com", "Dries", 50.123456)
obj_mail.add_user("dries.raman.test@gmail.com", "Joris", 20.1)
obj_mail.add_user("dries.raman.test@gmail.com", "Dries", 60.56)

obj_mail.mail_messages()

print("done")
