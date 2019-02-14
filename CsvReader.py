import csv
from FileHelper import FileHelper

# Not ideal, but just testing class extension and csv reading
class CsvReader(FileHelper):

    ## #################################################################
    ##  PRIVATE ATTRIBUTES PART
    ## #################################################################

    _data = []


    ## #################################################################
    ##  GET AND SET PART
    ## #################################################################

    ##
    #
    ##
    def get_data(self):
        return self._data


    ## #################################################################
    ##  PUBLIC METHODS PART
    ## #################################################################

    ##
    #
    ##
    def load_data(self):
        with open(self.get_file(), "r") as data_file:
            reader = csv.DictReader(data_file)

            # There is probably a better way for this...
            for row in reader:
                # Make sure the total field is a float value
                # # => needed for the formatting in the MailMessage class
                row["total"] = float(row["total"])

                self._data.append(row)



############################
# TEST TEST TEST
############################

# obj = CsvReader()
# obj.set_file("data.csv")
# obj.load_data()
#
# print(obj.get_data())
