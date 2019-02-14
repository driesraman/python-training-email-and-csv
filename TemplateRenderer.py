import os

class TemplateRenderer:


    ## #################################################################
    ##  PRIVATE ATTRIBUTES PART
    ## #################################################################

    _template_file = None
    _template_content = None


    ## #################################################################
    ##  GET AND SET PART
    ## #################################################################

    ##
    #
    ##
    def get_template_file(self):
        return self._template_file

    ##
    #
    ##
    def set_template_file(self, file):
        # Make the path system (windows, mac, linux) independent
        # and make it relative to the current working directory
        local_file = os.path.join(os.getcwd(), file)

        # Verify the fileexists
        if not os.path.isfile(local_file):
            raise FileNotFoundError("Template file '%s' not found" %(local_file))

        # set the file
        self._template_file = local_file

        # Reset the template contents
        self._reset_template_content()


    ## #################################################################
    ##  PUBLIC METHODS PART
    ## #################################################################

    ##
    #
    ##
    def render(self, content):
        if self._template_content == None:
            self._load_template()

        return self._template_content.format(**content)


    ## #################################################################
    ##  PRIVATE METHODS PART
    ## #################################################################

    ##
    #
    ##
    def _load_template(self):
        if self.get_template_file() == None:
            raise RuntimeError("No template file provided.")

        self._template_content = open(self.get_template_file()).read()

    ##
    #
    ##
    def _reset_template_content(self):
        self._template_content = None



############################
# TEST TEST TEST
############################

# obj = TemplateRenderer()
# obj.set_template_file("templates/email_message.txt")
# print(
#     obj.render(
#         {
#             "name": "Dries",
#             "date": "2018-01-01",
#             "total": 0.12
#         }
#     )
# )
