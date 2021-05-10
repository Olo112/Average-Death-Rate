#======================================================================
#   IMPORTS:
#======================================================================
import csv

import pandas as pd         # for operating on csv file



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG9_ = True						# Standard debug



#======================================================================
#   CLASSES:
#======================================================================

class Operations:
    # operation class

    def __init__(self):
        # initializing class


        return



    def fix_csv(self, csv_file, col_num):
        '''
            in:     csv_file, row number and column number,

            deleting row in row_num and column in col_num (index of rows and columns start with 0)

            out:    ls_ls_csv_data:     list of csv data;
        '''


        self.csv_file = csv_file
        self.col_num = col_num

        ls_csv_data = []        # main list


        file = open(csv_file)
        reader = csv.reader(file)

        for element in reader:
            del element[col_num]
            ls_csv_data.append(element)


        return ls_csv_data



    def to_int(self, ls_data):
        '''
            in:     list of data,

            convert every element of list to int,

            out:    converted list of int elements;
        '''


        self.ls_data = ls_data

        ls_data = [int(element) for element in ls_data]     # converting each element in ls_data to type int

        return ls_data



    def zero_to_blank(self, ls_data):
        '''
            in:     list of data,

            fill empty spaces (elements which have '') with '0',

            out:    ls_fixed_blank
        '''


        self.ls_data = ls_data

        ls_fixed_blank = []



        for element in ls_data:

            if (element != ''):
                ls_fixed_blank.append(element)

            else:
                ls_fixed_blank.append('0')


        return ls_fixed_blank



    def sum_data_columns(self, data_file):
        '''
            in:     data_file,

            reading the whole file of data, and get access to data,

            out:    read_data;
        '''

        # go through the whole data file


            # check if every element is a digit


            # sum all the data in that file





        self.data_file = data_file


        return "data =", data_file



#======================================================================
#   END OF FILE
#======================================================================