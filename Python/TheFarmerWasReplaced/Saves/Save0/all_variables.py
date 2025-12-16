from __builtins__ import *

x = get_pos_x()
y = get_pos_y()
drone = x,y
total_side_length = get_world_size()
zero = 0
total_side_length_positional = (get_world_size() - 1)

# Assigning blocks to the "Starting Points" of the sets.
top_side = (get_pos_y() == total_side_length_positional)
bottom_side = (get_pos_y() == zero)
left_side = (get_pos_x() == zero)
right_side = (get_pos_x() == total_side_length_positional)
tl_block = (top_side and left_side) 	                    # A block representing the Top-left "Starting Point" set.
tr_block = (top_side and right_side) 	                    # A block representing the Top-right "Starting Point" set.
bl_block = (bottom_side and left_side) 	                    # A block representing the Bottom-left "Starting Point" set.
br_block = (bottom_side and right_side)	                    # A block representing the Bottom-right "Starting Point" set.
tro_block = ((total_side_length % 2 == 1) and (tr_block))   # A block representing the Top-right-odd "Starting Point" set. (odd farm size).

# Assigning "Starting Points" set variables with corresponding numbers.
bl_set = 0 		# Bottom-left set.
br_set = 1 		# Bottom-right set.
tr_set = 2 		# Top-right set.
tro_set = 2     # Top-right-odd set.
tl_set = 3 		# Top-left set.

# Set and Direction system.
current_set = 0	# Current set indicator.
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
harvesting_rotations = ((even_farmland_set_rotation_count) or (odd_farmland_set_rotation_count))
remaining_harvesting_rotations = (harvesting_rotations - current_set)
main_harvesting_rotations = (remaining_harvesting_rotations)
number_of_required_set_rotations = (get_world_size() // 2)

desired_rotations_for_when_detection_of_farmland_not_harvested = 2
desired_rotations_positional = ((desired_rotations_for_when_detection_of_farmland_not_harvested) - (1))
live_rotation_counter = 0

# The Remaining Moves system.
required_moves_per_rotation = (total_side_length ** 2)

# Starting at bottom_right (bl) move calculator. (HARVEST at end of set required)
bl_full_column_moved_x = (get_pos_x() * total_side_length)
bl_moves = (((bl_full_column_moved_x % 2 == 0) and (get_pos_y() + 1)) or (((bl_full_column_moved_x > 0) and (bl_full_column_moved_x % 2 == 1)) and (total_side_length - get_pos_y())))
bl_moves_completed = ((bl_full_column_moved_x) + (bl_moves))
bl_moves_remaining = (required_moves_per_rotation - bl_moves_completed)

# Starting at bottom_right (br) move calculator. (HARVEST at end of set required)
br_full_row_moved_y = (get_pos_y() * total_side_length)
br_moves = (((br_full_row_moved_y % 2 == 0) and (total_side_length - get_pos_x())) or (((br_full_row_moved_y > 0) and (br_full_row_moved_y % 2 == 1)) and (get_pos_x() + 1)))
br_moves_completed = ((br_full_row_moved_y) + (br_moves))
br_moves_remaining = (required_moves_per_rotation - br_moves_completed)

# Starting at top_right (tr) move calculator. (HARVEST at end of set required)
tr_full_column_moved_x = ((total_side_length_positional - get_pos_x()) * (total_side_length))
tr_moves = (((tr_full_column_moved_x % 2 == 0) and (total_side_length - get_pos_y())) or (((tr_full_column_moved_x > 0) and (tr_full_column_moved_x % 2 == 1)) and (get_pos_y() + 1)))
tr_moves_completed = ((tr_full_column_moved_x) + (tr_moves))
tr_moves_remaining = (required_moves_per_rotation - tr_moves_completed)

# Starting at top_right_odd (tro) move calculator. (HARVEST at end of set required)
tro_full_column_moved_y = ((total_side_length_positional - get_pos_y()) * (total_side_length))
tro_moves = (((tro_full_column_moved_y % 2 == 0) and (total_side_length - get_pos_x())) or (((tro_full_column_moved_y > 0) and (tro_full_column_moved_y % 2 == 1)) and (get_pos_x() + 1)))
tro_moves_completed = ((tro_full_column_moved_y) + (tro_moves))
tro_moves_remaining = (required_moves_per_rotation - tro_moves_completed)

# Starting at top_left (tl) move calculator. (HARVEST at end of set required)
tl_full_column_moved_y = ((total_side_length_positional - get_pos_y()) * (total_side_length))
tl_moves = (((tl_full_column_moved_y % 2 == 0) and (get_pos_x() + 1)) or ((tl_full_column_moved_y > 0) and (tl_full_column_moved_y % 2 == 1) and ((total_side_length_positional - get_pos_x()) + (1))))
tl_moves_completed = ((tl_full_column_moved_y) + (tl_moves))
tl_moves_remaining = (required_moves_per_rotation - tl_moves_completed)