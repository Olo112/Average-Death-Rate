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
    # counting class

    def __init__(self):
        # initializing class

        return



    def delete_row_col(self, csv_file, row_num, col_num):
        '''
            in:     csv_file, row number and column number,

            deleting row in row_num and column in col_num,

            out:    csv_file without the deleted row and column;
        '''


        return



    def read(self, csv_file):
        '''
            in:     csv_file;

            reads the csv file and returns the main values

            out:    None

        '''

        pd.read_csv(csv_file)

        return



    def get_data(self, data):
        '''
            in:     data,

            reading the whole file of data,

            out:    read_data;
        '''



        return "data =", data



#======================================================================
#   MAIN:       # for tests
#======================================================================

if (__name__ == '__main__'):
    Obj = Operation()

    ls = Obj.get_data([1, 2, 3])

    print(ls)