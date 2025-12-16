# Ground has to be turf.
	#print('Can you do a flip like me ? :D')
	#do_a_flip()
	print('Planting grass!')
	
	# A conditional loop to 'check plant type -> reset to the "Starting Point". 
	while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrots or Grounds.Soil or Grounds.Turf:
		#1. No need to reset as drone is on the "Starting Point" at (0, 0).
		#2. Reset position to the "Starting Point" when x is = 0 and y is > than 0.
		#3. Reset position to the "Starting Point" when x is > than 0 and y is = 0.
		#4. Reset position to the "Starting Point" when x and y are both > than 0.
		#5. Room for extra statements.
		
		rotation = 1
		grass_x = 3
		grass_y = 3
		total_side_length_positional = get_world_size() - 1
		#indicator_x = total_side_length_positional / total_side_length_positional
		
		#1.
		if get_pos_x() == (total_side_length_positional - total_side_length_positional) and get_pos_y() == (total_side_length_positional - total_side_length_positional):
			
			pass
		
		#2.	
		#elif get_pos_x() == (total_side_length_positional - total_side_length_positional) and get_pos_y() != (total_side_length_positional - total_side_length_positional):
		
			#for south in range(get_pos_y()):
				#move(South)
			
		#3.	
		#elif get_pos_x() != (total_side_length_positional - total_side_length_positional) and get_pos_y() == (total_side_length_positional - total_side_length_positional):
		
			#for west in range(get_pos_x()):
				#move(West)
			
		#4.	
		#elif get_pos_x() != (total_side_length_positional - total_side_length_positional) and get_pos_y() != (total_side_length_positional - total_side_length_positional):
		
			#for south in range(get_pos_y()):
				#move(South)
			#for west in range(get_pos_x()):
				#move(West)
			
		#5.	
		else:
			
			for south in range(get_pos_y()):
				move(South)
			for west in range(get_pos_x()):
				move(West)	
		
		# Indicates how many rotations to execute.
		for Grass_Harvest_Rotation in range(rotation):
			#1. First loop, that executes the number of desired moves, 'Repeats 3 times'.
			#2. Second loop, that executes the number of desired moves, 'Repeats 3 times' ('Grass_x -> 3' x 'Grass_y -> 3' = '9' .., moves 9 times before it is counted as 1 rotation).
		
			#1.
			for Grass_x in range(grass_x):
				
				#2.
				for Grass_y in range(grass_y):
							
					# Moves to the bottom row after reach the top row.
					if get_pos_y() == total_side_length_positional and not get_pos_x() == total_side_length_positional:
						#1. Moves the required South moves to reach the bottom row by subtracting 1 from the total length of the side (total_side_length_positional), then translating it in to directional moves (1.1.) and 1xEast move after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> planting grass'.
						#2. Moves the required South moves to reach the bottom row by subtracting 1 from the total length of the side (total_side_length_positional), then translating it in to directional moves (2.2.) and 1xEast move after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting grass'.
						#3. Moves the required South moves to reach the bottom row by subtracting 1 from the total length of the side (total_side_length_positional), then translating it in to directional moves (3.3.) and 1xEast move after 'checking for harvest opportunity (if not true)'.
						#4. Room for extra statements.
								
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
										
							harvest() # Plants grass automatically if ground is a Turf.
							#1.1.
							for south in range(total_side_length_positional):#move(South)
								move(South)
							move(East)
									
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							till()
							#2.2.
							for south in range(total_side_length_positional):#move(South)
								move(South)
							move(East)
									
						#3.	
						elif can_harvest() != True:
							
							#3.3.		
							for south in range(total_side_length_positional):#move(South)
								move(South)
							move(East)
							
						#4.
						else:
							
							continue
								
					# Moves to the "Starting Point" after reaching the final block (top-right) on the top row.
					elif get_pos_y() == total_side_length_positional and get_pos_x() == total_side_length_positional:
						#1. Moves the required South and West moves to reach the "Starting Point" by subtracting 1 from the total length of the side (total_side_length_positional), then translating it in to directional moves (1.1.) after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> planting grass'.
						#2. Moves the required South and West moves to reach the "Starting Point" by subtracting 1 from the total length of the side (total_side_length_positional), then translating it in to directional moves (2.2.) after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting grass'.
						#3. Moves the required South and West moves to reach the "Starting Point" by subtracting 1 from the total length of the side (total_side_length_positional), then translating it in to directional moves (3.3.) after 'checking for harvest opportunity (if not true)'.
						#4. Room for extra statements.
								
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
										
							harvest() # Plants grass automatically if ground is a Turf.
							#1.1.
							for south in range(total_side_length_positional):#move(South)
								move(South)
							for west in range(total_side_length_positional):#move(West)
								move(West)
									
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							till()
							#2.2.
							for south in range(total_side_length_positional):#move(South)
								move(South)
							for west in range(total_side_length_positional):#move(West)
								move(West)
								
						#3.	
						elif can_harvest() != True:
							
							#3.3.
							for south in range(total_side_length_positional):#move(South)
								move(South)
							for west in range(total_side_length_positional):#move(West)
								move(West)
							
						#4.
						else:
							
							continue
							
					# Moves North on any block.
					else:
						#1. Moves 1xNorth after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> planting grass'.
						#2. Moves 1xNorth after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting grass'.
						#3. Moves 1xNorth after 'checking for harvest opportunity (if not true)'.
						#4. Room for extra statements.
								
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
										
							harvest() # Plants grass automatically if ground is a Turf.
							move(North)
									
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
								
							harvest() # Plants grass automatically if ground is a Turf.	
							till()
							move(North)
									
						#3.	
						elif can_harvest() != True:
									
							move(North)
							
						#4.
						else:
							
							continue	
							
		# Stops the conditional loop and moves to the next statements.
		break