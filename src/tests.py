#======================================================================
#   IMPORTS:
#======================================================================

import pandas as pd         # for operating on csv file
import csv
import count as c



#======================================================================
#   MAIN TESTS:
#======================================================================

if (__name__ == '__main__'):
    print("tests.. \n")

    test_operations = c.Operations()     # creating main object


    summed = test_operations.sum_data_columns(12)
    print(summed, '\n\n')

    fixed_csv = test_operations.fix_csv(csv_file='liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv', col_num=0)   # deleting first column and row
    fixed_csv = fixed_csv.to_csv()
    print(fixed_csv, '\n\n')


    # opening and reading csv
    file = open('liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv', 'r')
    reader = csv.reader(file)

    for element in reader:
        del element[0]
        #print(element)

        # filling blank with 0 digit:
        test_operations.zero_to_blank(element)

        # converting to int:
        test_operations.to_int(element)

        print(element)



#======================================================================
#   END OF FILE
#======================================================================