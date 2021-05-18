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

    counter = c.Operations       # creating main object

    read_file(s_scv_file)


    plt.xlabel("Years (from 2015)")     # main labels
    plt.ylabel("ADR")

    plt.grid()      # display grid in plot
    plt.show()      # displaying main plot



#======================================================================
#   END OF FILE
#======================================================================
