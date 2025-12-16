size = 3
even_farmland = (size % 2 == 0)
odd_farmland = (size % 2 == 1)

a = True
b = False
world_sizee = 0

def world_size():
    if size % 2 == 0:
        world_size = 4
    elif size % 2 == 1:
        world_size = 2
    return world_size

t = (even_farmland == False and 4)
nt = (even_farmland == False and world_size())


print('odd =',t)
print(nt)
