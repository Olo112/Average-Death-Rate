#======================================================================
#   IMPORTS:
#======================================================================

from matplotlib import pyplot as plt        # for plots
# import csv


#======================================================================
#   GLOBALS:
#======================================================================

ls_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]              # test lists
ls_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]



s_scv_file = 'file_name.txt'



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG9_ = True						# Standard debug



#======================================================================
#   FUNCTIONS:
#======================================================================

def find_data(file):
    '''
        input:
            file: file in which all the data is;

        output:
            ls_data_01:     list of an average death rate for specific year(s);
    '''

    global ls_data_01  #ls_data_02

    ls_data_01 = []
    #ls_data_02 = []

    file_len = len(file)

    # counting the sum of all elements in the list and adding to the list
    element_sum = sum(file)

    ls_data_01.append(element_sum)


    return ls_data_01   #ls_data_02



#======================================================================
#   MAIN:
#======================================================================

if (__name__ == '__main__'):

    # open the file and read it
    #op_file = open(s_scv_file)


    #rd_file = read

    found_data = find_data(s_scv_file)

    plt.plot(ls_1)
    plt.grid()
    plt.show()              # displaying the plot



#======================================================================
#   END OF FILE
#======================================================================