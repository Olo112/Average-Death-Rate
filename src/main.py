#======================================================================
#   IMPORTS:
#======================================================================

from matplotlib import pyplot as plt        # for plots
import csv                                  # for opening csv files



#======================================================================
#   GLOBALS:
#======================================================================



s_scv_file = 'liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv'        # example file name



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG9_ = False						# Standard debug



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



def read_data(csv_file_name, row_num):
    '''
        input:
            csv_file_name:   current csv file (name in string);

        output:
            ls_data:        list of current data from csv_file_name;
    '''

    global ls_data

    ls_data = []

    file = open(csv_file_name, 'r')
    reader = csv.reader(file)
    if (_DBG9_): print(reader)

    for line in reader:     # going through whole read .csv file line
        if (line[row_num] != ''):
            ls_data.append(line[row_num])
            if (_DBG9_): print(line[row_num])

        else:
            pass

    del ls_data[0]      # delete first element which is the date
    ls_data = [int(element) for element in ls_data]     # changing all elements to int()
    if (_DBG9_): print(ls_data)


    l = len(ls_data)
    el_sum = sum(ls_data)
    avr = (el_sum)/l

    if (_DBG9_): print('avr =',avr)

    return avr



def collect_data(csv_file_name, years_num):
    '''
    input:
        file_name:  source of data;

    output:
        ---
    '''

    global ls_global_data

    ls_global_data = []

    for i in range(0, years_num):
        read_row = read_data(csv_file_name, i)
        ls_global_data.append(read_row)


        if (_DBG9_): print('read_row =',read_row)
        # if (_DBG9_): print('\n\nls_global_data =',ls_global_data)

    del ls_global_data[0]

    if (_DBG9_): print('\n\nls_global_data =', ls_global_data)

    return ls_global_data



#======================================================================
#   MAIN:
#======================================================================

if (__name__ == '__main__'):

    plt.xlabel("Years (from 2015)")

    plt.grid()      # display grid in plot
    plt.show()      # displaying main plot



#======================================================================
#   END OF FILE
#======================================================================
