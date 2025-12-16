from __builtins__ import *

# Drone locator and farmland size
x = get_pos_x()
y = get_pos_y()
drone = x,y
total_side_length = get_world_size()
zero = 0
total_side_length_positional = (get_world_size() - 1)

# Assigning blocks to the "Starting Points" of the sets.
top_side = (get_pos_y() == total_side_length_positional)
bottom_side = (get_pos_y() == zero)
left_side = (get_pos_x() == zero)
right_side = (get_pos_x() == total_side_length_positional)
tl_block = (top_side and left_side) 	                    # A block representing the Top-left "Starting Point" set.
tr_block = (top_side and right_side) 	                    # A block representing the Top-right "Starting Point" set.
bl_block = (bottom_side and left_side) 	                    # A block representing the Bottom-left "Starting Point" set.
br_block = (bottom_side and right_side)	                    # A block representing the Bottom-right "Starting Point" set.
blo_block = ((total_side_length % 2 == 1) and (bl_block))	# A block representing the Bottom-left-odd "Starting Point" set. (odd farm size).
tro_block = ((total_side_length % 2 == 1) and (tr_block))   # A block representing the Top-right-odd "Starting Point" set. (odd farm size).

# Assigning "Starting Points" set variables with corresponding numbers.
bl_set = 0		# Bottom-left set.
blo_set = 0 	# Bottom-left set.
br_set = 1 		# Bottom-right set.
tr_set = 2 		# Top-right set.
tro_set = 2     # Top-right-odd set.
tl_set = 3 		# Top-left set.

# Set and Direction system.
current_set = 0	# Current set indicator.
past_move = ''		# Past move indicator.
current_move = ''	# Current move indicator.
next_move = ''		# Next move indicator.
reset = 'Reset'
north = 'North'
south = 'South'
east = 'East'
west = 'West'

even_farmland = (total_side_length % 2 == 0)
even_farmland_set_rotation_count = ((even_farmland == True) and (4))
odd_farmland = (total_side_length % 2 == 1)
odd_farmland_set_rotation_count = ((odd_farmland == True) and (2))
detection_of_unharvested_crop_during_main_harvesting_rotaion = 0
harvesting_rotations = ((even_farmland_set_rotation_count) or (odd_farmland_set_rotation_count))
remaining_harvesting_rotations = (harvesting_rotations - current_set)
main_harvesting_rotations = (remaining_harvesting_rotations)
number_of_required_set_rotations = (get_world_size() // 2)

desired_rotations_for_when_detection_of_farmland_not_harvested = 2
desired_rotations_positional = ((desired_rotations_for_when_detection_of_farmland_not_harvested) - (1))
live_rotation_counter = 0

# The Remaining Moves system.
required_moves_per_rotation = (total_side_length ** 2)

run = 0
# A conditional loop to 'check plant type or check ground type'
while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrot or Grounds.Soil or Grounds.Grassland and run < 1:
	run = run
	#1. Checks for the detection of an un-harvested crop during the main rotation.
	#2. Creates a temporary loop when (#1) is false, to rotate again until a desired number of required rotations are finished.
	#3. Breaks the temporary loop after reaching the desired rotations (#2).

	##
	##
	# Starting at bottom_right (bl) move calculator. (HARVEST at end of set required)
	bl_full_column_moved_x = (get_pos_x() * total_side_length)
	bl_moves = (((bl_full_column_moved_x % 2 == 0) and (get_pos_y() + 1)) or (((bl_full_column_moved_x > 0) and (bl_full_column_moved_x % 2 == 1)) and (total_side_length - get_pos_y())))
	bl_moves_completed = ((bl_full_column_moved_x) + (bl_moves))
	bl_moves_remaining = (required_moves_per_rotation - bl_moves_completed)
	
	# Starting at bottom_right (br) move calculator. (HARVEST at end of set required)
	br_full_row_moved_y = (get_pos_y() * total_side_length)
	br_moves = (((br_full_row_moved_y % 2 == 0) and (total_side_length - get_pos_x())) or (((br_full_row_moved_y > 0) and (br_full_row_moved_y % 2 == 1)) and (get_pos_x() + 1)))
	br_moves_completed = ((br_full_row_moved_y) + (br_moves))
	br_moves_remaining = (required_moves_per_rotation - br_moves_completed)
	
	# Starting at top_right (tr) move calculator. (HARVEST at end of set required)
	tr_full_column_moved_x = ((total_side_length_positional - get_pos_x()) * (total_side_length))
	tr_moves = (((tr_full_column_moved_x % 2 == 0) and (total_side_length - get_pos_y())) or (((tr_full_column_moved_x > 0) and (tr_full_column_moved_x % 2 == 1)) and (get_pos_y() + 1)))
	tr_moves_completed = ((tr_full_column_moved_x) + (tr_moves))
	tr_moves_remaining = (required_moves_per_rotation - tr_moves_completed)
	
	# Starting at top_right_odd (tro) move calculator. (HARVEST at end of set required)
	tro_full_column_moved_y = ((total_side_length_positional - get_pos_y()) * (total_side_length))
	tro_moves = (((tro_full_column_moved_y % 2 == 0) and (total_side_length - get_pos_x())) or (((tro_full_column_moved_y > 0) and (tro_full_column_moved_y % 2 == 1)) and (get_pos_x() + 1)))
	tro_moves_completed = ((tro_full_column_moved_y) + (tro_moves))
	tro_moves_remaining = (required_moves_per_rotation - tro_moves_completed)
	
	# Starting at top_left (tl) move calculator. (HARVEST at end of set required)
	tl_full_column_moved_y = ((total_side_length_positional - get_pos_y()) * (total_side_length))
	tl_moves = (((tl_full_column_moved_y % 2 == 0) and (get_pos_x() + 1)) or ((tl_full_column_moved_y > 0) and (tl_full_column_moved_y % 2 == 1) and ((total_side_length_positional - get_pos_x()) + (1))))
	tl_moves_completed = ((tl_full_column_moved_y) + (tl_moves))
	tl_moves_remaining = (required_moves_per_rotation - tl_moves_completed)
	##
	##

	#1.
	if detection_of_unharvested_crop_during_main_harvesting_rotaion == 0:
		#1. Checks to see if the farmland has an "even or odd side length" amount of blocks and is not on a specific "Starting Point" block, after detecting the position of the drone. Then uses 'The Remaining Moves system' to compelete the set and end on a "Starting Point".
		#2. Checks to see if the farmland has an "even side length" amount of blocks and on a specific "Starting Point" block. If true then, starts an "even-sided farmland" route. (Even corners)
		#3. Checks to see if the farmland has an "odd side length" amount of blocks and on a specific "Starting Point" block. If true then, starts an "odd-sided farmland" route. (odd corners)
			
		#1.
		if (((even_farmland == True) or (odd_farmland == True)) and not (bl_block or br_block or tr_block or tl_block or blo_block or tro_block)):
			#1. Checks to see if the farmland has an "even side length" amount of blocks and not on a specific "Starting Point" block.
			#2. Checks to see if the farmland has an "odd side length" amount of blocks and not on a specific "Starting Point" block.			

			#1.
			if (even_farmland == True):
				#1. Moves the drone the remaining moves required to compelete a Bottom-left set.
				#2. Moves the drone the remaining moves required to compelete a Bottom-right set.
				#3. Moves the drone the remaining moves required to compelete a Top-right set.
				#4. Moves the drone the remaining moves required to compelete a Top-left set.
				
				#1
				if ((get_pos_x() == ((0) or (get_pos_x() % 2 == 0))) and (get_pos_y() == ((0) or (get_pos_y() % 2 == 0)))): 
					#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
					
					#1.
					for bl_moves_remaining in range(bl_moves_remaining):
						#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
						#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation.
						#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
						#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation.
						
						#1.
						if ((get_pos_x() == ((0) or (get_pos_x() % 2 == 0))) and (get_pos_y() != (total_side_length_positional))):
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
						elif ((get_pos_x() == ((0) or (get_pos_x() % 2 == 0))) and (get_pos_y() == (total_side_length_positional))):
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
						elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
						elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
				elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == ((0) or (get_pos_y() % 2 == 0)))): #brc2
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
						
						#1.
						for br_moves_remaining in range(br_moves_remaining):
							#1. Executing the remaining moves for the Bottom-right set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-right set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Bottom-right set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-right set. This indicates the fourth statement of the set-rotation.
							
							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == ((0) or (get_pos_y() % 2 == 0)))):
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
							
							#2.
							elif ((get_pos_x() == (0)) and (get_pos_y() == ((0) or (get_pos_y() % 2 == 0)))):
								#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system
								
								#1.
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(North)
									current_set = br_set
									past_move = west
									current_move = north
									next_move = east
								
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(North)
									current_set = br_set
									past_move = west
									current_move = north
									next_move = east
								
								#3.	
								elif can_harvest() != True:
								
									move(North)
									current_set = br_set
									past_move = west
									current_move = north
									next_move = east
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#3.
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
								#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(East)
									current_set = br_set
									past_move = east
									current_move = east
									next_move = east
								
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(East)
									current_set = br_set
									past_move = east
									current_move = east
									next_move = east
								
								#3.	
								elif can_harvest() != True:
								
									move(East)
									current_set = br_set
									past_move = east
									current_move = east
									next_move = east
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#4.
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
								#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system
								
								#1.
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(North)
									current_set = br_set
									past_move = east
									current_move = north
									next_move = west
								
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(North)
									current_set = br_set
									past_move = east
									current_move = north
									next_move = west
								
								#3.	
								elif can_harvest() != True:
								
									move(North)
									current_set = br_set
									past_move = east
									current_move = north
									next_move = west
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
				
				#3.
				elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (get_pos_y() % 2 == 1))): #trc3
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
						
						#1.
						for tr_moves_remaining in range(tr_moves_remaining):
							#1. Executing the remaining moves for the Top-right set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right set. This indicates the fourth statement of the set-rotation.
							
							#1.
							if ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
								#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(South)
									current_set = tr_set
									past_move = south
									current_move = south
									next_move = south
								
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
								
										harvest() # Plants grass automatically if ground is a Grassland.	
										till()
										move(South)
										current_set = tr_set
										past_move = south
										current_move = south
										next_move = south
								
								#3.	
								elif can_harvest() != True:
								
									move(South)
									current_set = tr_set
									past_move = south
									current_move = south
									next_move = south
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#2.
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
								#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(West)
									current_set = tr_set
									past_move = south
									current_move = west
									next_move = north
								
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(West)
									current_set = tr_set
									past_move = south
									current_move = west
									next_move = north
								
								#3.	
								elif (can_harvest() != True):
								
									move(West)
									current_set = tr_set
									past_move = south
									current_move = west
									next_move = north
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#3.
							elif ((get_pos_x() == ((0) or (get_pos_x() % 2 == 0))) and (get_pos_y() != (total_side_length_positional))):
								#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(North)
									current_set = tr_set
									past_move = north
									current_move = north
									next_move = north
								
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(North)
									current_set = tr_set
									past_move = north
									current_move = north
									next_move = north
								
								#3.	
								elif (can_harvest() != True):
								
									move(North)
									current_set = tr_set
									past_move = north
									current_move = north
									next_move = north
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#4.
							elif ((get_pos_x() == (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
								#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(West)
									current_set = tr_set
									past_move = north
									current_move = west
									next_move = south
								
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(West)
									current_set = tr_set
									past_move = north
									current_move = west
									next_move = south
								
								#3.	
								elif (can_harvest() != True):
								
									move(West)
									current_set = tr_set
									past_move = north
									current_move = west
									next_move = south
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
				
				#4.
				elif ((get_pos_x() == ((0) or (get_pos_x() % 2 == 0))) and (get_pos_y() == (get_pos_y() % 2 == 1))): #tlc4
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
						
						#1.
						for tl_moves_remaining in range(tl_moves_remaining):
							#1. Executing the remaining moves for the Top-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-left set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-left set. This indicates the fourth statement of the set-rotation.
							
							#1.
							if ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
								#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(East)
									current_set = tl_set
									past_move = east
									current_move = east
									next_move = east
								
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(East)
									current_set = tl_set
									past_move = east
									current_move = east
									next_move = east
								
								#3.	
								elif can_harvest() != True:
								
									move(East)
									current_set = tl_set
									past_move = east
									current_move = east
									next_move = east
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#2.
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
								#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(South)
									current_set = tl_set
									past_move = east
									current_move = south
									next_move = west
								
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(South)
									current_set = tl_set
									past_move = east
									current_move = south
									next_move = west
								
								#3.	
								elif (can_harvest() != True):
								
									move(South)
									current_set = tl_set
									past_move = east
									current_move = south
									next_move = west
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#3.
							elif ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
								#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(West)
									current_set = tl_set
									past_move = west
									current_move = west
									next_move = west
								
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(West)
									current_set = tl_set
									past_move = west
									current_move = west
									next_move = west
								
								#3.	
								elif (can_harvest() != True):
								
									move(West)
									current_set = tl_set
									past_move = west
									current_move = west
									next_move = west
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#4.
							elif ((get_pos_x() == (0)) and (get_pos_y() == ((0) or (get_pos_y() % 2 == 0)))):
								#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
								
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.
									move(South)
									current_set = tl_set
									past_move = west
									current_move = south
									next_move = east
								
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
								
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(South)
									current_set = tl_set
									past_move = west
									current_move = south
									next_move = east
								
								#3.	
								elif (can_harvest() != True):
								
									move(South)
									current_set = tl_set
									past_move = west
									current_move = south
									next_move = east
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0			

			#2.
			elif (odd_farmland == True): # Odd & Even based on block number, not positional *
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
							if ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
							if ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
					elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) > (get_pos_y())) and (((get_pos_x()) == (get_pos_x() % 2 == 0)) and ((get_pos_y()) == ((0) or (get_pos_y() % 2 == 0))))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for tro_moves_remaining in range(tro_moves_remaining):
							#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
					elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) > (get_pos_y())) and (((get_pos_x()) == (get_pos_x() % 2 == 1)) and ((get_pos_y()) == (get_pos_y() % 2 == 1)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for bl_moves_remaining in range(bl_moves_remaining):
							#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
							#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

							#1.
							if ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
					elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) < (get_pos_y())) and (((get_pos_x()) == ((0) or (get_pos_x() % 2 == 0))) and ((get_pos_y()) == (get_pos_y() % 2 == 0)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for tro_moves_remaining in range(tro_moves_remaining):
							#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
					elif ((((get_pos_x()) + (get_pos_y())) == (total_side_length_positional)) and ((get_pos_x()) < (get_pos_y())) and (((get_pos_x()) == (get_pos_x() % 2 == 1)) and ((get_pos_y()) == (get_pos_y() % 2 == 1)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for bl_moves_remaining in range(bl_moves_remaining):
							#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
							#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

							#1.
							if ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
					elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (0) or (get_pos_x() % 2 == 0)) and ((get_pos_y()) == (0) or (get_pos_y() % 2 == 0)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for tro_moves_remaining in range(tro_moves_remaining):
							#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
					elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (get_pos_x() % 2 == 1)) and ((get_pos_y()) == (get_pos_y() % 2 == 1)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for bl_moves_remaining in range(bl_moves_remaining):
							#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
							#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

							#1.
							if ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
					elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (get_pos_x() % 2 == 1)) and ((get_pos_y()) == (get_pos_y() % 2 == 0)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for bl_moves_remaining in range(bl_moves_remaining):
							#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
							#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

							#1.
							if ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
					elif ((((get_pos_x()) + (get_pos_y())) < (total_side_length_positional)) and (((get_pos_x()) == (get_pos_x() % 2 == 0)) and ((get_pos_y()) == (get_pos_y() % 2 == 1)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for bl_moves_remaining in range(bl_moves_remaining):
							#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
							#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

							#1.
							if ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
					elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (get_pos_x() % 2 == 0)) and ((get_pos_y()) == (get_pos_y() % 2 == 0)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for tro_moves_remaining in range(tro_moves_remaining):
							#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
					elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (get_pos_x() % 2 == 1)) and ((get_pos_y()) == (get_pos_y() % 2 == 1)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for bl_moves_remaining in range(bl_moves_remaining):
							#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation
							#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation

							#1.
							if ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (0) or (get_pos_x() % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (get_pos_x() % 2 == 1)) and (get_pos_y() == (0))):
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
					elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (get_pos_x() % 2 == 1)) and ((get_pos_y()) == (get_pos_y() % 2 == 0)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for tro_moves_remaining in range(tro_moves_remaining):
							#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
					elif ((((get_pos_x()) + (get_pos_y())) > (total_side_length_positional)) and (((get_pos_x()) == (get_pos_x() % 2 == 0)) and ((get_pos_y()) == (get_pos_y() % 2 == 1)))):
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".

						#1.
						for tro_moves_remaining in range(tro_moves_remaining):
							#1. Executing the remaining moves for the Top-right-odd set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right-odd set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right-odd set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right-odd set. This indicates the fourth statement of the set-rotation.

							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == (get_pos_y() % 2 == 0))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (get_pos_y() % 2 == 1))):
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
			
		#2.
		if ((even_farmland == True) and (bl_block or br_block or tr_block or tl_block)):
			#1. Checks to see if the drone is on a "Starting Point" of this set, which is on the bottom-left block. The route of this set is North -> East -> South.
			#2. Checks to see if the drone is on a "Starting Point" of this set, which is on the bottom-right block. The route of this set is West -> North -> East.
			#3. Checks to see if the drone is on a "Starting Point" of this set, which is on the top-right block. The route of this set is South -> West -> North.
			#4. Checks to see if the drone is on a "Starting Point" of this set, which is on the top-left block. The route of this set is East -> South -> West.
			
			#1.
			if (bl_block):
				#1. Updates the current set value in the direction system.
				#2. The main harvesting rotation loop from a "Starting Point" block.
				#3. Updates the direction system (indicating that the drone has reached the 'End Point' of the current set and completed a "Full even-set-rotation", which means the next move is from a new set).

				#1.
				current_set = bl_set

				#2.
				for main_harvesting_rotations in range(main_harvesting_rotations):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at a set's 'Starting Point' and ends at it's 'Ending Point'.

					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations):
						#1. A loop that moves the drone in the North direction until it reaches the top of the farmland.
						#2. A loop that moves the drone in the East direction.
						#3. A loop that moves the drone in the South direction until it reaches the bottom of the farmland.
						#4. A Conditional loop that either moves in the East direction or moves to the next set-route.
													
						#1.
						for north_moves in range(total_side_length_positional - get_pos_y()):
							#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(North)
								past_move = north
								current_move = north
								next_move = north
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a TGrassland.	
								till()
								move(North)
								past_move = north
								current_move = north
								next_move = north
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(North)
								past_move = north
								current_move = north
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
							
						#2.
						for east_moves in range(1):
							#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
							
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
								harvest() # Plants grass automatically if ground is a Grassland.
								move(East)
								past_move = north
								current_move = east
								next_move = south
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(East)
								past_move = north
								current_move = east
								next_move = south
															
							#3.	
							elif can_harvest() != True:
															
								move(East)
								past_move = north
								current_move = east
								next_move = south
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
			
						#3.							
						for south_moves in range(get_pos_y()):
							#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(South)
								past_move = south
								current_move = south
								next_move = south
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(South)
								past_move = south
								current_move = south
								next_move = south
																	
							#3.	
							elif can_harvest() != True:
																	
								move(South)
								past_move = south
								current_move = south
								next_move = south
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for east_moves in range(1):
							#1. Checks to see if the drone is able to move in the East direction, which also indicates the end of a "Set-rotation".
							#2.	Moves on to the next 'Starting Point'.

							#1.
							if (get_pos_x() < total_side_length_positional):
								#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
								#1.						
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
									harvest() # Plants grass automatically if ground is a Grassland.
									move(East)
									past_move = south
									current_move = east
									next_move = north
																
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(East)
									#current_set = bl_set
									past_move = south
									current_move = east
									next_move = north
																
								#3.	
								elif can_harvest() != True:
																	
									move(East)
									past_move = south
									current_move = east
									next_move = north
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0

							#2.		
							else:

								pass

				#3.
				past_move = south
				current_move = reset
				next_move = west
					
			#2.	
			elif (br_block):
				#1. Updates the current set value in the direction system.
				#2. The main harvesting rotation loop from a "Starting Point" block.					
				#3. Updates the direction system (indicating that the drone has reached the 'End Point' of the current set and completed a "Full even-set-rotation", which means the next move is from a new set).

				#1.
				current_set = br_set
				
				#2.
				for main_harvesting_rotations in range(main_harvesting_rotations):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at a set's 'Starting Point' and ends at it's 'Ending Point'.

					#1
					for number_of_required_set_rotations in range(number_of_required_set_rotations):
						#1. A loop that moves the drone in the West direction until it reaches the left side of the farmland.
						#2. A loop that moves the drone in the North direction.
						#3. A loop that moves the drone in the East direction until it reaches the right side of the farmland.
						#4. A Conditional loop that either moves in the North direction or moves to the next set-route.
							
						#1.
						for west_moves in range(get_pos_x()):
							#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(West)
								past_move = west
								current_move = west
								next_move = west
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(West)
								
								past_move = west
								current_move = west
								next_move = west
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(West)
								past_move = west
								current_move = west
								next_move = west
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
							
						#2.
						for north_moves in range(1):
							#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
								harvest() # Plants grass automatically if ground is a Grassland.
								move(North)
								past_move = west
								current_move = north
								next_move = east
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(North)

								past_move = west
								current_move = north
								next_move = east
															
							#3.	
							elif can_harvest() != True:
															
								move(North)
								past_move = west
								current_move = north
								next_move = east
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
			
						#3.							
						for east_moves in range(total_side_length_positional - get_pos_x()):
							#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(East)
								past_move = east
								current_move = east
								next_move = east
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(East)

								past_move = east
								current_move = east
								next_move = east
																	
							#3.	
							elif can_harvest() != True:
																	
								move(East)
								past_move = east
								current_move = east
								next_move = east
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for north_moves in range(1):
							#1. Checks to see the if the drone is able to move in the North direction, which also indicates the end of a "Set-rotation".
							#2.	Moves on to the next 'Starting Point'.

							#1
							if (get_pos_y() < total_side_length_positional):
								#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
								#1.						
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
									harvest() # Plants grass automatically if ground is a Grassland.
									move(North)
									past_move = east
									current_move = north
									next_move = west
																
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(North)
									past_move = east
									current_move = north
									next_move = west
																
								#3.	
								elif can_harvest() != True:
																	
									move(North)
									past_move = east
									current_move = north
									next_move = west
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#2.		
							else:

								pass

				#3.
				past_move = east
				current_move = reset
				next_move = south
				
			#3.	
			elif (tr_block):
				#1. Updates the current set value in the direction system.
				#2. The main harvesting rotation loop from a "Starting Point" block.
				#3. Updates the direction system (indicating that the drone has reached the 'End Point' of the current set and completed a "Full even-set-rotation", which means the next move is from a new set).
				
				#1.
				current_set = tr_set

				#2.
				for main_harvesting_rotations in range(main_harvesting_rotations):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at a set's 'Starting Point' and ends at it's 'Ending Point'.

					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations):
						#1. A loop that moves the drone in the South direction until it reaches the left side of the farmland.
						#2. A loop that moves the drone in the West direction.
						#3. A loop that moves the drone in the North direction until it reaches the right side of the farmland.
						#4. A Conditional loop that either moves in the West direction or moves to the next set-route.
							
						#1.							
						for south_moves in range(get_pos_y()):
							#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(South)
								past_move = south
								current_move = south
								next_move = south
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(South)
								past_move = south
								current_move = south
								next_move = south
																	
							#3.	
							elif can_harvest() != True:
																	
								move(South)
								past_move = south
								current_move = south
								next_move = south
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
							
						#2.
						for west_moves in range(1):
							#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(West)
								past_move = south
								current_move = west
								next_move = north
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(West)
								past_move = south
								current_move = west
								next_move = north
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(West)
								past_move = south
								current_move = west
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
			
						#3.
						for north_moves in range(total_side_length_positional - get_pos_y()):
							#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(North)
								past_move = north
								current_move = north
								next_move = north
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(North)
								past_move = north
								current_move = north
								next_move = north
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(North)
								past_move = north
								current_move = north
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for west_moves in range(1):
							#1. Checks to see the if the drone is able to move in the West direction, which also indicates the end of a "Set-rotation".
							#2.	Moves on to the next 'Starting Point'.

							#1
							if (get_pos_x() > 0):
								#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
									harvest() # Plants grass automatically if ground is a Grassland.
									move(West)
									past_move = north
									current_move = west
									next_move = south
																	
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(West)
									past_move = north
									current_move = west
									next_move = south
																	
								#3.	
								elif (can_harvest() != True):
																	
									move(West)
									past_move = north
									current_move = west
									next_move = south
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
									
							#2.		
							else:
								
								pass
					
				#3.
				past_move = north
				current_move = reset
				next_move = east
								
			#4.	
			elif (tl_block):
				#1. Updates the current set value in the direction system.
				#2. The main harvesting rotation loop from a "Starting Point" block.
				#3. Updates the direction system (indicating that the drone has reached the 'End Point' of the current set and completed a "Whole rotation" in regards with the even 'Starting Points').

				#1.
				current_set = tl_set

				#2.
				for main_harvesting_rotations in range(main_harvesting_rotations):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at a set's 'Starting Point' and ends at it's 'Ending Point'.

					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations):
						#1. A loop that moves the drone in the East direction until it reaches the left side of the farmland.
						#2. A loop that moves the drone in the South direction.
						#3. A loop that moves the drone in the West direction until it reaches the right side of the farmland.
						#4. A Conditional loop that either moves in the South direction or makes the drone harvest and stop.
							
						#1.							
						for east_moves in range(total_side_length_positional - get_pos_x()):
							#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(East)
								past_move = east
								current_move = east
								next_move = east
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(East)
								past_move = east
								current_move = east
								next_move = east
																	
							#3.	
							elif can_harvest() != True:
																	
								move(East)
								past_move = east
								current_move = east
								next_move = east
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
							
						#2.
						for south_moves in range(1):
							#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(South)
								past_move = east
								current_move = south
								next_move = west
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(South)
								past_move = east
								current_move = south
								next_move = west
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(South)
								past_move = east
								current_move = south
								next_move = west
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
			
						#3.
						for west_moves in range(get_pos_x()):
							#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(West)
								past_move = west
								current_move = west
								next_move = west
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(West)
								past_move = west
								current_move = west
								next_move = west
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(West)
								past_move = west
								current_move = west
								next_move = west
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for south_moves in range(1):
							#1. Checks to see the if the drone is able to move in the South direction, which also indicates the end of a "Set-rotation".
							#2.	When (#1) is false, the drone harvests and does not move, which also indicates the end of a "Full-even-rotation".

							#1
							if (get_pos_y() > 0):
								#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
								#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
								#1.
								if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
									harvest() # Plants grass automatically if ground is a Grassland.
									move(South)
									past_move = west
									current_move = south
									next_move = east
																	
								#2.	
								elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									move(South)
									past_move = west
									current_move = south
									next_move = east
																	
								#3.	
								elif (can_harvest() != True):
																	
									move(South)
									past_move = west
									current_move = south
									next_move = east
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
							
							#2.		
							else:
								#1. Drone does not move after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Drone does not move after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Drone does not move after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
								#1.						
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
									harvest() # Plants grass automatically if ground is a Grassland.
									past_move = west
									current_move = reset
									next_move = north
																
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									past_move = west
									current_move = reset
									next_move = north
																
								#3.	
								elif can_harvest() != True:
																	
									past_move = west
									current_move = reset
									next_move = north
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
					
				#3.
				past_move = west
				current_move = reset
				next_move = north

		#3.
		if ((odd_farmland == True) and (blo_block or tro_block)):
			#1. Checks to see if the drone is on a "Starting Point" of this set, which is on the bottom-left block. The route of this set is North -> East -> South -> East ->
			#2. Checks to see if the drone is on a "Starting Point" of this set, which is on the top-right block. The route of this set is South -> West -> North.
			
			#1.
			if (blo_block):
				#1. Updates the current set value in the direction system.
				#2. The main harvesting rotation loop from a "Starting Point" block.
				#3. A loop that moves the drone in the North direction and reaches the 'End Point' of the current set.
				#4. Updates the direction system (indicating that the drone has reached the 'End Point' of this set and completed a "Full odd-set-rotation", which means the next move is from a new set).

				#1.
				current_set = bl_set

				#2.
				for main_harvesting_rotations in range(main_harvesting_rotations):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at the set's 'Starting Point' and ends after a full 'Set-rotation'.

					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations):
						#1. A loop that moves the drone in the North direction until it reaches the top of the farmland.
						#2. A loop that moves the drone in the East direction.
						#3. A loop that moves the drone in the South direction until it reaches the bottom of the farmland.
						#4. A loop that moves the drone in the East direction.
						
						#1.
						for north_moves in range(total_side_length_positional - get_pos_y()):
							#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
							
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(North)
								past_move = north
								current_move = north
								next_move = north
							
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a TGrassland.	
								till()
								move(North)
								past_move = north
								current_move = north
								next_move = north
							
							#3.	
							elif (can_harvest() != True):
							
								move(North)
								past_move = north
								current_move = north
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
						
						#2.
						for east_moves in range(1):
							#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
							
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(East)
								past_move = north
								current_move = east
								next_move = south
							
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(East)
								past_move = north
								current_move = east
								next_move = south
							
							#3.	
							elif can_harvest() != True:
							
								move(East)
								past_move = north
								current_move = east
								next_move = south
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
						
						#3.							
						for south_moves in range(get_pos_y()):
							#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
							
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(South)
								past_move = south
								current_move = south
								next_move = south
							
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(South)
								past_move = south
								current_move = south
								next_move = south
							
							#3.	
							elif can_harvest() != True:
							
								move(South)
								past_move = south
								current_move = south
								next_move = south
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
						
						#4.
						for east_moves in range(1):
							#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
							
							#1.						
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(East)
								past_move = south
								current_move = east
								next_move = north
							
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(East)
								past_move = south
								current_move = east
								next_move = north
							
							#3.	
							elif can_harvest() != True:
							
								move(East)
								past_move = south
								current_move = east
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
					
				#3.
				for north_moves in range(total_side_length_positional):
					#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'. 
					#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
					#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".        

					#1.
					if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a Grassland.
						move(North)
						past_move = north
						current_move = north
						next_move = north                   
					
					#2.	
					elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a TGrassland.	
						till()
						move(North)
						past_move = north
						current_move = north
						next_move = north                   
					
					#3.	
					elif (can_harvest() != True):
					
						move(North)
						past_move = north
						current_move = north
						next_move = north
						detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
						main_harvesting_rotation = 0                    

				#4.                
				past_move = south
				current_move = reset
				next_move = west
			
			#2.
			elif (tro_block):
				#1. Updates the current set value in the direction system.
				#2. The main harvesting rotation loop from a "Starting Point" block.
				#3. A loop that moves the drone in the West direction and reaches the 'End Point' of the current set.
				#4. Updates the direction system (indicating that the drone has reached the 'End Point' of this set and completed a "Whole rotation").

				#1.
				current_set = tro_set
				
				#2.
				for main_harvesting_rotations in range(main_harvesting_rotations):
					#1. The main harvesting rotation loop from a "Starting Point" block.

					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations):
						#1. A loop that moves the drone in the South direction until it reaches the left side of the farmland.
						#2. A loop that moves the drone in the West direction.
						#3. A loop that moves the drone in the North direction until it reaches the right side of the farmland.
						#4. A loop that moves the drone in the West direction.
						
						#1.							
						for west_moves in range(get_pos_x()):
							#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".    

							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(West)
								past_move = west
								current_move = west
								next_move = west    

							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
							
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(West)
								past_move = west
								current_move = west
								next_move = west    

							#3.	
							elif can_harvest() != True:
							
								move(West)
								past_move = west
								current_move = west
								next_move = west
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0    
						
						#2.
						for south_moves in range(1):
							#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".    
							
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(South)
								past_move = west
								current_move = south
								next_move = east    
							
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(South)
								past_move = west
								current_move = south
								next_move = east    
							
							#3.	
							elif (can_harvest() != True):
							
								move(South)
								past_move = west
								current_move = south
								next_move = east
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0    
						
						#3.
						for east_moves in range(total_side_length_positional - get_pos_x()):
							#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".    
							
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(East)
								past_move = east
								current_move = east
								next_move = east    
							
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(East)
								past_move = east
								current_move = east
								next_move = east    
							
							#3.	
							elif (can_harvest() != True):
							
								move(East)
								past_move = east
								current_move = east
								next_move = east
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0    
						
						#4.
						for south_moves in range(1):
							#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".    
							
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a Grassland.
								move(South)
								past_move = west
								current_move = south
								next_move = east    
							
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
							
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(South)
								past_move = west
								current_move = south
								next_move = east    
							
							#3.	
							elif (can_harvest() != True):
							
								move(South)
								past_move = west
								current_move = south
								next_move = east
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0    
					
				#3.
				for west_moves in range(get_world_size()):
					#1. Checks to see the if the drone is able to move in the West direction, which also indicates the end of a "Set-rotation".
					#2.	When (#1) is false, the drone harvests and does not move, which also indicates the end of a "Full-odd-rotation".

					#1.
					if (get_pos_x() > 0):
						#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
						#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
						#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
						#1.
						if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
						
							harvest() # Plants grass automatically if ground is a Grassland.
							move(West)
							past_move = west
							current_move = west
							next_move = west
						
						#2.	
						elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
						
							harvest() # Plants grass automatically if ground is a Grassland.	
							till()
							move(West)
							past_move = west
							current_move = west
							next_move = west
						
						#3.	
						elif (can_harvest() != True):

							move(West)
							past_move = west
							current_move = west
							next_move = west
							detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
							main_harvesting_rotation = 0
						
					#2.		
					else:
						#1. Drone does not move after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
						#2. Drone does not move after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
						#3. Drone does not move after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".          
						
						#1.						
						if get_ground_type() == Grounds.Grassland and can_harvest() == True:
						
							harvest() # Plants grass automatically if ground is a Grassland.
							past_move = west
							current_move = reset
							next_move = north           
						
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
						
							harvest() # Plants grass automatically if ground is a Grassland.	
							till()
							past_move = west
							current_move = reset
							next_move = north           
						
						#3.	
						elif can_harvest() != True:
						
							past_move = west
							current_move = reset
							next_move = north
							detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
							main_harvesting_rotation = 0
			
				#4.
				past_move = west
				current_move = reset
				next_move = north

		run = 1

	#2.			
	#elif (detection_of_unharvested_crop_during_main_harvesting_rotaion > 0) and (live_rotation_counter < desired_rotations_positional): #change this
	#
	#	detection_of_unharvested_crop_during_main_harvesting_rotaion = 0
	#	main_harvesting_rotation = 1
	#	live_rotation_counter += 1
	#	live_rotation_counter = live_rotation_counter

	#3.	
	#else:
	#
	#	break												