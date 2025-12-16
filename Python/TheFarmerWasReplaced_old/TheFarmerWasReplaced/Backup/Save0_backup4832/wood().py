# Ground can be Soil or Turf.	
	#print('Can you do a flip like me ? :D')
	#do_a_flip()
	print('Planting Bushes!')
	
	# A conditional loop to 'check plant type -> reset to starting block'. 
	while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrots or Grounds.Soil or Grounds.Turf:
		#1. No need to reset as drone is on the ""Starting Point"" at (0, 0).
		#2. Reset position from the BOTTOM row at (1, 0).
		#3. Reset position from the BOTTOM row at (2, 0).
			#4. Reset position from the MIDDLE row at (1, 0).
			#5. Reset position from the MIDDLE row at (1, 1).
			#6. Reset position from the MIDDLE row at (1, 2).
				#7. Reset position from the TOP row at (2, 0).
				#8. Reset position from the TOP row at (2, 1).
				#9. Reset position from the TOP row at (2, 2).
					#10. Room for extra statements.
		
		#1.
		if get_pos_x() == 0 and get_pos_y() == 0:
			
			pass
		
		#2.	
		elif get_pos_x() == 1 and get_pos_y() == 0:
		
			move(West)
		
		#3.	
		elif  get_pos_x() == 2 and get_pos_y() == 0:
		
			move(West)
			move(West)
		
		#4.
		elif get_pos_x() == 0 and get_pos_y() == 1:
		
			move(South)
		
		#5.
		elif get_pos_x() == 1 and get_pos_y() == 1:
			
			move(South)
			move(West)
		
		#6.
		elif get_pos_x() == 2 and get_pos_y() == 1:
		
			move(South)
			move(West)
			move(West)
			
		#7.
		elif get_pos_x() == 0 and get_pos_y() == 2:
			
			move(South)
			move(South)
			
		#8.
		elif get_pos_x() == 1 and get_pos_y() == 2:
			
			move(South)
			move(South)
			move(West)
		
		#9.
		elif get_pos_x() == 2 and get_pos_y() == 2:
			
			move(South)
			move(South)
			move(West)
			move(West)
			
		#10.	
		else:
			
			pass 
		
		# Indicates how many rotations to execute.
		for Bush_Harvest_Rotation in range(1):
			#1. First loop, that executes the number of desired moves, 'Repeats 3 times'.
			#2. Second loop, that executes the number of desired moves, 'Repeats 3 times' ('Bush_x -> 3' x 'Bush_y -> 3' = '9' .., moves 9 times before it is counted as 1 rotation).
		
			#1.
			for Bush_x in range(3):
				
				#2.
				for Bush_y in range(3):
						
					# Moves to the bottom of the coloum when at block (0, 2).
					if get_pos_x() == 0 and get_pos_y() == 2:
						#1. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if true) -> harvesting -> planting bush'.
						#2. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if not true)'.
						#3. Room for extra statements.
							
						#1.
						if can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							plant(Entities.Bush)
							move(South)
							move(South)
							move(East)
								
						#2.	
						elif can_harvest() != True:
								
							move(South)
							move(South)
							move(East)
							
						#3.
						else:
							
							continue	
							
					# Moves to the bottom of the coloum when at block (1, 2).
					elif get_pos_x() == 1 and get_pos_y() == 2:
						#1. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if true) -> harvesting -> planting bush'.
						#2. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if not true)'.
						#3. Room for extra statements.
							
						#1.
						if can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							plant(Entities.Bush)
							move(South)
							move(South)
							move(East)
								
						#2.	
						elif can_harvest() != True:
								
							move(South)
							move(South)
							move(East)
							
						#3.
						else:
							
							continue	
							
					# Moves to the bottom of the coloum when at block (2, 2).
					elif get_pos_x() == 2 and get_pos_y() == 2:
						#1. Moves 2xSouth and 2xWest after 'checking for harvest opportunity (if true) -> harvesting -> planting bush'.
						#2. Moves 2xSouth and 2xWest after 'checking for harvest opportunity (if not true)'.
						#3. Room for extra statements.
							
						#1.
						if can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							plant(Entities.Bush)
							move(South)
							move(South)
							move(West)
							move(West)
								
						#2.	
						elif can_harvest() != True:
								
							move(South)
							move(South)
							move(West)
							move(West)
							
						#3.
						else:
							
							continue	
							
					# Moves North on any block.
					else:
						#1. Moves 1xNorth after 'checking for harvest opportunity (if true) -> harvesting -> planting bush'.
						#2. Moves 1xNorth after 'checking for harvest opportunity (if not true)'.
						#3. Room for extra statements.
							
						#1.
						if can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							plant(Entities.Bush)
							move(North)
								
						#2.	
						elif can_harvest != True:
								
							move(North)
							
						#3.
						else:
							
							continue	
		
		# Stops the conditional loop and moves to the next statements.
		break