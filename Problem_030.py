sum = 0

for a in range(2,1000000): #skip 1 and generic big value
    x = 0 
    for b in str(a): 
        x += int(b)**5
    if x == a: #if sum of fith powers of digits equals number
        sum += x
        print(x)
        
print(sum)
     