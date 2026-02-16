a, b, c, d = 0, 3, 4, 9

l = [a,b,c,d]

d = {
    't': b,
    'b': a,
    'l': c,
    'r': d
}



#print(list(reversed(sorted(l))))
print(f"list: {list(sorted(d.values()))}")

biggest = list(reversed(sorted(d.values())))

print(f"reversed: {biggest}")
print(f"biggest two: {biggest[:2]}\n")


full_list = list(d.keys())
print(f"full_list: {full_list}")
popped_value = full_list.pop(full_list.index('b'))
print(f"filtered_list: {full_list}")

print(d.get('t'))


A = (0, 4)
B = (2, 1)



print(tuple(a + b for a, b in zip(A, B)))