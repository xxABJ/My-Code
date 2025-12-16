total_sets = 4
set_order_number = 1 #sets into numbers & (current_set)
l = 1
p = 1
o = 0 

while (total_sets - set_order_number) > (l - p) > 0:
	for up in range(1):
		l += 1
		o += 1
		print(o)