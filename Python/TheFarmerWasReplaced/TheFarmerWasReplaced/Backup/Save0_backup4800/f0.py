x = get_pos_x()
y = get_pos_y()
drone = x,y

a = 2
nd = ''
od = ''

for r2 in range(a):
	nd = ''
	od = ''
	for r in range(a):
		nd = od
		print(nd)
		if can_harvest():
			move(North)
			ox = x
			oy = y
			od = ox,oy
			nd = od
			#nd += od
			#print(nd)
		elif can_harvest() and (od = nd):
			nd = od
			print(od)
	od = nd
	print(nd)