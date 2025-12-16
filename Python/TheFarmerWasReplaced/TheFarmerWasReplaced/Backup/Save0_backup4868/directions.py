if (even_farmland == True):
    
    for side_blocks in range(1):

        #bottom side
        if ( (x == (total_side_length_positional % 2 == 0)) and (y == 0) ):
            # new bl set-rotation
            (total_side_lenth - x) / 2 = num of sets required 

        elif ( (x == (total_side_length_positional % 2 == 1)) and (y == 0) ):
            # continue br set with remaining moves
            for

        #left side
        elif ( (x == 0) and (y == (total_side_length_positional % 2 == 0)) ):
            # continue bl set with remaining moves
            for

        elif ( (x == 0) and (y == (total_side_length_positional % 2 == 1)) ):
            #  new tl set-rotation

        #top side
        elif ( (x == (total_side_length_positional % 2 == 0)) and (y == total_side_length_positional) ):
            # continue tl set with remaining moves
            for

        elif ( (x == (total_side_length_positional % 2 == 1)) and (y == total_side_length_positional) ):
            # new tr set-rotation

        #right side
        elif ( (x == total_side_length_positional) and (y == (total_side_length_positional % 2 == 0)) ):
            # new br set-rotation

        elif ( (x == total_side_length_positional) and (y == (total_side_length_positional % 2 == 1)) ):
            # continue tr set with rotation
            for

    for inner_blocks in range(1):

        o,e = d
        o,o = r 
        e,o = l 
        e,e = u  

elif (odd_farmland == True): #NOT CORRECT

    for side_blocks in range(1):

         #bottom side
        if ( (x == (total_side_length_positional % 2 == 0)) and (y == 0) ):
            # new bl set-rotation

        elif ( (x == (total_side_length_positional % 2 == 1)) and (y == 0) ):
            # continue br set with remaining moves

        #left side
        elif ( (x == 0) and (y == (total_side_length_positional % 2 == 0)) ):
            # continue bl set with remaining moves

        elif ( (x == 0) and (y == (total_side_length_positional % 2 == 1)) ):
            #  new tl set-rotation

        #top side
        elif ( (x == (total_side_length_positional % 2 == 0)) and (y == total_side_length_positional) ):
            # continue tl set with remaining moves

        elif ( (x == (total_side_length_positional % 2 == 1)) and (y == total_side_length_positional) ):
            # new tr set-rotation

        #right side
        elif ( (x == total_side_length_positional) and (y == (total_side_length_positional % 2 == 0)) ):
            # new br set-rotation

        elif ( (x == total_side_length_positional) and (y == (total_side_length_positional % 2 == 1)) ):
            # continue tr set with rotation

    for inner_blocks in range(1): #NOT CORRECT

        o,e = d
        o,o = r 
        e,o = l 
        e,e = u  
