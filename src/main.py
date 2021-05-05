#======================================================================
#   IMPORTS:
#======================================================================
from typing import Type

from matplotlib import pyplot as plt        # for plots
import csv                                  # for opening csv files
import count as c



#======================================================================
#   GLOBALS:
#======================================================================
from src.count import Operation

s_scv_file = 'liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv'        # file name



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG9_ = False						# Standard debug



#======================================================================
#   FUNCTIONS:
#======================================================================

def to_int(ls):
    ls = [int(element) for element in ls]
    if (_DBG9_): print(ls)

    return ls



#======================================================================
#   MAIN:
#======================================================================

if (__name__ == '__main__'):

    counter = c.Operation       # creating main object



    plt.xlabel("Years (from 2015)")     # main labels
    plt.ylabel("ADR")

    plt.grid()      # display grid in plot
    plt.show()      # displaying main plot



#======================================================================
#   END OF FILE
#======================================================================
