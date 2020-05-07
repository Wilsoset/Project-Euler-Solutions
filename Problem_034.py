#function from Problem 020

def n_factorial(n): #function to find factorial of number n
    product = 1
    for x in range(1,n+1): # n+1 to include the last digit
        product *= x
    return product 

sum_of_curious = 0

for i in range(3,1000000): #any large number works
    sum_of_factorial = 0
    for z in str(i): #turn into string to loop through
        sum_of_factorial += n_factorial(int(z)) 
    if sum_of_factorial == i:
        sum_of_curious += sum_of_factorial
            
print(sum_of_curious)