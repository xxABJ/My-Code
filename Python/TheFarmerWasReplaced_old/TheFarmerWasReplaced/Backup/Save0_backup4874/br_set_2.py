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
