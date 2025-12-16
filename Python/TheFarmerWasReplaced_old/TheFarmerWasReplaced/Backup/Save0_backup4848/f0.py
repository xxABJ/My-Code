x = get_pos_x()
y = get_pos_y()
drone = x,y

a = 2
ox = ''
oy = ''
od = ''
nx = ''
ny = ''
nd = ''

for r2 in range(1):
	for r in range(a):
		#od = nd
		if can_harvest():
			ox = (x)
			oy = (y)
			od = ox,oy
			#print(od)
	move(North)
	nx = get_pos_x()
	ny = get_pos_y()
	nd = nx,ny
	print(nd,(od))
			#nd += od
			#print(nd)