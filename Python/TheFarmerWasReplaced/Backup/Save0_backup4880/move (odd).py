total_side_length_positional = get_world_size() - 1		

a = total_side_length_positional - get_pos_y()

#1.
if get_pos_x() == (total_side_length_positional - total_side_length_positional) and get_pos_y() == (total_side_length_positional - total_side_length_positional):
			
	pass

#2.	
else:
			
	for south in range(get_pos_y()):  ####################################### V
		move(South)
	for west in range(get_pos_x()):
		move(West)	
	
	############# FIX BRAKETS + if else for 2 odd algorythms after odd indication
	########################################
	###################################################### 
if get_pos_y() == (get_world_size() % 2 == 1 and not total_side_length_positional) and get_pos_x() == (get_world_size() % 2 == 1 and not total_side_length_positional): #odd indication
			
for north in range(total_side_length_positional - get_pos_y()):
							
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
						
if get_pos_y() != total_side_length_positional and get_pos_x() == total_side_length_positional: 
							
	pass
							
else:
		
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
							
for south in range(get_pos_y()):
								
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
								
if get_pos_y() != total_side_length_positional and get_pos_x() == total_side_length_positional: 
							
	pass
							
else:
		
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
		
		
		
		########################## ODD CONNECTOR (BETWEEN
		
		#5.
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
					#6.		
					else:
							
						pass