r = 1
b = 3
c = 5

while r < 2:
	r += 1
	for repeat in range(c % 2):
		if c % 2 == 1:
			##
			r -= 1
			#b += 1
			c += c+3
		else:
			##
			r += 1
		do_a_flip()
		print('c = ',c,'b = ',b,'r = ',r)