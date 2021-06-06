#======================================================================
#   IMPORTS:
#======================================================================

import csv
import numpy as np


#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG8_ = False                      # Other issues
_DBG9_ = False						# Standard debug



#======================================================================
#   CLASSES:
#======================================================================

class Operations:

    def __init__(self):
        # initializing class

        return



    def fix_csv(self, csv_file, col_num):
        '''
            in:
            csv_file:       name of csv file,
            col_num:        number of deleted column,

            deleting column in col_num (index of rows and columns start with 0),

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



    def zero_to_blank(self, ls_data):
        '''
            in:     list of data,

            fill empty spaces (elements which have '') with '0',

            out:    ls_fixed_blank;
        '''


        self.ls_data = ls_data

        ls_fixed_blank = []


        for row in ls_data:
            ls_row = []         # main point list

            for value in row:           # looping through each value in row
                if (value != ''):       # checking if value is not a blank string
                    ls_row.append(value)

                else:
                    ls_row.append(0)

            ls_fixed_blank.append(ls_row)


        return ls_fixed_blank



    def to_float(self, ls_data):
        '''
            in:     ls_data:    list of data,

            convert every element of list to int,

            out:    ls_conv_data:    converted list of int elements;
        '''


        self.ls_data = ls_data

        ls_conv_data = []


        for row in ls_data:
            row = [float(value) for value in row]       # changing all values in a list to float type
            ls_conv_data.append(row)


        return ls_conv_data



    def sum_data_columns(self, data_file):
        '''
            in:     data_file,

            reading the whole file of data, and get access to data,

            out:    ls_main_data:   list of average data;
        '''


        self.data_file = data_file

        ls_main_data = []


        ls_data_arrays = np.array(data_file)    # change main data_file to numpy array

        if (_DBG9_):
            for ls in ls_data_arrays.T:
                print(ls, '\n')



        for ls_data in ls_data_arrays.T:
            summed_data = sum(ls_data)      # sum all the data in that file
            data_length = len(ls_data)      # getting the number of elements in that list

            avr = (summed_data)/data_length     # counting average data

            ls_main_data.append(avr)


        return ls_main_data



#======================================================================
#   END OF FILE
#======================================================================