g = 0
r = 0
b = 1

while True:
	if g == 0:
		for b in range(b):
			g = 1
			b = 0
			print('harvest')
	
	elif (g > 0) and (r < 2):
		g = 0
		b = 1
		r += 1
		print(r)
		#r = r

	else:
		break
	