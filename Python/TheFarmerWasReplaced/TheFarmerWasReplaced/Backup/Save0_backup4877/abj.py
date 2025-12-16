from all_variables import *

# A conditional loop to 'check plant type or check ground type'
while get_entity_type() == Entities.Grass or Entities.Bush or Entities.Carrot or Grounds.Soil or Grounds.Grassland:
	#1. Checks for the detection of an un-harvested crop during the main rotation.
	#2. Creates a temporary loop when (#1) is false, to rotate again until a desired number of required rotations are finished.
	#3. Breaks the temporary loop after reaching the desired rotations (#2).

	#1.
	if detection_of_unharvested_crop_during_main_harvesting_rotaion == 0:
		
		# The main harvesting rotation loop from a "Starting Point" block.
		for main_harvesting_rotation in range(main_harvesting_rotation):
			#1. Checks to see if the farmland has an "even side length" amount of blocks and is on a specific "Starting Point" block. If true then, starts an "even-sided farmland" route. (Even corners)
			#2. odd corners
			
			#1. (Even & corners)
			if ((even_farmland == True) and (bl_block or br_block or tr_block or tl_block)):
				#1. Checks to see if the drone is on the "Starting Point" of this set, which is on the bottom-left block. The route of this set is North -> East -> South.
 				#2. Checks to see if the drone is on the "Starting Point" of this set, which is on the bottom-right block. The route of this set is West -> North -> East.
 				#3. Checks to see if the drone is on the "Starting Point" of this set, which is on the top-right block. The route of this set is South -> West -> North.
 				#4. Checks to see if the drone is on the "Starting Point" of this set, which is on the top-left block. The route of this set is East -> South -> West.
				
				#1.
				if (bl_block):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at the set's 'Starting Point' and ends at the 'Ending Point'.
					#2. Updates the direction system (indicating that the system has reached the 'End Point' of this set and completed a "Full-rotation", which means the next move is from a new set).

					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations): # # # # also need function for when reaches end point and this loop and number_of_required_set_rotations is still not done or just moving to end points
						#1. A loop that moves the drone in the North direction until it reaches the top of the farmland.
						#2. A loop that moves the drone in the East direction.
						#3. A loop that moves the drone in the South direction until it reaches the bottom of the farmland.
						#4. A Conditional loop that either moves in the East direction or makes the drone harvest and stop.
													
						#1.
						for north_moves in range(total_side_length_positional - get_pos_y()):
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
																
								harvest() # Plants grass automatically if ground is a TGrassland.	
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
						for east_moves in range(1):
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
						for south_moves in range(get_pos_y()):
							#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(South)
								current_set = bl_set
								past_move = east
								current_move = south
								next_move = south
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(South)
								current_set = bl_set
								past_move = east
								current_move = south
								next_move = south
																	
							#3.	
							elif can_harvest() != True:
																	
								move(South)
								current_set = bl_set
								past_move = east
								current_move = south
								next_move = south
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for east_moves in range(1):
							#1. Checks to see the if the drone is able to move in the East direction, which also indicates the end of a "Set-rotation".
							#2.	When (#1) is false, the drone does not move, indicating the end of a "Full-rotation".

							#1.
							if (get_pos_x() < total_side_length_positional):
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
							else:
								#1. Drone does not move after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Drone does not move after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Drone does not move after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
								#1.						
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
									harvest() # Plants grass automatically if ground is a Grassland.
									current_set = bl_set
									past_move = south
									current_move = reset
									next_move = west
																
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									current_set = bl_set
									past_move = south
									current_move = reset
									next_move = west
																
								#3.	
								elif can_harvest() != True:
																	
									current_set = bl_set
									past_move = south
									current_move = reset
									next_move = west
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
								
					#2.
					current_set = bl_set
					past_move = south
					current_move = reset
					next_move = west
						
				#2.	
				elif (br_block):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at the set's 'Starting Point' and ends at the 'Ending Point'.
					#2. Updates the direction system (indicating that the system has reached the 'End Point' of this set and completed a "Full-rotation", which means the next move is from a new set).
					
					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations): # # # # also need function for when reaches end point and this loop and number_of_required_set_rotations is still not done or just moving to end points
						#1. A loop that moves the drone in the West direction until it reaches the left side of the farmland.
						#2. A loop that moves the drone in the North direction.
						#3. A loop that moves the drone in the East direction until it reaches the right side of the farmland.
						#4. A Conditional loop that either moves in the North direction or makes the drone harvest and stop.
							
						#1.
						for west_moves in range(get_pos_x()):
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
						for north_moves in range(1):
							#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".

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
						for east_moves in range(total_side_length_positional - get_pos_x()):
							#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
							#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(East)
								current_set = br_set
								past_move = north
								current_move = east
								next_move = east
																	
							#2.	
							elif get_ground_type() == Grounds.Soil and can_harvest() == True:
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(East)
								current_set = br_set
								past_move = north
								current_move = east
								next_move = east
																	
							#3.	
							elif can_harvest() != True:
																	
								move(East)
								current_set = br_set
								past_move = north
								current_move = east
								next_move = east
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for north_moves in range(1):
							#1. Checks to see the if the drone is able to move in the North direction, which also indicates the end of a "Set-rotation".
							#2.	When (#1) is false, the drone does not move, which also indicates the end of a "Full-rotation".

							#1
							if (get_pos_y() < total_side_length_positional):
								#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
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
							
							#2.		
							else:
								#1. Drone does not move after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Drone does not move after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Drone does not move after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
								#1.						
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
									harvest() # Plants grass automatically if ground is a Grassland.
									current_set = br_set
									past_move = east
									current_move = reset
									next_move = south
																
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									current_set = br_set
									past_move = east
									current_move = reset
									next_move = south
																
								#3.	
								elif can_harvest() != True:
																	
									current_set = br_set
									past_move = east
									current_move = reset
									next_move = south
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
						
					#2.
					current_set = br_set
					past_move = east
					current_move = reset
					next_move = south
					
				#3.	
				elif (tr_block):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at the set's 'Starting Point' and ends at the 'Ending Point'.
					#2. Updates the direction system (indicating that the system has reached the 'End Point' of this set and completed a "Full-rotation", which means the next move is from a new set).
					
					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations): # # # # also need function for when reaches end point and this loop and number_of_required_set_rotations is still not done or just moving to end points
						#1. A loop that moves the drone in the South direction until it reaches the left side of the farmland.
						#2. A loop that moves the drone in the West direction.
						#3. A loop that moves the drone in the North direction until it reaches the right side of the farmland.
						#4. A Conditional loop that either moves in the West direction or makes the drone harvest and stop.
							
						#1.							
						for south_moves in range(get_pos_y()):
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
						for west_moves in range(1):
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
						for north_moves in range(total_side_length_positional - get_pos_y()):
							#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(North)
								current_set = tr_set
								past_move = west
								current_move = north
								next_move = north
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(North)
								current_set = tr_set
								past_move = west
								current_move = north
								next_move = north
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(North)
								current_set = tr_set
								past_move = west
								current_move = north
								next_move = north
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for west_moves in range(1):
							#1. Checks to see the if the drone is able to move in the West direction, which also indicates the end of a "Set-rotation".
							#2.	When (#1) is false, the drone does not move, which also indicates the end of a "Full-rotation".

							#1
							if (get_pos_x() > 0):
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
									
							#2.		
							else:
								#1. Drone does not move after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Drone does not move after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Drone does not move after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
								#1.						
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
									harvest() # Plants grass automatically if ground is a Grassland.
									current_set = tr_set
									past_move = north
									current_move = reset
									next_move = east
																
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									current_set = tr_set
									past_move = north
									current_move = reset
									next_move = east
																
								#3.	
								elif can_harvest() != True:
																	
									current_set = tr_set
									past_move = north
									current_move = reset
									next_move = east
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
						
					#2.
					current_set = tr_set
					past_move = north
					current_move = reset
					next_move = east
									
				#4.	
				elif (tl_block):
					#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at the set's 'Starting Point' and ends at the 'Ending Point'.
					#2. Updates the direction system (indicating that the system has reached the 'End Point' of this set and completed a "Full-rotation", which means the next move is from a new set).
					
					#1.
					for number_of_required_set_rotations in range(number_of_required_set_rotations): # # # # also need function for when reaches end point and this loop and number_of_required_set_rotations is still not done or just moving to end points
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
						for south_moves in range(1):
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
						for west_moves in range(get_pos_x()):
							#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
							#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
							#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
														
							#1.
							if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
																		
								harvest() # Plants grass automatically if ground is a Grassland.
								move(West)
								current_set = tl_set
								past_move = south
								current_move = west
								next_move = west
																	
							#2.	
							elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
																
								harvest() # Plants grass automatically if ground is a Grassland.	
								till()
								move(West)
								current_set = tl_set
								past_move = south
								current_move = west
								next_move = west
																	
							#3.	
							elif (can_harvest() != True):
																	
								move(West)
								current_set = tl_set
								past_move = south
								current_move = west
								next_move = west
								detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
								main_harvesting_rotation = 0
								
						#4.
						for south_moves in range(1):
							#1. Checks to see the if the drone is able to move in the South direction, which also indicates the end of a "Set-rotation".
							#2.	When (#1) is false, the drone does not move, which also indicates the end of a "Full-rotation".

							#1
							if (get_pos_y() > 0):
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
							else:
								#1. Drone does not move after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
								#2. Drone does not move after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
								#3. Drone does not move after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
						
								#1.						
								if get_ground_type() == Grounds.Grassland and can_harvest() == True:
																	
									harvest() # Plants grass automatically if ground is a Grassland.
									current_set = tl_set
									past_move = west
									current_move = reset
									next_move = north
																
								#2.	
								elif get_ground_type() == Grounds.Soil and can_harvest() == True:
															
									harvest() # Plants grass automatically if ground is a Grassland.	
									till()
									current_set = tl_set
									past_move = west
									current_move = reset
									next_move = north
																
								#3.	
								elif can_harvest() != True:
																	
									current_set = tl_set
									past_move = west
									current_move = reset
									next_move = north
									detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
									main_harvesting_rotation = 0
						
					#2.
					current_set = tl_set
					past_move = west
					current_move = reset
					next_move = north
			

			#2. (odd & corners)
			elif ((odd_farmland == True) and (bl_block or tr_block)):
				#1.
				#2.

				#1.

			#Moves to directions (need *update loop)
			elif (((even_farmland == True) or (odd_farmland == True)) and not (bl_block or br_block or tr_block or tl_block)):

				pass

		# The locator and remaining moves calculator (... -= 1)
		if (even_farmland == True):
				
		else:
			pass


	#2.			
	elif (detection_of_unharvested_crop_during_main_harvesting_rotaion > 0) and (live_rotation_counter < desired_rotations_positional): #change this
		
		detection_of_unharvested_crop_during_main_harvesting_rotaion = 0
		main_harvesting_rotation = 1
		live_rotation_counter += 1
		live_rotation_counter = live_rotation_counter
	
	#3.	
	else:
		
		break												