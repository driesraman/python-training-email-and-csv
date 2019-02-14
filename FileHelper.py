import os

class FileHelper:

    ## #################################################################
    ##  PRIVATE ATTRIBUTES PART
    ## #################################################################

    _file = None


    ## #################################################################
    ##  GET AND SET PART
    ## #################################################################

    ##
    #
    ##
    def get_file(self):
        return self._file

    ##
    #
    ##
    def set_file(self, file):
        # Make the path system (windows, mac, linux) independent
        # and make it relative to the current working directory
        local_file = os.path.join(os.getcwd(), file)

        # Verify the fileexists
        if not os.path.isfile(local_file):
            raise FileNotFoundError("File '%s' not found" %(local_file))

        # set the file
        self._file = local_file
