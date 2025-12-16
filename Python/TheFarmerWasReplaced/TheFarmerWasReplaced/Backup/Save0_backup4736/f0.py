x = get_pos_x()
y = get_pos_y()
drone = x,y

if can_harvest():
	ox = x
	oy = y
	od = ox,oy
	nd = od
	nd += od
	print(nd)
	
