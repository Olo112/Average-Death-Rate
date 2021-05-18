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
#   MAIN:
#======================================================================

if (__name__ == '__main__'):
    count_data = c.Operations()   # creating main object

    main_file = open(s_scv_file)
    reader = csv.reader(main_file)      # csv reader to read all data

    ls_fixed_data = count_data.fix_csv(csv_file=s_scv_file, col_num=0)     # fix the main data (deleting first column)
    if (_DBG9_):
        for row in ls_fixed_data:
            print(row)


    counter = c.Operations       # creating main object

    read_file(s_scv_file)


    plt.xlabel("Years (from 2015)")     # main labels
    plt.ylabel("ADR")

    plt.grid()      # display grid in plot
    plt.show()      # displaying main plot



#======================================================================
#   END OF FILE
#======================================================================
