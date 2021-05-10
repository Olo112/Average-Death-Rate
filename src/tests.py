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
_DBG9_ = True						# Standard debug



#======================================================================
#   MAIN TESTS:
#======================================================================

if (__name__ == '__main__'):
    print("tests.. \n")

    # opening and reading csv
    file = open('liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv', 'r')
    reader = csv.reader(file)

    print("reader: \n")

    if (_DBG9_):
        for i in reader:
            print(i)


    test_operations = c.Operations()     # creating main object


    summed = test_operations.sum_data_columns(12)
    print(summed, '\n\n')

    fixed_data = test_operations.fix_csv(csv_file='liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv', col_num=0)   # deleting first column and row
    #print()


        # filling blank with 0 digit:
        #test_operations.zero_to_blank(element)

        # converting to int:
        #test_operations.to_int(element)

        #print(element)



#======================================================================
#   END OF FILE
#======================================================================