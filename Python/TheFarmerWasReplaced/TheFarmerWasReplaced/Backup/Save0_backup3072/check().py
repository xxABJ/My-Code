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