from __builtins__ import *

x = get_pos_x()
y = get_pos_y()
drone = x,y

total_side_length = get_world_size()
zero = total_side_length - total_side_length
total_side_length_positional = (get_world_size() - 1)

top_side = (y == total_side_length_positional)
bottom_side = (y == zero)
left_side = (x == zero)
right_side = (x == total_side_length_positional)

tl_block = (top_side and left_side) 	# Top-left block.
tr_block = (top_side and right_side) 	# Top-right block.
bl_block = (bottom_side and left_side) 	# Bottom-left block.
br_block = (bottom_side and right_side)	# Bottom-right block.

# Assigning or names to sets ("Starting Points").
bl_set = 0 		# Bottom-left set.
br_set = 1 		# Bottom-right set.
tr_set = 2 		# Top-right set.
tl_set = 3 		# Top-left set.

# Set and Direction system.
current_set = ''	# Current set indicator.
past_move = ''		# Past move indicator.
current_move = ''	# Current move indicator.
next_move = ''		# Next move indicator.
reset = 'Reset'
north = 'North'
south = 'South'
east = 'East'
west = 'West'

even_farmland = (total_side_length % 2 == 0)
even_farmland_set_rotation_count = ((even_farmland == True) and (4))
odd_farmland = (total_side_length % 2 == 1)
odd_farmland_set_rotation_count = ((odd_farmland == True) and (2)) 
detection_of_unharvested_crop_during_main_harvesting_rotaion = 0
harvesting_rotations = ((even_farmland_set_rotation_count) or (odd_farmland_set_rotation_count)) #### fix this and below
harvesting_rotations = ((even_farmland == True == 4) or (odd_farmland == True == 2)) #### fix below
remaining_harvesting_rotations = (harvesting_rotations - (((even_farmland == True) and (current_set)) or ((odd_farmland == True) - ((current_set) or ((odd_farmland == True == 2) / (current_set))))))
main_harvesting_rotations = (harvesting_rotations + remaining_harvesting_rotations)
number_of_required_set_rotations = (get_world_size() // 2)

desired_rotations_for_when_detection_of_farmland_not_harvested = 2
desired_rotations_positional = ((desired_rotations_for_when_detection_of_farmland_not_harvested) - (1))
live_rotation_counter = 0

# Calculating the remaining moves required.
required_moves_per_rotation = (total_side_length ** 2)

# Starting at bottom_right (bl) move calculator. (HARVEST at end of set required)
bl_full_column_moved_x = (x * total_side_length)
bl_moves = (((bl_full_column_moved_x % 2 == 0) and (y + 1)) or (((bl_full_column_moved_x > 0) and (bl_full_column_moved_x % 2 == 1)) and (total_side_length - y)))
bl_moves_completed = ((bl_full_column_moved_x) + (bl_moves))
bl_moves_remaining = (required_moves_per_rotation - bl_moves_completed)
#bl_moves_completed_positional = (bl_moves_completed - 1)

# Starting at bottom_right (br) move calculator. (HARVEST at end of set required)
br_full_row_moved_y = (y * total_side_length)
br_moves = (((br_full_row_moved_y % 2 == 0) and (total_side_length - x)) or (((br_full_row_moved_y > 0) and (br_full_row_moved_y % 2 == 1)) and (x + 1)))
br_moves_completed = ((br_full_row_moved_y) + (br_moves))
br_moves_remaining = (required_moves_per_rotation - br_moves_completed)
#br_moves_completed_positional = (br_moves_completed - 1)

# Starting at top_right (tr) move calculator. (HARVEST at end of set required)
tr_full_column_moved_x = ((total_side_length_positional - x) * (total_side_length))
tr_moves = (((tr_full_column_moved_x % 2 == 0) and (total_side_length - y)) or (((tr_full_column_moved_x > 0) and (tr_full_column_moved_x % 2 == 1)) and (y + 1)))
tr_moves_completed = ((tr_full_column_moved_x) + (tr_moves))
tr_moves_remaining = (required_moves_per_rotation - tr_moves_completed)
#tr_moves_completed_positional = (tr_moves_completed - 1)

# Starting at top_left (tl) move calculator. (HARVEST at end of set required)
tl_full_column_moved_x = ((total_side_length_positional - y) * (total_side_length))
tl_moves = (((tl_full_column_moved_x % 2 == 0) and (x + 1)) or ((tl_full_column_moved_x > 0) and (tl_full_column_moved_x % 2 == 1) and ((total_side_length_positional - x) + (1))))
tl_moves_completed = ((tl_full_column_moved_x) + (tl_moves))
tl_moves_remaining = (required_moves_per_rotation - tl_moves_completed)
#tl_moves_completed_positional = (tl_moves_completed - 1)