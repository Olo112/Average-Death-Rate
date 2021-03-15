#======================================================================
#   IMPORTS:
#======================================================================

from matplotlib import pyplot as plt        # for plots
# import csv


#======================================================================
#   GLOBALS:
#======================================================================

ls_years = [1, 2, 3, 4]

ls_00 = [4442, 4545, 4666, 3992, 4333, 4567, 4862, 4532, 4091]      # example lists
ls_01 = [4444, 4555, 4866, 4992, 4339, 4537, 4962, 3532, 4092]
ls_02 = [4440, 4595, 4066, 4692, 4634, 4687, 4762, 4932, 3091]
ls_03 = [3077, 3471, 4244, 4956, 3834, 3844, 3844, 4611, 3285]


s_scv_file = 'file_name.txt'        # example file name



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG9_ = True						# Standard debug



#======================================================================
#   FUNCTIONS:
#======================================================================

def find_data(ls_file):
    '''
        input:
            file: file in which all the data is;

        output:
            ls_data_01:     list of an average death rate for specific year(s);
    '''

    global ls_data_01

    ls_data_01 = []
    file_len = len(ls_file)
    element_sum = sum(ls_file)/file_len    # summing all elements and dividing it by file_len

    ls_data_01.append(element_sum)
    if(_DBG9_): print(ls_data_01, '\nls_data_01 length =', file_len)


    return ls_data_01   #ls_data_02



#======================================================================
#   MAIN:
#======================================================================

if (__name__ == '__main__'):

    # open the file and read it
    #op_file = open(s_scv_file)
    #rd_file = read
    #found_data = find_data(s_scv_file)

    ls_main_data = []

    ls_data_00 = find_data(ls_00)
    ls_data_01 = find_data(ls_01)
    ls_data_02 = find_data(ls_02)
    ls_data_03 = find_data(ls_03)

    ls_main_data.append(ls_data_00[0])
    ls_main_data.append(ls_data_01[0])
    ls_main_data.append(ls_data_02[0])
    ls_main_data.append(ls_data_03[0])

    plt.xlabel("years from 2015")
    plt.ylabel("average deaths")

    plt.plot(ls_years, ls_main_data, color='blue', marker='o')
    plt.grid()
    plt.show()              # displaying the plot



#======================================================================
#   END OF FILE
#======================================================================