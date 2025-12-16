x = get_pos_x()
y = get_pos_y()
drone = x,y

a = 1
ox = ''
oy = ''
od = ''
nx = ''
ny = ''
nd = ''

for r in range(a):
	#od = nd
	if can_harvest():
		ox = x
		oy = y
		od = ox,oy
		print(od)
move(North)
nx = ox
ny = oy
nd = nx,ny
print(nd)
			#nd += od
			#print(nd)