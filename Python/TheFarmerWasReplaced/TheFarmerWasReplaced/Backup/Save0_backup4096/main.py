while True:
	
	# Ground has to be turf.
	#print('Can you do a flip like me ? :D')
	#do_a_flip()
	print('Planting grass!')
	
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
		for Grass_Harvest_Rotation in range(1):
			#1. First loop, that executes the number of desired moves, 'Repeats 3 times'.
			#2. Second loop, that executes the number of desired moves, 'Repeats 3 times' ('Grass_x -> 3' x 'Grass_y -> 3' = '9' .., moves 9 times before it is counted as 1 rotation).
		
			#1.
			for Grass_x in range(3):
				
				#2.
				for Grass_y in range(3):
							
					# Moves to the bottom of the coloum when at block (0, 2).
					if get_pos_x() == 0 and get_pos_y() == 2:
						#1. Moves 2xSouth and 1xEast after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> planting grass'.
						#2. Moves 2xSouth and 1xEast after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting grass'.
						#3. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if not true)'
						#4. Room for extra statements.
								
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
										
							harvest() # Plants grass automatically if ground is a Turf.
							move(South)
							move(South)
							move(East)
									
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							till()
							move(South)
							move(South)
							move(East)
									
						#3.	
						elif can_harvest() != True:
									
							move(South)
							move(South)
							move(East)
							
						#4.
						else:
							
							continue
							
					# Moves to the bottom of the coloum when at block (1, 2).
					elif get_pos_x() == 1 and get_pos_y() == 2:
						#1. Moves 2xSouth and 1xEast after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> planting grass'.
						#2. Moves 2xSouth and 1xEast after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting grass'.
						#3. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if not true)'
						#4. Room for extra statements.
								
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
										
							harvest() # Plants grass automatically if ground is a Turf.
							move(South)
							move(South)
							move(East)
									
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							till()
							move(South)
							move(South)
							move(East)
									
						#3.	
						elif can_harvest() != True:
									
							move(South)
							move(South)
							move(East)
							
						#4.
						else:
							
							continue
								
					# Moves to the bottom of the coloum when at block (2, 2).
					elif get_pos_x() == 2 and get_pos_y() == 2:
						#1. Moves 2xSouth and 2xWest after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> planting grass'.
						#2. Moves 2xSouth and 2xWest after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting grass'.
						#3. Moves 2xSouth and 2xWest after 'checking for harvest opportunity (if not true)'
						#4. Room for extra statements.
								
						#1.
						if get_ground_type() == Grounds.Turf and can_harvest() == True:
										
							harvest() # Plants grass automatically if ground is a Turf.
							move(South)
							move(South)
							move(West)
							move(West)
									
						#2.	
						elif get_ground_type() == Grounds.Soil and can_harvest() == True:
									
							harvest() # Plants grass automatically if ground is a Turf.
							till()
							move(South)
							move(South)
							move(West)
							move(West)
									
						#3.	
						elif can_harvest() != True:
									
							move(South)
							move(South)
							move(West)
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
		
	# Ground has to be soil.	
	#print('Can you do a flip like me ? :D')
	#do_a_flip()
	print('Planting Carrots!')
	
	if num_items(Items.Carrot_Seed) >= 10:
		
		# A conditional loop to 'check plant type -> reset to starting block'. 
		while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrots:
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
			for Carrot_Harvest_Rotation in range(1):
				#1. First loop, that executes the number of desired moves, 'Repeats 3 times'.
				#2. Second loop, that executes the number of desired moves, 'Repeats 3 times' ('Carrot_x -> 3' x 'Carrot_y -> 3' = '9' .., moves 9 times before it is counted as 1 rotation).
			
				#1.
				for Carrot_x in range(3):
					
					#2.
					for Carrot_y in range(3):
							
						# Moves to the bottom of the coloum when at block (0, 2).
						if get_pos_x() == 0 and get_pos_y() == 2:
							#1. Moves 2xSouth and 1xEast after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> planting carrot'.
							#2. Moves 2xSouth and 1xEast after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting carrot'.
							#3. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if not true)'.
							#4. Room for extra statements.
								
							#1.
							if get_ground_type() == Grounds.Soil and can_harvest() == True:
										
								harvest() # Plants grass automatically if ground is a Turf.
								plant(Entities.Carrots)
								move(South)
								move(South)
								move(East)
									
							#2.	
							elif get_ground_type() == Grounds.Turf and can_harvest() == True:
									
								harvest() # Plants grass automatically if ground is a Turf.
								till()
								plant(Entities.Carrots)
								move(South)
								move(South)
								move(East)
									
							#3.	
							elif can_harvest() != True:
									
								move(South)
								move(South)
								move(East)
								
							#4.
							else:
								
								continue	
								
						# Moves to the bottom of the coloum when at block (1, 2).
						elif get_pos_x() == 1 and get_pos_y() == 2:
							#1. Moves 2xSouth and 1xEast after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> planting carrot'.
							#2. Moves 2xSouth and 1xEast after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting carrot'.
							#3. Moves 2xSouth and 1xEast after 'checking for harvest opportunity (if not true)'.
							#4. Room for extra statements.
								
							#1.
							if get_ground_type() == Grounds.Soil and can_harvest() == True:
										
								harvest() # Plants grass automatically if ground is a Turf.
								plant(Entities.Carrots)
								move(South)
								move(South)
								move(East)
									
							#2.	
							elif get_ground_type() == Grounds.Turf and can_harvest() == True:
									
								harvest() # Plants grass automatically if ground is a Turf.
								till()
								plant(Entities.Carrots)
								move(South)
								move(South)
								move(East)
									
							#3.	
							elif can_harvest() != True:
									
								move(South)
								move(South)
								move(East)
								
							#4.
							else:
								
								continue	
								
						# Moves to the bottom of the coloum when at block (2, 2).
						elif get_pos_x() == 2 and get_pos_y() == 2:
							#1. Moves 2xSouth and 2xWest after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> planting carrot'.
							#2. Moves 2xSouth and 2xWest after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting carrot'.
							#3. Moves 2xSouth and 2xWest after 'checking for harvest opportunity (if not true)'.
							#4. Room for extra statements.
								
							#1.
							if get_ground_type() == Grounds.Soil and can_harvest() == True:
										
								harvest() # Plants grass automatically if ground is a Turf.
								plant(Entities.Carrots)
								move(South)
								move(South)
								move(West)
								move(West)
									
							#2.	
							elif get_ground_type() == Grounds.Turf and can_harvest() == True:
									
								harvest() # Plants grass automatically if ground is a Turf.
								till()
								plant(Entities.Carrots)
								move(South)
								move(South)
								move(West)
								move(West)
									
							#3.	
							elif can_harvest() != True:
									
								move(South)
								move(South)
								move(West)
								move(West)
								
							#4.
							else:
								
								continue	
								
						# Moves North on any block.
						else:
							#1. Moves 1xNorth after 'checking for soil and checking for harvest opportunity (if true) -> harvesting -> planting carrot'.
							#2. Moves 1xNorth after 'checking for turf and checking for harvest opportunity (if true) -> harvesting -> tilling the ground -> planting carrot'.
							#3. Moves 1xNorth after 'checking for harvest opportunity (if not true)'.
							#4. Room for extra statements.
								
							#1.
							if get_ground_type() == Grounds.Soil and can_harvest() == True:
										
								harvest() # Plants grass automatically if ground is a Turf.
								plant(Entities.Carrots)
								move(North)
									
							#2.	
							elif get_ground_type() == Grounds.Turf and can_harvest() == True:
									
								harvest() # Plants grass automatically if ground is a Turf.	
								till()
								plant(Entities.Carrots)
								move(North)
									
							#3.	
							elif can_harvest() != True:
									
								move(North)
								
							#4.	
							else:
								
								continue
			
			# Stops the conditional loop and moves to the next statements.
			break
	
	# Skips carrots. (Should buy more seeds!)		
	else:
		
		#buy_carrot_seeds()
		continue
		
	#break