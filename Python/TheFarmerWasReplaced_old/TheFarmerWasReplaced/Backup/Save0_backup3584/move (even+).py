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

past_move = ''		# Past move direction.
current_move = ''	# Current move direction.
next_move = ''		# Next move direction.
reset = 'Reset'
north = 'North'
south = 'South'
east = 'East'
west = 'West'

#print(old_direction,'&',current_direction,'&',new_direction)

# A conditional loop to 'check plant type or check ground type'
while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrots or Grounds.Soil or Grounds.Turf:
	#1. Checks for the detection of an un-harvested crop during the main rotation.
	#2. Creates a temporary loop, to rotate again until a desired number of required rotations are finished, due to the detection of an unharvested crop.
	#3. Breaks the temporary loop after reaching the desired rotations (above point no. 2).

	#1.
	if detection_of_unharvested_crop_during_main_harvesting_rotaion == 0:
		
		#
		for main_harvesting_rotation in range(main_harvesting_rotation):
			
			# Checks to see if the farmland has an "even side length" of blocks and that if the drone is on the "Starting Point" of this set, which is on the bottom-left block. The route of this set is North -> East -> South.
			if (get_pos_y() == get_world_size() % 2 == 0) and (get_pos_y() == zero) and (get_pos_x() == get_world_size() % 2 == 0) and (get_pos_x() == zero):
				#1. Checks to see if the drone is already on the "End Point" of this set, which is the bottom-right block. If true, then resets the route progression of the set at (1.1).
 				#2. Starts a specific route of an "even-sided farmland" set, that has a "Starting Point" at the bottom-left block.
				
				#1.
				if (get_pos_y() == zero) and (get_pos_x() == total_side_length_positional):
						
						#1.1					
						past_move = reset
						current_move = reset
						next_move = reset
						pass
						
				#2.	
				else:
					#1. A loop for the amount of required set-routes that makes up a whole rotation, which starts at the set's 'Starting Point' and ends at 'Ending Point'.
					
					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations):
						#1.
						#2.
						#3.
						#4.	
							
						#1.
						for north in range(total_side_length_positional - get_pos_y()):
							#1.
							#2.
							#3.
														
							#1.
							if get_ground_type() == Grounds.Turf and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Turf.
								move(North)
								past_move = north
								current_move = north
								next_move = north
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Turf.	
								till()
								move(North)
								past_move = north
								current_move = north
								next_move = north
																	
							#3.	
							elif can_harvest() != True:
																	
								move(North)
								past_move = north
								current_move = north
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#2.
						if (get_pos_x() < total_side_length_positional): # not at the last column regarding this pattern (right column)
							
							if (get_pos_x() < total_side_length_positional) == True:
							
								#1.
								#2.
								#3.
								
								#1.						
								if get_ground_type() == Grounds.Turf and can_harvest() == True:
																		
									harvest() # Plants grass automatically if ground is a Turf.
									move(East)
									past_move = north
									current_move = east
									next_move = south
																	
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
									harvest() # Plants grass automatically if ground is a Turf.	
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
							
								#3.							
								for south in range(get_pos_y()):
									#1.
									#2.
									#3.
																
									#1.
									if get_ground_type() == Grounds.Turf and can_harvest() == True:
																				
										harvest() # Plants grass automatically if ground is a Turf.
										move(South)
										past_move = east
										current_move = south
										next_move = south
																			
									#2.	
									elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																		
										harvest() # Plants grass automatically if ground is a Turf.	
										till()
										move(South)
										past_move = east
										current_move = south
										next_move = south
																			
									#3.	
									elif can_harvest() != True:
																			
										move(South)
										past_move = east
										current_move = south
										next_move = south
										detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
										main_harvesting_rotation = 0
						
						#4.		
						if (get_pos_x() < total_side_length_positional): # not at the last column regarding this pattern (right column)
							#1.
							#2.
							#3.
							
							#1.						
							if get_ground_type() == Grounds.Turf and can_harvest() == True:
																	
								harvest() # Plants grass automatically if ground is a Turf.
								move(East)
								past_move = north
								current_move = east
								next_move = south
																
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
								harvest() # Plants grass automatically if ground is a Turf.	
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
						
						#5.
						else:
							
							past_move = reset
							current_move = reset
							next_move = reset
							pass
			
			#corners
			#elif
			#elif
			#elif
			
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