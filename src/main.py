#======================================================================
#   IMPORTS:
#======================================================================
from typing import Type

from matplotlib import pyplot as plt        # for plots
import csv                                  # for operations on csv file(s)
import count as c



#======================================================================
#   GLOBALS:
#======================================================================

s_scv_file = 'liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv'        # file name



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG9_ = True						# Standard debug



#======================================================================
#   FUNCTIONS:
#======================================================================

def read_file(csv_file_name):

    '''
        in:     csv_csv_file_name:  name of a csv file with data,

        change blank places to '0'

        out:    ls_data:    list of all the data that
    '''

    file = open(csv_file_name, 'r')

    read_data = csv.reader(file)

    for row in read_data:
        del row[0]
        for i in row:
            if (i == ''):
                #i = '0'
                row.insert(row.index(i), '0')
                if (_DBG9_): print('i =', i)

                pass

            else:
                pass

        if (_DBG9_): print(row)

    return



def main():
    '''
        in:



        out:
    '''
    ls_data = []

    return



#======================================================================
#   MAIN:
#======================================================================

if (__name__ == '__main__'):

    counter = c.Operations       # creating main object

    read_file(s_scv_file)


    plt.xlabel("Years (from 2015)")     # main labels
    plt.ylabel("ADR")

    plt.grid()      # display grid in plot
    plt.show()      # displaying main plot



#======================================================================
#   END OF FILE
#======================================================================
