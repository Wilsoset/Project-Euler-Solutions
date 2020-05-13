def d(n): #return sum of divisors
    total = 0 
    for w in range(1,n): 
            if n%w == 0:
                total += w
    return total

Data = []

for x in range(1,10000):
    b = d(x) 
    a = d(b)
    if (x == a) and (b != a): #in the question
        Data.append(a) #just add it to the list
        
print(sum(Data))    
    






        


    

