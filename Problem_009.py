# a + b + c = 1000
# a**2 + b**2 = c**2
# c = (a**2 + b**2)**0.5 

x = 1000 # a+b+c value

for a in range(1,x+1): #looping through testing values of a and b
    for b in range(a, x+1): #ensuring that b > a
        if a + b + ((a**2 + b**2)**0.5) == x: #using the rearranged formula above
            c = int(((a**2 + b**2)**0.5))
            print('a:' + str(a) + \
                  'b:' + str(b) + \
                  'c:' + str(c))
            print(a*b*c)

