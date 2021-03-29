

'''
WHAT IM DOING:



'''

#======================================================================
#   IMPORTS:
#======================================================================

from matplotlib import pyplot as plt        # for plots
import csv                                  # for opening csv files



#======================================================================
#   GLOBALS:
#======================================================================

# ls_years = [1, 2, 3, 4]

'''
ls_00 = [4442, 4545, 4666, 3992, 4333, 4567, 4862, 4532, 4091]          # example lists
ls_01 = [4444, 4555, 4866, 4992, 4339, 4537, 4962, 3532, 4092]
ls_02 = [4440, 4595, 4066, 4692, 4634, 4687, 4762, 4932, 3091]
ls_03 = [3077, 3471, 4244, 4956, 3834, 3844, 3844, 4611, 3285]
'''

s_scv_file = 'liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv'        # example file name



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
    #if (_DBG9_): print(reader)

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

    if (_DBG9_): print('avr =',avr)        # debugger

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

    read_file = read_data(s_scv_file, 1)
    if (_DBG9_): print(read_file)


    print('----------------------------------------------')
    if (_DBG9_): print(collect_data(s_scv_file, 8))

    main_data = collect_data(s_scv_file, 8)

    plt.plot(main_data, label='deaths in 2015', marker='o', linewidth=2.0)

    plt.grid()
    plt.show()



    '''
    # other tests:
    
    ls_main_data = []

    ls_data_00 = find_data(ls_00)
    ls_data_01 = find_data(ls_01)
    ls_data_02 = find_data(ls_02)
    ls_data_03 = find_data(ls_03)

    ls_main_data.append(ls_data_00[0])
    ls_main_data.append(ls_data_01[0])
    ls_main_data.append(ls_data_02[0])
    ls_main_data.append(ls_data_03[0])

    plt.plot(ls_years, ls_main_data, color='blue', marker='o')
    plt.grid()
    plt.show()              # displaying the plot
    '''



#======================================================================
#   END OF FILE
#======================================================================