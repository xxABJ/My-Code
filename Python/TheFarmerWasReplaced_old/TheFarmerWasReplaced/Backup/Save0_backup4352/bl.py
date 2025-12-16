x = get_pos_x()
y = get_pos_y()
drone = x,y

total_side_length = get_world_size()
zero = (total_side_length - total_side_length)
total_side_length_positional = (get_world_size() - 1)

top_side = (y == total_side_length_positional)
bottom_side = (y == zero)
left_side = (x == zero)
right_side = (x == total_side_length_positional)

top_left_block = (top_side and left_side)
top_right_block = (top_side and right_side)
bottom_left_block = (bottom_side and left_side)
bottom_right_block = (bottom_side and right_side)

detection_of_unharvested_crop_during_main_harvesting_rotaion = 0
main_harvesting_rotation = 1
number_of_required_set_rotations = (get_world_size() // 2)

desired_rotations_for_when_detection_of_farmland_not_harvested = 2
desired_rotations_positional = (desired_rotations_for_when_detection_of_farmland_not_harvested - 1)
live_rotation_counter = 0

required_moves_per_rotation = (total_side_length ** 2)
#full_column_moved = total_side_length

#Starting at bottom_left (bl) moves' calculator. (HARVEST at end of set required)

bl_full_column_moved_x = (x * total_side_length)
#bl_moves_north = ((full_column_moved_completed % 2 == 0) and (y))
#bl_moves_south = ((full_column_moved_completed > 0) and (total_side_length - y))
bl_moves = (((bl_full_column_moved_x % 2 == 0) and (y + 1)) or (((bl_full_column_moved_x > 0) and (bl_full_column_moved_x % 2 == 1)) and (total_side_length - y)))
bl_moves_completed = (bl_full_column_moved_x) + (bl_moves)  #(bl_moves_odd)
bl_moves_remaning = (required_moves_per_rotation - bl_moves_completed)
bl_moves_completed_positional = (bl_moves_completed - 1)

#print(bl_moves)
print(bl_moves_completed_positional)
print(bl_moves_remaning)