#======================================================================
#   IMPORTS:
#======================================================================

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


    data_counter = c.Operations()   # creating main object

    main_file = open(s_scv_file)
    reader = csv.reader(main_file)      # creating a csv reader to read all data

    ls_float_data = []



    ls_fixed_data = data_counter.fix_csv(csv_file=s_scv_file, col_num=0)     # fix the main data (deleting first column)
    if (_DBG9_):
        for row in ls_fixed_data:
            print(row)

        print('\n\n')


    ls_filled_data = data_counter.zero_to_blank(ls_fixed_data)   # filling blank with 0 digit
    if (_DBG9_):
        for row in ls_filled_data:
            print(row)

        print('\n\n')


    for row in ls_filled_data:
        row = [float(data_val) for data_val in row]     # converting all data vaules to float
        ls_float_data.append(row)


        if (_DBG9_): print(row)

    print('\n\n')


    del ls_float_data[0]       # deleting years list ls_filled_float_data[0]

    if (_DBG9_):
        for row in ls_float_data:
            print(row)
        print('\n\n')


    ls_years = []
    year = 2015
    for i in range(len(ls_float_data[0])):
        ls_years.append(year)
        year = year + 1

    if (_DBG9_): print('years =', ls_years, '\n\n')


    ls_main_data = data_counter.sum_data_columns(ls_float_data)     # going through columns and counting average



    # displaying the data on graph (creating plots):

    # 1. naming labels of OX, OY and window title:
    plt.title("ADR data chart from 2015")
    plt.xlabel('Years')         # OX label: years from 2015
    plt.ylabel('ADR')           # OY label: ADR (short: average death rate)


    # 2. adding plot:
    plt.plot(ls_years, ls_main_data, label='ADR', marker='o')      # OX data, OY data,

    # 2. displaying (with grid):
    plt.grid(True)
    plt.show()



#======================================================================
#   END OF FILE
#======================================================================