from all_variables import *

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
tro_block = ((total_side_length % 2 == 1) and tr_block)     # A block representing the Top-right-odd "Starting Point" set. (odd farm size).

# Assigning "Starting Points" set variables with corresponding numbers.
bl_set = 0 		# Bottom-left set.
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

if (((even_farmland == True) or (odd_farmland == True)) and not (bl_block or br_block or tr_block or tl_block or tro_block)):
			#1. Checks to see if the farmland has an "even side length" amount of blocks and not on a specific "Starting Point" block.
			#2. Checks to see if the farmland has an "odd side length" amount of blocks and not on a specific "Starting Point" block.			

			#1.
			if (even_farmland == True):
				#1. Moves the drone the remaining moves required to compelete a Bottom-left set.
				#2. Moves the drone the remaining moves required to compelete a Bottom-right set.
				#3. Moves the drone the remaining moves required to compelete a Top-right set.
				#4. Moves the drone the remaining moves required to compelete a Top-left set.
				
				#1
				if ((x == ((0) or (total_side_length_positional % 2 == 0))) and (y == ((0) or (total_side_length_positional % 2 == 0)))): 
					#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
					
					#1.
					for bl_moves_remaining in range(bl_moves_remaining):
						#1. Executing the remaining moves for the Bottom-left set. This indicates the first statement of the set-rotation.
						#2. Executing the remaining moves for the Bottom-left set. This indicates the second statement of the set-rotation.
						#3. Executing the remaining moves for the Bottom-left set. This indicates the third statement of the set-rotation.
						#4. Executing the remaining moves for the Bottom-left set. This indicates the fourth statement of the set-rotation.
						
						#1.
						if ((get_pos_x() == ((0) or (total_side_length_positional % 2 == 0))) and (get_pos_y() != (total_side_length_positional))):
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
						elif ((get_pos_x() == ((0) or (total_side_length_positional % 2 == 0))) and (get_pos_y() == (total_side_length_positional))):
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
				elif ((x == (total_side_length_positional % 2 == 1)) and (y == ((0) or (total_side_length_positional % 2 == 0)))): #brc2
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
						
						#1.
						for br_moves_remaining in range(br_moves_remaining):
							#1. Executing the remaining moves for the Bottom-right set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Bottom-right set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Bottom-right set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Bottom-right set. This indicates the fourth statement of the set-rotation.
							
							#1.
							if ((get_pos_x() != (0)) and (get_pos_y() == ((0) or (total_side_length_positional % 2 == 0)))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == ((0) or (total_side_length_positional % 2 == 0)))):
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
							elif ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
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
				elif ((x == (total_side_length_positional % 2 == 1)) and (y == (total_side_length_positional % 2 == 1))): #trc3
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
						
						#1.
						for tr_moves_remaining in range(tr_moves_remaining):
							#1. Executing the remaining moves for the Top-right set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-right set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-right set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-right set. This indicates the fourth statement of the set-rotation.
							
							#1.
							if ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() != (0))):
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
							elif ((get_pos_x() == (total_side_length_positional % 2 == 1)) and (get_pos_y() == (0))):
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
							elif ((get_pos_x() == ((0) or (total_side_length_positional % 2 == 0))) and (get_pos_y() != (total_side_length_positional))):
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
							elif ((get_pos_x() == (total_side_length_positional % 2 == 0)) and (get_pos_y() == (total_side_length_positional))):
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
				elif ((x == ((0) or (total_side_length_positional % 2 == 0))) and (y == (total_side_length_positional % 2 == 1))): #tlc4
						#1. A Loop to move the drone the remaining moves to reach a "Starting Point".
						
						#1.
						for tl_moves_remaining in range(tl_moves_remaining):
							#1. Executing the remaining moves for the Top-left set. This indicates the first statement of the set-rotation.
							#2. Executing the remaining moves for the Top-left set. This indicates the second statement of the set-rotation.
							#3. Executing the remaining moves for the Top-left set. This indicates the third statement of the set-rotation.
							#4. Executing the remaining moves for the Top-left set. This indicates the fourth statement of the set-rotation.
							
							#1.
							if ((get_pos_x() != (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
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
							elif ((get_pos_x() == (total_side_length_positional)) and (get_pos_y() == (total_side_length_positional % 2 == 1))):
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
							elif ((get_pos_x() != (0)) and (get_pos_y() == (total_side_length_positional % 2 == 0))):
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
							elif ((get_pos_x() == (0)) and (get_pos_y() == ((0) or (total_side_length_positional % 2 == 0)))):
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
			elif (odd_farmland == True):
					#1. Moves the drone the remaining moves required to compelete the Bottom-left set.      (lucky middle, x and y is odd)
					#2. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (lucky middle, x and y is even)
					#3. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (Diagonal TLBR line, x > y, x and y is even)
					#4. Moves the drone the remaining moves required to compelete the Bottom-left set.      (Diagonal TLBR line, x > y, x and y is odd)
					#5. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (Diagonal TLBR line, x < y, x and y is even)
					#6. Moves the drone the remaining moves required to compelete the Bottom-left set.      (Diagonal TLBR line, x < y, x and y is odd)
					#7. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (Below the diagonal TLBR line, drone on even blocks)
					#8. Moves the drone the remaining moves required to compelete the Bottom-left set.      (Below the diagonal TLBR line, drone on odd blocks)
					#9. Moves the drone the remaining moves required to compelete the Top-right-odd set.    (Above the diagonal TLBR line, drone on even blocks)
					#10. Moves the drone the remaining moves required to compelete the Bottom-left set.     (Above the diagonal TLBR line, drone on odd blocks)

					#1.
					if ((((x) + (y)) == (total_side_length_positional)) and (((x) and (y)) == (total_side_length_positional % 2 == 0))):
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
					elif ((((x) + (y)) == (total_side_length_positional)) and (((x) and (y)) == (total_side_length_positional % 2 == 1))):
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
					elif ((((x) + (y)) == (total_side_length_positional)) and ((x) > (y)) and (((x) == (total_side_length_positional % 2 == 0)) and ((y) == ((0) or (total_side_length_positional % 2 == 0))))):
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
					elif ((((x) + (y)) == (total_side_length_positional)) and ((x) > (y)) and (((x) == (total_side_length_positional % 2 == 1)) and ((y) == (total_side_length_positional % 2 == 1)))):
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
					elif ((((x) + (y)) == (total_side_length_positional)) and ((x) < (y)) and (((x) == ((0) or (total_side_length_positional % 2 == 0))) and ((y) == (total_side_length_positional % 2 == 0)))):
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
					elif ((((x) + (y)) == (total_side_length_positional)) and ((x) < (y)) and (((x) == (total_side_length_positional % 2 == 1)) and ((y) == (total_side_length_positional % 2 == 1)))):
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
					elif ((((x) + (y)) < (total_side_length_positional)) and (((x) == (0) or (total_side_length_positional % 2 == 0)) and ((y) == (0) or (total_side_length_positional % 2 == 0)))):
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
					elif ((((x) + (y)) < (total_side_length_positional)) and (((x) == (total_side_length_positional % 2 == 1)) and ((y) == (total_side_length_positional % 2 == 1)))):
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
					elif ((((x) + (y)) > (total_side_length_positional)) and (((x) == (total_side_length_positional % 2 == 0)) and ((y) == (total_side_length_positional % 2 == 0)))):
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

					#10.
					elif ((((x) + (y)) > (total_side_length_positional)) and (((x) == (total_side_length_positional % 2 == 1)) and ((y) == (total_side_length_positional % 2 == 1)))):
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
