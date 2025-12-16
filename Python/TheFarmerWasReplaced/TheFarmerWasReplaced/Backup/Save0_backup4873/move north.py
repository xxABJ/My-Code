#move(North)
total_p = get_world_size() - 1
#x = get_pos_x()
#y = get_pos_y()

for north in range(total_p - get_pos_y()):
	move(North)
for south in range(get_pos_y()):
	move(South)