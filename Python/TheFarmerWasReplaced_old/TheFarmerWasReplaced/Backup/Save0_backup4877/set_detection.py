from abj import *

while ((even_farmland == True) or (odd_farmland == True)):
    #1. Checks the size of the farmland, for even sides.
    #2. Checks the size of the farmland, for odd sides.

    #1.
    if (even_farmland == True):
        #1. Updates the current set indicator in the "Set and Direction system" to the Bottom-left set.
        #2. Updates the current set indicator in the "Set and Direction system" to the Bottom-right set.
        #3. Updates the current set indicator in the "Set and Direction system" to the Top-right set.
        #4. Updates the current set indicator in the "Set and Direction system" to the Top-left set.

        #1.
        if ((x == ((0) or (total_side_length_positional % 2 == 0))) and (y == ((0) or (total_side_length_positional % 2 == 0)))):
        
            current_set == bl_set

        #2.
        elif ((x == (total_side_length_positional % 2 == 1)) and (y == ((0) or (total_side_length_positional % 2 == 0)))):
        
            current_set == br_set        

        #3.
        elif ((x == (total_side_length_positional % 2 == 1)) and (y == (total_side_length_positional % 2 == 1))):
        
            current_set == tr_set

        #4.
        elif ((x == ((0) or (total_side_length_positional % 2 == 0))) and (y == (total_side_length_positional % 2 == 1))):

            current_set == tl_set

    #2. #NOT CORRECT
    elif (odd_farmland == True):
        #1.
        #2.

        #1.
        if ((x == ((0) or (total_side_length_positional % 2 == 0))) and (y == ((0) or (total_side_length_positional % 2 == 0)))):
        
        #2.
        elif ((x == (total_side_length_positional % 2 == 1)) and (y == ((0) or (total_side_length_positional % 2 == 0)))):
        
        #3.
        elif ((x == (total_side_length_positional % 2 == 1)) and (y == (total_side_length_positional % 2 == 1))):
        
        #4.
        elif ((x == ((0) or (total_side_length_positional % 2 == 0))) and (y == (total_side_length_positional % 2 == 1))):