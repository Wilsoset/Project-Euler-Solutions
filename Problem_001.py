#setting up the sum variable
sum = 0
#looping through the first 1000 digits
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
# if its a multiple of 3/5, add it to x
        sum += i
print(sum)