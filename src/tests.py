#======================================================================
#   IMPORTS:
#======================================================================

import pandas as pd         # for operating on csv file
import csv
import count as c



#---------------------------------------------------------
#   DEBUGGERS:
#---------------------------------------------------------

_DBG0_ = True						# Errors
_DBG1_ = True						# Warnings
_DBG8_ = True                       # For other bugs
_DBG9_ = True						# Standard debug



#======================================================================
#   MAIN TESTS:
#======================================================================

if (__name__ == '__main__'):
    print("tests.. \n")

    # opening and reading csv
    file = open('liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv', 'r')
    reader = csv.reader(file)

    '''     WORKS
    print("reader: \n")
    if (_DBG8_):
        for i in reader:
            print(i)
    '''


    test_operations = c.Operations()     # creating main test object


    summed = test_operations.sum_data_columns(12)
    print(summed, '\n\n')

    fixed_data = test_operations.fix_csv(csv_file='liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv', col_num=0)   # deleting first column and row

    '''
    if (_DBG8_):
        for i in fixed_data:
            print(i) 
    '''

    # filling blank with 0 digit:
    filled_data = test_operations.zero_to_blank(fixed_data)

    ''' WORKS
    for i in filled_data:
        print(i)
    '''

    # converting to float:
    ls_filled_float_data = []

    for row in filled_data:
        row = [float(val) for val in row]
        ls_filled_float_data.append(row)


    del ls_filled_float_data[0]

    for row in ls_filled_float_data:
        print(row)


    '''
    for row in fixed_data:
        row = [float(value) for value in row]
        print(row)

        # ls_int_data.append(row)
    '''

    # test_operations.to_int(element)



#======================================================================
#   END OF FILE
#======================================================================