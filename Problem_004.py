#function to determine if a number (i) is a palindrome
def is_palindrome(i):
    return str(i) == str(i)[::-1]
#[::-1] gives us the last digit of the number

largest_p = 0 #variable for the largest palindrome

for i in range(100, 999): #going through all 3 digit numbers
    for j in range(i+1, 1000):
        p = i * j    #multiplying with every other 3 digit number
        if is_palindrome(p) and p > largest_p: 
          largest_p = p 

print(largest_p)
