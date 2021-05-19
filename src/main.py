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
_DBG9_ = False						# Standard debug



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


    ls_years = []
    year = 2015
    for i in range(len(ls_float_data[0])):
        ls_years.append(year)
        year = year + 1


    ls_second_years = ls_years[5:]

    del ls_float_data[0]       # deleting years list ls_filled_float_data[0]

    if (_DBG9_):
        for row in ls_float_data:
            print(row)
        print('\n\n')


    if (_DBG9_): print('years =', ls_years, '\n\n')


    ls_main_data = data_counter.sum_data_columns(ls_float_data)     # going through columns and counting average


    figure, (axis0, axis1) = plt.subplots(nrows=2, ncols=1)


    # displaying the data on graph (creating plots):
    # 1. naming labels of OX, OY and chart title:
    axis0.set_title("ADR data charts 2015 - 2021")
    axis0.set_xlabel('Years')         # OX label: years from 2015
    axis0.set_ylabel('ADR')           # OY label: ADR (short: average death rate)

    axis0.plot(ls_years, ls_main_data, label='ADR', marker='o')      # OX data, OY data
    axis0.legend()
    axis0.grid(True)


    axis1.set_xlabel('Years (2020 - 2021+)')         # OX label: years from 2015
    axis1.set_ylabel('ADR')           # OY label: ADR (short: average death rate)

    axis1.plot(ls_second_years, ls_main_data[5:], label='ADR', marker='o', color='orange')
    axis1.legend()
    axis1.grid(True)

    plt.show()      # 2. displaying plots (with grid and legend):

#======================================================================
#   END OF FILE
#======================================================================