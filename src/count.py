#======================================================================
#   IMPORTS:
#======================================================================

import csv
import numpy as np
import matplotlib.pyplot as plt


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






    def sqrtn( self, x , power ):
        """
            input:
                x:   value which will be operated;
        """

        operation_val = (  x ** ( 1 / power )  )


        return operation_val




    def count_average( self, ls_data : list ):
        """
            input:
                ls_data:    list of data;

            output:
                average_val:    average value of the list;
        """

        n = len( ls_data )      # length of the list

        average_val = (  sum( ls_data ) / n  )      # counting average value


        return average_val




    def count_sum_val( self , ls_x : list, x_average ):
        """
            input:
                ls_x:   list of data to count square of sum of difference of i-th element and x_average,
                x_average:      average value;

            output:
                summed_val: sum value of list;
        """

        ls_val = []


        for x in ls_x:
            sum_val = ( x - x_average )**2      # y(x) = sum(x_i - x_average)^2
            ls_val.append( sum_val )


        sum_val = sum( ls_val )

        return sum_val




    def count_std_dev( self , ls_x : list ):
        """
            input:
                ls_x:   list of x values;

            output:
                std_dev_val:    value of standard deviation;
        """

        # standard deviation formula:   sqrt( ( 1/n-1 ) * sum ( x_i - x_average )**2 )


        n = len( ls_x )


        # x_average
        average_val = self.count_average( ls_x )                    # count average value

        # sum ( x_i - x_average )
        summed_val = self.count_sum_val( ls_x , average_val )       # count summed value


        std_dev_val = self.sqrtn( ( 1 / (n-1) ) * summed_val , 2 )




        return std_dev_val



    def display_std_dev( self, ls : list ):

        """
            input:
                ls:     list of given data;

            output:
                displays standard deviation
        """

        ls_std_dev = []
        n = len( ls )

        std_dev_val = self.count_std_dev(ls)


        for i in range( n+1 ):
            ls_std_dev.append(std_dev_val)


        plt.plot( ls_std_dev )

        return



#======================================================================
#   END OF FILE
#======================================================================