import math

def Triangle_Number(n):
   return int((n*(n+1)) / 2) #sum of natural numbers

#Only check for factors up to the square root of the
#triangle number - each number above has a mirror factor below.
#factor below.
def Num_of_Divisors(a): #no of divisors number a has 
    num = 0 #counter for no of divisors
    for w in range(1,int(math.sqrt(a))+1): #to reduce time complexity
        if a % w == 0: 
            num += 2 # since we sqrt the original number
    return num

print(Num_of_Divisors(80))

x = 0 #for the sake of the while loop
n = 1

while x == 0: 
    n += 1
    if Num_of_Divisors(Triangle_Number(n)) > 500:
        print(Triangle_Number(n))
        break
        
