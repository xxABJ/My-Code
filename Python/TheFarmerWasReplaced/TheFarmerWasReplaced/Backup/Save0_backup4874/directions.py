if (even_farmland == True):
    #1. Moves the drone the remaining moves required to compelete the Bottom-left set.
    #2. Moves the drone the remaining moves required to compelete the Bottom-left set.
    #3. Moves the drone the remaining moves required to compelete the Bottom-left set.
    #4. Moves the drone the remaining moves required to compelete the Bottom-left set.

    #1
    if ((x == (0) or (total_side_length % 2 == 1)) and ((y == 0) or ((total_side_length % 2 == 1))): #blc1 
        #1. A Loop to move the drone the remaining move to reach a "Starting Point".

        #1.
        for bl_remaining_moves in range(bl_remaining_moves):
            #1. Executing the remaining moves for the Bottom-left set. This indicates the first stage of the set-rotation.
            #2. Executing the remaining moves for the Bottom-left set. This indicates the second stage of the set-rotation.
            #3. Executing the remaining moves for the Bottom-left set. This indicates the third stage of the set-rotation.
            #4. Executing the remaining moves for the Bottom-left set. This indicates the fourth stage of the set-rotation.

            #1.
            if ((get_pos_x() == (0) or (total_side_length % 2 == 1)) and (get_pos_y() == (0))):
                #1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
		        #2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
		        #3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

		        #1.
                if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
                
                    harvest() # Plants grass automatically if ground is a Grassland.
                    move(North)
                    current_set = bl_set
                    past_move = north
                    current_move = north
                    next_move = north

                #2.	
                elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
                
                    harvest() # Plants grass automatically if ground is a Grassland.	
                    till()
                    move(North)
                    current_set = bl_set
                    past_move = north
                    current_move = north
                    next_move = north

                #3.	
                elif (can_harvest() != True):
                
                    move(North)
                    current_set = bl_set
                    past_move = north
                    current_move = north
                    next_move = north
                    detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
                    main_harvesting_rotation = 0
            
            #2.
            elif ((get_pos_x() == (0) or (total_side_length % 2 == 1)) and ((get_pos_y() == total_side_length))):
                #1. Moves the drone in the East direction after 'checking for turf -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
		        #2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
		        #3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

		        #1.
                if get_ground_type() == Grounds.Turf and can_harvest() == True:
                
                    harvest() # Plants grass automatically if ground is a Turf.
                    move(East)
                    current_set = bl_set
                    past_move = north
                    current_move = east
                    next_move = south

		        #2.	
                elif get_ground_type() == Grounds.Soil and can_harvest() == True:
                
                    harvest() # Plants grass automatically if ground is a Turf.	
                    till()
                    move(East)
                    current_set = bl_set
                    past_move = north
                    current_move = east
                    next_move = south

		        #3.	
                elif can_harvest() != True:
                
                    move(East)
                    current_set = bl_set
                    past_move = north
                    current_move = east
                    next_move = south
                    detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
                    main_harvesting_rotation = 0

            #3.
            elif ((get_pos_x() == (total_side_length % 2 == 0)) and (get_pos_y() == ((total_side_length % 2 == 0) and not (0)))):
                #1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
		        #2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
		        #3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

		        #1.
                if get_ground_type() == Grounds.Grassland and can_harvest() == True:
                
                    harvest() # Plants grass automatically if ground is a Grassland.
                    move(South)
                    current_set = bl_set
                    past_move = east
                    current_move = south
                    next_move = south

		        #2.	
                elif get_ground_type() == Grounds.Soil and can_harvest() == True:
                
                    harvest() # Plants grass automatically if ground is a Grassland.	
                    till()
                    move(South)
                    current_set = bl_set
                    past_move = east
                    current_move = south
                    next_move = south

		        #3.	
                elif can_harvest() != True:
                
                    move(South)
                    current_set = bl_set
                    past_move = east
                    current_move = south
                    next_move = south
                    detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
                    main_harvesting_rotation = 0
            
            #4.
            elif ((get_pos_x() == total_side_length % 2 == 0) and (get_pos_y() == 0)):
                #1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
		        #2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
		        #3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

		        #1.
                if get_ground_type() == Grounds.Grassland and can_harvest() == True:
                
                    harvest() # Plants grass automatically if ground is a Grassland.
                    move(East)
                    current_set = bl_set
                    past_move = north
                    current_move = east
                    next_move = south

		        #2.	
                elif get_ground_type() == Grounds.Soil and can_harvest() == True:
                
                    harvest() # Plants grass automatically if ground is a Grassland.	
                    till()
                    move(East)
                    current_set = bl_set
                    past_move = north
                    current_move = east
                    next_move = south

		        #3.	
                elif can_harvest() != True:
                
                    move(East)
                    current_set = bl_set
                    past_move = north
                    current_move = east
                    next_move = south
                    detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
                    main_harvesting_rotation = 0

    #2.
    elif ((x == (total_side_length % 2 == 0)) and (y == (0) or (total_side_length % 2 == 0))): #brc2
        #1. A Loop to move the drone the remaining move to reach a "Starting Point".

        #1.
        for br_remaining_moves in range(br_remaining_moves):
            #1. Executing the remaining moves for the Bottom-right set. This indicates the first stage of the set-rotation.
            #2. Executing the remaining moves for the Bottom-right set. This indicates the second stage of the set-rotation.
            #3. Executing the remaining moves for the Bottom-right set. This indicates the third stage of the set-rotation.
            #4. Executing the remaining moves for the Bottom-right set. This indicates the fourth stage of the set-rotation.

            #1.
            if ((get_pos_x() == (total_side_length)) and (get_pos_y() == ((0) or (total_side_length % 2 == 1)))):
			    #1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
			    #2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
			    #3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
    
			    #1.
			    if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
                
			    	harvest() # Plants grass automatically if ground is a Grassland.
			    	move(West)
			    	current_set = br_set
			    	past_move = west
			    	current_move = west
			    	next_move = west
    
			    #2.	
			    elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
                
			    	harvest() # Plants grass automatically if ground is a Grassland.	
			    	till()
			    	move(West)
			    	current_set = br_set
			    	past_move = west
			    	current_move = west
			    	next_move = west
    
			    #3.	
			    elif (can_harvest() != True):
                
			    	move(West)
			    	current_set = br_set
			    	past_move = west
			    	current_move = west
			    	next_move = west
			    	detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
			    	main_harvesting_rotation = 0

    #3.
    elif ( (x == 0) and (y == (total_side_length_positional % 2 == 0)) ): #trc3
        # continue bl set with remaining moves

    #4.
    elif ( (x == 0) and (y == (total_side_length_positional % 2 == 1)) ): #tlc4
        # new tl set-rotation

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
