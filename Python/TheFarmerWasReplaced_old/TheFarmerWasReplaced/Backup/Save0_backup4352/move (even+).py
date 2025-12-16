x = get_pos_x()
y = get_pos_y()
drone = x,y

total_side_length = get_world_size()
zero = (total_side_length - total_side_length)
total_side_length_positional = (get_world_size() - 1)

top_side = (y == total_side_length_positional)
bottom_side = (y == zero)
left_side = (x == zero)
right_side = (x == total_side_length_positional)

top_left_block = (top_side and left_side)
top_right_block = (top_side and right_side)
bottom_left_block = (bottom_side and left_side)
bottom_right_block = (bottom_side and right_side)

#1.
#if get_pos_x() == (total_side_length_positional - total_side_length_positional) and get_pos_y() == (total_side_length_positional - total_side_length_positional):
			
	#pass

#2.	
#else:
			
	#for south in range(get_pos_y()):  ####################################### V
		#move(South)
	#for west in range(get_pos_x()):
		#move(West)	

detection_of_unharvested_crop_during_main_harvesting_rotaion = 0
main_harvesting_rotation = 1
number_of_required_set_rotations = (get_world_size() // 2)

desired_rotations_for_when_detection_of_farmland_not_harvested = 2
desired_rotations_positional = (desired_rotations_for_when_detection_of_farmland_not_harvested - 1)
live_rotation_counter = 0

current_set = ''
past_move = ''		# Past move direction.
current_move = ''	# Current move direction.
next_move = ''		# Next move direction.
reset = 'Reset'
north = 'North'
south = 'South'
east = 'East'
west = 'West'
bottom_left_set = 'Bottom_left set'
bottom_right_set = 'Bottom_Right set'
top_right_set = 'Top_right set'
top_left_set = 'Top_left set'

required_moves_per_rotation = (total_side_length ** 2)
#full_column_moved = total_side_length

#Starting at bottom_left (bl) moves' calculator. (HARVEST at end of set required)

bl_full_column_moved_x = (x * total_side_length)
#bl_moves_north = ((full_column_moved_completed % 2 == 0) and (y))
#bl_moves_south = ((full_column_moved_completed > 0) and (total_side_length - y))
bl_moves = (((bl_full_column_moved_x % 2 == 0) and (y + 1)) or (((bl_full_column_moved_x > 0) and (bl_full_column_moved_x % 2 == 1)) and (total_side_length - y)))
bl_moves_completed = (bl_full_column_moved_x) + (bl_moves)  #(bl_moves_odd)
bl_moves_remaning = (required_moves_per_rotation - bl_moves_completed)
bl_moves_completed_positional = (bl_moves_completed - 1)

#Starting at bottom_right (br) moves' calculator.

br_moves_west = (total_side_length - x)
br_moves_completed = (y * full_column_moved) + (br_moves_west)
br_moves_remaining = (required_moves_per_rotation - br_moves_completed)

#Starting at top_right (tr) moves' calculator.

tr_moves_north = y
tr_moves_completed = (x * full_column_moved) + (tr_moves_north)
tr_moves_remaning = (required_moves_per_rotation - tr_moves_completed)

#Starting at top_left (tl) moves' calculator.

tl_moves_east = x
tl_moves_completed = (y * full_column_moved) + (tl_moves_east)
tl_moves_remaining = (required_moves_per_rotation - tl_moves_completed)

# A conditional loop to 'check plant type or check ground type'
while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrots or Grounds.Soil or Grounds.Turf:
	#1. Checks for the detection of an un-harvested crop during the main rotation.
	#2. Creates a temporary loop, to rotate again until a desired number of required rotations are finished, due to the detection of an unharvested crop.
	#3. Breaks the temporary loop after reaching the desired rotations (above point no. 2).

	#1.
	if detection_of_unharvested_crop_during_main_harvesting_rotaion == 0:
		
		#
		for main_harvesting_rotation in range(main_harvesting_rotation):
			
			# Checks to see if the farmland has an "even side length" amount of blocks. If true then, starts a specific route of an "even-sided farmland" set.
			if (total_side_length % 2 == 0) and (bottom_left_block or bottom_right_block or top_right_block or top_left_block):
				#1. Checks to see if the drone is on the "Starting Point" of this set, which is on the bottom-left block. The route of this set is North -> East -> South.
 				#2. Checks to see if the drone is on the "Starting Point" of this set, which is on the bottom-right block. The route of this set is West -> North -> East.
 				#3. Checks to see if the drone is on the "Starting Point" of this set, which is on the top-right block. The route of this set is South -> West -> North.
 				#4. Checks to see if the drone is on the "Starting Point" of this set, which is on the top-left block. The route of this set is East -> South -> West.
				
				#1.
				if (bottom_left_block):
					#1. A loop for the amount of required set-routes that makes up a whole rotation, which starts at the set's 'Starting Point' and ends at 'Ending Point'.
					#2. Updates the direction system (indicating that the system has reached the 'End Point' of this set and completed a full rotation, which means the next move is from a new set).
					
					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations): # # # # also need function for when reaches end point and this loop and number_of_required_set_rotations is still not done or just moving to end points
						#1.
						#2.
						#3.
						#4.
						#5.
						#6.	
							
						#1.
						for north in range(total_side_length_positional - get_pos_y()):
							#1.
							#2.
							#3.
														
							#1.
							if (get_ground_type() == Grounds.Turf) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Turf.
								move(North)
								current_set = bottom_left_set
								past_move = north
								current_move = north
								next_move = north
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Turf.	
								till()
								move(North)
								current_set = bottom_left_set
								past_move = north
								current_move = north
								next_move = north
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(North)
								current_set = bottom_left_set
								past_move = north
								current_move = north
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
							
						#2.		
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
																	
							harvest() # Plants grass automatically if ground is a Turf.
							move(East)
							current_set = bottom_left_set
							past_move = north
							current_move = east
							next_move = south
																	
						#3.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
							harvest() # Plants grass automatically if ground is a Turf.	
							till()
							move(East)
							current_set = bottom_left_set
							past_move = north
							current_move = east
							next_move = south
															
						#4.	
						elif can_harvest() != True:
															
							move(East)
							current_set = bottom_left_set
							past_move = north
							current_move = east
							next_move = south
							detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
							main_harvesting_rotation = 0
			
						#5.							
						for south in range(get_pos_y()):
							#1.
							#2.
							#3.
														
							#1.
							if get_ground_type() == Grounds.Turf and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Turf.
								move(South)
								current_set = bottom_left_set
								past_move = east
								current_move = south
								next_move = south
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Turf.	
								till()
								move(South)
								current_set = bottom_left_set
								past_move = east
								current_move = south
								next_move = south
																	
							#3.	
							elif can_harvest() != True:
																	
								move(South)
								current_set = bottom_left_set
								past_move = east
								current_move = south
								next_move = south
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#6.		
						if (x < total_side_length_positional):
							#1.
							#2.
							#3.
						
							#1.						
							if get_ground_type() == Grounds.Turf and can_harvest() == True:
																	
								harvest() # Plants grass automatically if ground is a Turf.
								move(East)
								current_set = bottom_left_set
								past_move = south
								current_move = east
								next_move = north
																
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
								harvest() # Plants grass automatically if ground is a Turf.	
								till()
								move(East)
								current_set = bottom_left_set
								past_move = south
								current_move = east
								next_move = north
																
							#3.	
							elif can_harvest() != True:
																	
								move(East)
								current_set = bottom_left_set
								past_move = south
								current_move = east
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
						#7.		
						else:
							#1.
							#2.
							#3.
						
							#1.						
							if get_ground_type() == Grounds.Turf and can_harvest() == True:
																	
								harvest() # Plants grass automatically if ground is a Turf.
								#move(East)
								current_set = bottom_left_set
								past_move = south
								current_move = east
								next_move = north
																
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
								harvest() # Plants grass automatically if ground is a Turf.	
								till()
								#move(East)
								current_set = bottom_left_set
								past_move = south
								current_move = east
								next_move = north
																
							#3.	
							elif can_harvest() != True:
																	
								#move(East)
								current_set = bottom_left_set
								past_move = south
								current_move = east
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
							
								
						#2.
						current_set = bottom_left_set
						past_move = south
						current_move = reset
						next_move = west
						
				#2.	
				#elif:
					
					
				#3.
				#elif:
					
					
				#4.
				#elif:
					
						
					
				#corners
				#elif  # < - ^ - > , and odd = 1
				#elif  # v - < - ^
				#elif  # > - v - <
				
				#directions
				#elif
				#elif
				#elif
				#elif
			
			# Moves to odd algorithm		
			else:
				
				pass
		#break
				
	#2.			
	elif (detection_of_unharvested_crop_during_main_harvesting_rotaion > 0) and (live_rotation_counter < desired_rotations_positional):
		
		detection_of_unharvested_crop_during_main_harvesting_rotaion = 0
		main_harvesting_rotation = 1
		live_rotation_counter += 1
		live_rotation_counter = live_rotation_counter
	
	#3.	
	else:
		
		break												
													############### THIS IS ODD V
													
					#if get_pos_y() != total_side_length_positional and get_pos_x() == total_side_length_positional: 
												
						#pass
												
					#else:
							
						#1.						
						#if get_ground_type() == Grounds.Turf and can_harvest() == True:
																
							#harvest() # Plants grass automatically if ground is a Turf.
							#move(East)
															
						#2.	
						#elif get_ground_type() == Grounds.Soil and can_harvest() == True:
														
							#harvest() # Plants grass automatically if ground is a Turf.	
							#till()
							#move(East)
															
						#3.	
						#elif can_harvest() != True:
															
							#move(East)
							#no_harvest += 1