import os
from FileHelper import FileHelper

class TemplateRenderer(FileHelper):


    ## #################################################################
    ##  PRIVATE ATTRIBUTES PART
    ## #################################################################

    _template_content = None

    ##
    #
    ##
    def set_file(self, file):
        # Call the parent method
        super(TemplateRenderer, self).set_file(file)

        # Do some extra work
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
        if self.get_file() == None:
            raise RuntimeError("No template file provided.")

        self._template_content = open(self.get_file()).read()

    ##
    #
    ##
    def _reset_template_content(self):
        self._template_content = None



############################
# TEST TEST TEST
############################

# data = {
#     "name": "Dries",
#     "date": "2018-01-01",
#     "total": 0.12
# }
#
# obj = TemplateRenderer()
# obj.set_file("templates/email_message.txt")
# print(obj.render(data))
#
# # Test reset the file content
# obj.set_file("templates/email_message.html")
# print(obj.render(data))
