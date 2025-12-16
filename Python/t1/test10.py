n_floors = 4
chars = n_floors*2-1
star = []
s = "*"
space = " "
num = 2
for i in range(n_floors):
    for j in range(1):
        star.append(s*chars)
    chars-=num
    for index, value in enumerate(star):
        #if i != n_floors*2-1:
        if index != len(star):
            star[i] = space*(int(num*0.5))+star[i]+space*(int(num*0.5))

    #if i > 0:
    #    for index, value in enumerate(star[i]):
    #        star[i] = space*(int(num*0.5))+star[i]+space*(int(num*0.5))
    #        #star[0] += space*(int(num*0.5))
    #        #star[-1] += space*(int(num*0.5))
    #        #star.append(space*(int(num*0.5)))
    #        #star.append(space*(int(num*0.5)))
    #        num-=2
            
print(star[::-1])