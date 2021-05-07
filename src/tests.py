#======================================================================
#   IMPORTS:
#======================================================================

import pandas as pd         # for operating on csv file
import count as c


#======================================================================
#   MAIN TESTS:
#=====================================================================

if (__name__ == '__main__'):
    print("tests.. \n")

    test_operations = c.Operations()     # creating main object


    summed = test_operations.sum_data_columns(12)
    print(summed, '\n\n')

    fixed_csv = test_operations.fix_csv('liczba_zgonow_w_rejestrze_od_1_wrzesnia_2015.csv', 0)
    print(fixed_csv)



#======================================================================
#   END OF FILE
#======================================================================