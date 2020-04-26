product = 0 

for i in range(1, 1001):
    product += i**i

print(str(product)[-10:]) #the last 10 digits
    