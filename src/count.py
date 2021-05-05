#======================================================================
#   IMPORTS:
#======================================================================

import pandas as pd         # for operating on csv file



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG9_ = False						# Standard debug



#======================================================================
#   CLASSES:
#======================================================================

class Operation:
    # operation class

    def __init__(self):
        # initializing class

        return



    def fix_csv(self, csv_file, row_num, col_num):
        '''
            in:     csv_file, row number and column number,

            deleting row in row_num and column in col_num,

            out:    csv_file without the deleted row and column;
        '''

        self.csv_file = csv_file
        self.row_num = row_num
        self.col_num = col_num


        csv_file_data = pd.read_csv(csv_file)

        fixed_csv = csv_file_data.drop(index=row_num, columns=col_num)        # deleting first row and first column

        return fixed_csv






    def sum_data_columns(self, data):
        '''
            in:     data,

            reading the whole file of data, and get access to data,

            out:    read_data;
        '''

        self.data = data



        return "data =", data



#======================================================================
#   MAIN:       # for tests
#======================================================================

if (__name__ == '__main__'):
    Obj = Operation()

