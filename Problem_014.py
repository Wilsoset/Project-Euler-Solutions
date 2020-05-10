def Collatz(n): 
    count = 1
    while n !=1: #sequence finishes at 1
        if n%2 == 0:
            n = n/2
        else:
            n = (3*n)+1
        count += 1
    return count

most_links = 0 

for x in range (1,999999): # under one million
    if  Collatz(x) > most_links: 
        most_links = Collatz(x)
        print(x)
       
