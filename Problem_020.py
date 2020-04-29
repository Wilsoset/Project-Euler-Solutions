def n_factorial(n): #function to find factorial of number n
    product = 1
    for x in range(1,n+1): # n+1 to include the last digit
        product *= x
    return str(product) #return as a string to easily manipulate later

def sum_digits(y): #function to sum the digits of any given string
    sum = 0
    for z in range(0, len(n_factorial(y))):
        sum += int(n_factorial(y)[z])
    return sum

print(sum_digits(100))
        

