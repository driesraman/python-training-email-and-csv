from smtplib import SMTP, SMTPAuthenticationError # Import smtplib for the actual sending function
from email.message import EmailMessage # Import the email modules we'll need
from email.headerregistry import Address # Import the e-mail address module
import datetime
from TemplateRenderer import TemplateRenderer
import config

class MailMessage:

    ## #################################################################
    ##  PRIVATE ATTRIBUTES PART
    ## #################################################################

    _user_data = []
    _messages = []

    _from_email = Address(
        display_name = "Dries Raman",
        username = config.MAIL_CONFIG["user"],
        domain = config.MAIL_CONFIG["domain"]
    )

    _template_renderer = None


    ## #################################################################
    ##  CONSTRUCTOR PART
    ## #################################################################

    def __init__(self):
        self._template_renderer = TemplateRenderer()


    ## #################################################################
    ##  PUBLIC METHODS PART
    ## #################################################################

    ##
    #
    ##
    def add_user(self, email, name=None, total=0.00):
        data = {
            "email": email,
            "name": name.capitalize(),
            "total": "%.2f" %(total),
            "date": datetime.date.today().strftime("%d-%m-%Y")
        }

        self._user_data.append(data)


    ##
    #
    ##
    def get_user_data(self):
        return self._user_data

    ##
    #
    ##
    def set_mail_template_file(self, file):
        self._template_renderer.set_file(file)

    ##
    # BWEURK!!
    ##
    def make_messages(self):
        if len(self.get_user_data()) > 0:
            for data in self.get_user_data():
                message = {
                    "email": data["email"],
                    "message": self._template_renderer.render({
                        "name": data["name"],
                        "date": data["date"],
                        "total": data["total"]
                    })
                }
                self._messages.append(message)

            return self._messages

        return []

    ##
    # BWEURK!!!
    ##
    def mail_messages(self):
        # Generate the messages
        self.make_messages()

        # Check if there are mesages available
        if len(self._messages) < 1:
            return False

        try:
            # Create the SMT connection and connect
            email_conn = SMTP(config.MAIL_CONFIG["host"], config.MAIL_CONFIG["port"])

            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(config.MAIL_CONFIG["user"], config.MAIL_CONFIG["password"])

            # Send the mail messages
            for message in self._messages:
                msg = EmailMessage()

                msg.add_header("from", str(self._from_email))
                msg.add_header("to", message["email"])
                msg.add_header("subject", "[TEST] [TEST] [TEST]")
                msg.set_content("[TODO]")
                msg.add_alternative(message["message"], subtype='html')

                email_conn.send_message(msg)

            # Close the connection
            email_conn.quit()

            return True

        except SMTPAuthenticationError as e:
            print("Could not log in. Message was: '" + str(e.smtp_error) + "'")
        except Exception as e:
            print("Some error occured. Message was: '" + str(e) + "'")

        return False
