from all_variables import *

if ((odd_farmland == True) and (bl_block or tro_block)):
	#1. Checks to see if the drone is on a "Starting Point" of this set, which is on the bottom-left block. The route of this set is North -> East -> South -> East ->
	#2. Checks to see if the drone is on a "Starting Point" of this set, which is on the top-right block. The route of this set is South -> West -> North.
	
	#1.
	if (bl_block):
		#1. Updates the current set value in the direction system.
		#2. The main harvesting rotation loop from a "Starting Point" block.
		#3. A loop that moves the drone in the North direction and reaches the 'End Point' of the current set.
		#4. Updates the direction system (indicating that the drone has reached the 'End Point' of this set and completed a "Full odd-set-rotation", which means the next move is from a new set).

		#1.
		current_set = bl_set

		#2.
		for main_harvesting_rotations in range(main_harvesting_rotations):
			#1. A loop for the amount of required "Set-rotations" that makes up a whole rotation, which starts at the set's 'Starting Point' and ends after a full 'Set-rotation'.

			#1.
			for number_of_required_set_rotations in range(number_of_required_set_rotations):
				#1. A loop that moves the drone in the North direction until it reaches the top of the farmland.
				#2. A loop that moves the drone in the East direction.
				#3. A loop that moves the drone in the South direction until it reaches the bottom of the farmland.
				#4. A loop that moves the drone in the East direction.
				
				#1.
				for north_moves in range(total_side_length_positional - get_pos_y()):
					#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
					#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
					#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
					
					#1.
					if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a Grassland.
						move(North)
						past_move = north
						current_move = north
						next_move = north
					
					#2.	
					elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a TGrassland.	
						till()
						move(North)
						past_move = north
						current_move = north
						next_move = north
					
					#3.	
					elif (can_harvest() != True):
					
						move(North)
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
						past_move = north
						current_move = east
						next_move = south
					
					#2.	
					elif get_ground_type() == Grounds.Soil and can_harvest() == True:
					
						harvest() # Plants grass automatically if ground is a Grassland.	
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
						past_move = south
						current_move = south
						next_move = south
					
					#2.	
					elif get_ground_type() == Grounds.Soil and can_harvest() == True:
					
						harvest() # Plants grass automatically if ground is a Grassland.	
						till()
						move(South)
						past_move = south
						current_move = south
						next_move = south
					
					#3.	
					elif can_harvest() != True:
					
						move(South)
						past_move = south
						current_move = south
						next_move = south
						detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
						main_harvesting_rotation = 0
				
				#4.
				for east_moves in range(1):
					#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
					#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
					#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
					
					#1.						
					if get_ground_type() == Grounds.Grassland and can_harvest() == True:
					
						harvest() # Plants grass automatically if ground is a Grassland.
						move(East)
						past_move = south
						current_move = east
						next_move = north
					
					#2.	
					elif get_ground_type() == Grounds.Soil and can_harvest() == True:
					
						harvest() # Plants grass automatically if ground is a Grassland.	
						till()
						move(East)
						past_move = south
						current_move = east
						next_move = north
					
					#3.	
					elif can_harvest() != True:
					
						move(East)
						past_move = south
						current_move = east
						next_move = north
						detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
						main_harvesting_rotation = 0
			
		#3.
		for north_moves in range(total_side_length_positional):
			#1. Moves the drone in the North direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'. 
			#2. Moves the drone in the North direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
			#3. Moves the drone in the North direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".        

			#1.
			if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
			
				harvest() # Plants grass automatically if ground is a Grassland.
				move(North)
				past_move = north
				current_move = north
				next_move = north                   
			
			#2.	
			elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
			
				harvest() # Plants grass automatically if ground is a TGrassland.	
				till()
				move(North)
				past_move = north
				current_move = north
				next_move = north                   
			
			#3.	
			elif (can_harvest() != True):
			
				move(North)
				past_move = north
				current_move = north
				next_move = north
				detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
				main_harvesting_rotation = 0                    

		#4.                
		past_move = south
		current_move = reset
		next_move = west
	
	#2.
	elif (tro_block):
		#1. Updates the current set value in the direction system.
		#2. The main harvesting rotation loop from a "Starting Point" block.
		#3. A loop that moves the drone in the West direction and reaches the 'End Point' of the current set.
		#4. Updates the direction system (indicating that the drone has reached the 'End Point' of this set and completed a "Whole rotation").

		#1.
		current_set = tro_set
		
		#2.
		for main_harvesting_rotations in range(main_harvesting_rotations):
			#1. The main harvesting rotation loop from a "Starting Point" block.

			#1.
			for number_of_required_set_rotations in range(number_of_required_set_rotations):
				#1. A loop that moves the drone in the South direction until it reaches the left side of the farmland.
				#2. A loop that moves the drone in the West direction.
				#3. A loop that moves the drone in the North direction until it reaches the right side of the farmland.
				#4. A loop that moves the drone in the West direction.
				
				#1.							
				for west_moves in range(get_pos_x()):
					#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system".
					#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
					#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".    

					#1.
					if get_ground_type() == Grounds.Grassland and can_harvest() == True:
					
						harvest() # Plants grass automatically if ground is a Grassland.
						move(West)
						past_move = west
						current_move = west
						next_move = west    

					#2.	
					elif get_ground_type() == Grounds.Soil and can_harvest() == True:
					
						harvest() # Plants grass automatically if ground is a Grassland.	
						till()
						move(West)
						past_move = west
						current_move = west
						next_move = west    

					#3.	
					elif can_harvest() != True:
					
						move(West)
						past_move = west
						current_move = west
						next_move = west
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
						past_move = west
						current_move = south
						next_move = east    
					
					#2.	
					elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a Grassland.	
						till()
						move(South)
						past_move = west
						current_move = south
						next_move = east    
					
					#3.	
					elif (can_harvest() != True):
					
						move(South)
						past_move = west
						current_move = south
						next_move = east
						detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
						main_harvesting_rotation = 0    
				
				#3.
				for east_moves in range(total_side_length_positional - get_pos_x()):
					#1. Moves the drone in the East direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
					#2. Moves the drone in the East direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
					#3. Moves the drone in the East direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".    
					
					#1.
					if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a Grassland.
						move(East)
						past_move = east
						current_move = east
						next_move = east    
					
					#2.	
					elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a Grassland.	
						till()
						move(East)
						past_move = east
						current_move = east
						next_move = east    
					
					#3.	
					elif (can_harvest() != True):
					
						move(East)
						past_move = east
						current_move = east
						next_move = east
						detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
						main_harvesting_rotation = 0    
				
				#4.
				for south_moves in range(1):
					#1. Moves the drone in the South direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
					#2. Moves the drone in the South direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
					#3. Moves the drone in the South direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".    
					
					#1.
					if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a Grassland.
						move(South)
						past_move = west
						current_move = south
						next_move = east    
					
					#2.	
					elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
					
						harvest() # Plants grass automatically if ground is a Grassland.	
						till()
						move(South)
						past_move = west
						current_move = south
						next_move = east    
					
					#3.	
					elif (can_harvest() != True):
					
						move(South)
						past_move = west
						current_move = south
						next_move = east
						detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
						main_harvesting_rotation = 0    
			
		#3.
		for west_moves in range(get_world_size()):
			#1. Checks to see the if the drone is able to move in the West direction, which also indicates the end of a "Set-rotation".
			#2.	When (#1) is false, the drone harvests and does not move, which also indicates the end of a "Full-odd-rotation".

			#1.
			if (get_pos_x() > 0):
				#1. Moves the drone in the West direction after 'checking for grassland -> checking for ability to harvest (if True) -> harvesting -> planting grass', then updating the "Set and Direction system"'.
				#2. Moves the drone in the West direction after 'checking for soil -> checking for ability to harvest (if True) -> harvesting -> tilling the ground -> planting grass', then updating the "Set and Direction system".
				#3. Moves the drone in the West direction after 'checking for ability to harvest (if False)', then updating the "Set and Direction system".
				
				#1.
				if (get_ground_type() == Grounds.Grassland) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.
					move(West)
					past_move = west
					current_move = west
					next_move = west
				
				#2.	
				elif (get_ground_type() == Grounds.Soil) and (can_harvest() == True):
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					move(West)
					past_move = west
					current_move = west
					next_move = west
				
				#3.	
				elif (can_harvest() != True):

					move(West)
					past_move = west
					current_move = west
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
					past_move = west
					current_move = reset
					next_move = north           
				
				#2.	
				elif get_ground_type() == Grounds.Soil and can_harvest() == True:
				
					harvest() # Plants grass automatically if ground is a Grassland.	
					till()
					past_move = west
					current_move = reset
					next_move = north           
				
				#3.	
				elif can_harvest() != True:
				
					past_move = west
					current_move = reset
					next_move = north
					detection_of_unharvested_crop_during_main_harvesting_rotaion = 1
					main_harvesting_rotation = 0
	
		#4.
		past_move = west
		current_move = reset
		next_move = north
