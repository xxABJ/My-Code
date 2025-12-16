total_side_length_positional = (get_world_size() - 1)

#1.
#if get_pos_x() == (total_side_length_positional - total_side_length_positional) and get_pos_y() == (total_side_length_positional - total_side_length_positional):
			
	#pass

#2.	
#else:
			
	#for south in range(get_pos_y()):  ####################################### V
		#move(South)
	#for west in range(get_pos_x()):
		#move(West)	
	
no_harvest = 0
repeat_harvesting_rotation = 1
number_of_required_sets = (get_world_size() // 2)

desired_rotations_for_when_detection_of_farmland_not_harvested = 3
desired_rotations_positional = (desired_rotations_for_when_detection_of_farmland_not_harvested - 1)
live_rotation_counter = 0

old_direction = ''
current_direction = '' # directional characters: up, down, right, left ( u , d , r , l ).
new_direction = ''

#print(old_direction,'&',current_direction,'&',new_direction)

while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrots or Grounds.Soil or Grounds.Turf:

	#1.
	if no_harvest == 0:
		
		#
		for repeat_harevsting_rotation in range(repeat_harvesting_rotation):
			
			# Even Algorithm
			if (get_pos_y() == get_world_size() % 2 == 0) and (get_pos_y() == 0) and (get_pos_x() == get_world_size() % 2 == 0) and (get_pos_x() == 0): #even indication. start at (0, 0) and end at BOTTOM RIGHT
			#if (get_pos_y() == get_world_size() % 2 == 0) and (get_pos_y() != total_side_length_positional) and (get_pos_x() == get_world_size() % 2 == 0) and (get_pos_x() != total_side_length_positional):
				
				#	
				for number_of_required_sets in range(number_of_required_sets):
					
					#1.
					for north in range(total_side_length_positional - get_pos_y()):
						#1.
						#2.
						#3.
												
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
																
							harvest() # Plants grass automatically if ground is a Turf.
							move(North)
							direction = 'up'
															
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
														
							harvest() # Plants grass automatically if ground is a Turf.	
							till()
							move(North)
															
						#3.	
						elif can_harvest() != True:
															
							move(North)
							no_harvest = 1
							repeat_harvesting_rotation = 0
					
					#2.						
					if (get_pos_y() == 0) and (get_pos_x() == total_side_length_positional): # BOTTOM RIGHT
												
						pass
						
					#3.							
					else:
						#1.
						#2.
						#3.
							
						#1.						
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
																
							harvest() # Plants grass automatically if ground is a Turf.
							move(East)
															
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
														
							harvest() # Plants grass automatically if ground is a Turf.	
							till()
							move(East)
															
						#3.	
						elif can_harvest() != True:
															
							move(East)
					
					#4.							
					for south in range(get_pos_y()):
						#1.
						#2.
						#3.
													
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
																	
							harvest() # Plants grass automatically if ground is a Turf.
							move(South)
																
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
							harvest() # Plants grass automatically if ground is a Turf.	
							till()
							move(South)
																
						#3.	
						elif can_harvest() != True:
																
							move(South)
							no_harvest = 1
							repeat_harvesting_rotation = 0
			
			#corners
			elif
			elif
			elif
			
			#directions
			elif
			elif
			elif
			elif
			
			# Moves to odd algorithm		
			else:
				
				pass
				
	#2.			
	elif (no_harvest > 0) and (live_rotation_counter < desired_rotations_positional):
		
		no_harvest = 0
		repeat_harvesting_rotation = 1
		live_rotation_counter += 1
		live_rotation_counter = live_rotation_counter
	
	#3.	
	else:
		
		pass													
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