from all_variables import *

if (odd_farmland == True): # Odd & Even based on block number, not positional *
				#1. Moves the drone the remaining moves required to compelete the Bottom-left set.      (lucky middle, x and y is odd)
				#2. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (lucky middle, x and y is even)
				#3. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (Diagonal TLBR line, x > y, x and y is odd)
				#4. Moves the drone the remaining moves required to compelete the Bottom-left set.      (Diagonal TLBR line, x > y, x and y is even)
				#5. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (Diagonal TLBR line, x < y, x and y is odd)
				#6. Moves the drone the remaining moves required to compelete the Bottom-left set.      (Diagonal TLBR line, x < y, x and y is even)
				#7. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (Below the diagonal TLBR line, drone on odd blocks)
				#8. Moves the drone the remaining moves required to compelete the Bottom-left set.      (Below the diagonal TLBR line, drone on even blocks)
				#9. Moves the drone the remaining moves required to compelete the Bottom-left set.  	(Below the diagonal TLBR line, x is even block and y is odd)
				#10. Moves the drone the remaining moves required to compelete the Bottom-left set. 	(Below the diagonal TLBR line, x is odd block and y is even)
				#11. Moves the drone the remaining moves required to compelete the Top-right-odd set.   (Above the diagonal TLBR line, drone on odd blocks)
				#12. Moves the drone the remaining moves required to compelete the Bottom-left set.     (Above the diagonal TLBR line, drone on even blocks)
				#13. Moves the drone the remaining moves required to compelete the Top-right-odd set. 	(Above the diagonal TLBR line, x is even block and y is odd)
				#14. Moves the drone the remaining moves required to compelete the Top-right-odd set. 	(Above the diagonal TLBR line, x is odd block and y is even)

	#1.
	if ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and (((get_pos_x()) and (get_pos_y())) == (total_side_length_positional % 2 == 0))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for bl_moves_remaining in range(bl_moves_remaining):
			#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
			#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

			#1.
			if ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
			elif ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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

			#3.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#3.	
				elif can_harvest() != True:
				
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#3.	
				elif can_harvest() != True:
				
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#2.
	elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and (((get_pos_x()) and (get_pos_y())) == (total_side_length_positional % 2 == 1))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for tro_moves_remaining in range(tro_moves_remaining):
			#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
			#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

			#1.
			if ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#2.
			elif ((get_pos_x() == (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#3.
			elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#3.
	elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) > (get_pos_y())) and (((get_pos_x()) == (total_side_length_positional % 2 == 0)) and ((get_pos_y()) == ((0) or (total_side_length_positional % 2 == 0))))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for tro_moves_remaining in range(tro_moves_remaining):
			#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
			#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

			#1.
			if ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#2.
			elif ((get_pos_x() == (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#3.
			elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#4.
	elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) > (get_pos_y())) and (((get_pos_x()) == (total_side_length_positional % 2 == 1)) and ((get_pos_y()) == (total_side_length_positional % 2 == 1)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for bl_moves_remaining in range(bl_moves_remaining):
			#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
			#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

			#1.
			if ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
			elif ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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

			#3.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#3.	
				elif can_harvest() != True:
				
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
					
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#3.	
				elif can_harvest() != True:
				
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#5.
	elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) < (get_pos_y())) and (((get_pos_x()) == ((0) or (total_side_length_positional % 2 == 0))) and ((get_pos_y()) == (total_side_length_positional % 2 == 0)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for tro_moves_remaining in range(tro_moves_remaining):
			#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
			#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

			#1.
			if ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#2.
			elif ((get_pos_x() == (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#3.
			elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
					
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#6. 
	elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) < (get_pos_y())) and (((get_pos_x()) == (total_side_length_positional % 2 == 1)) and ((get_pos_y()) == (total_side_length_positional % 2 == 1)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for bl_moves_remaining in range(bl_moves_remaining):
			#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
			#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

			#1.
			if ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
			elif ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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

			#3.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#3.	
				elif can_harvest() != True:
				
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#3.	
				elif can_harvest() != True:
				
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#7.
	elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (0) or (total_side_length_positional % 2 == 0)) and ((get_pos_y()) == (0) or (total_side_length_positional % 2 == 0)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for tro_moves_remaining in range(tro_moves_remaining):
			#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
			#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

			#1.
			if ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#2.
			elif ((get_pos_x() == (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#3.
			elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#8.
	elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (total_side_length_positional % 2 == 1)) and ((get_pos_y()) == (total_side_length_positional % 2 == 1)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for bl_moves_remaining in range(bl_moves_remaining):
			#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
			#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

			#1.
			if ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
			elif ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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

			#3.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#3.	
				elif can_harvest() != True:
				
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#3.	
				elif can_harvest() != True:
				
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#9.
	elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (total_side_length_positional % 2 == 1)) and ((get_pos_y()) == (total_side_length_positional % 2 == 0)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for bl_moves_remaining in range(bl_moves_remaining):
			#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
			#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

			#1.
			if ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
			elif ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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

			#3.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#3.	
				elif can_harvest() != True:
				
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#3.	
				elif can_harvest() != True:
				
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#10.
	elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (total_side_length_positional % 2 == 0)) and ((get_pos_y()) == (total_side_length_positional % 2 == 1)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for bl_moves_remaining in range(bl_moves_remaining):
			#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
			#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

			#1.
			if ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
			elif ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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

			#3.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#3.	
				elif can_harvest() != True:
				
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#3.	
				elif can_harvest() != True:
				
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#11.
	elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (total_side_length_positional % 2 == 0)) and ((get_pos_y()) == (total_side_length_positional % 2 == 0)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for tro_moves_remaining in range(tro_moves_remaining):
			#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
			#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

			#1.
			if ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#2.
			elif ((get_pos_x() == (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#3.
			elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#12.
	elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (total_side_length_positional % 2 == 1)) and ((get_pos_y()) == (total_side_length_positional % 2 == 1)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for bl_moves_remaining in range(bl_moves_remaining):
			#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
			#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

			#1.
			if ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
			elif ((get_pos_x() == (0) or (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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

			#3.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south

				#3.	
				elif can_harvest() != True:
				
					move(South)
					current_set = bl_set
					past_move = south
					current_move = south
					next_move = south
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if get_ground_type() == Grounds.Grassland and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north

				#3.	
				elif can_harvest() != True:
				
					move(East)
					current_set = bl_set
					past_move = south
					current_move = east
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

	#13.
	elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (total_side_length_positional % 2 == 1)) and ((get_pos_y()) == (total_side_length_positional % 2 == 0)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for tro_moves_remaining in range(tro_moves_remaining):
			#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
			#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

			#1.
			if ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#2.
			elif ((get_pos_x() == (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#3.
			elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0
		
	#14.
	elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (total_side_length_positional % 2 == 0)) and ((get_pos_y()) == (total_side_length_positional % 2 == 1)))):
		#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

		#1.
		for tro_moves_remaining in range(tro_moves_remaining):
			#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
			#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
			#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
			#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

			#1.
			if ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(West)
					current_set = tro_set
					past_move = west
					current_move = west
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#2.
			elif ((get_pos_x() == (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = west
					current_move = south
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#3.
			elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east

				#3.	
				elif (can_harvest() != True):
				
					move(East)
					current_set = tro_set
					past_move = east
					current_move = east
					next_move = east
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0

			#4.
			elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
				#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west

				#3.	
				elif (can_harvest() != True):
				
					move(South)
					current_set = tro_set
					past_move = east
					current_move = south
					next_move = west
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0
