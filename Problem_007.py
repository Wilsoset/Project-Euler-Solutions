def is_prime(n): #function to determine if number n is prime
    if n % 2 == 0: 
        return False #if even then not prime
    p = 3 #smallest prime number is 3
    while p < (n ** 0.5) + 1: # only need to check the first half of a number
        if n % p == 0: 
            return False
        p += 2 #skip over even numbers
    return True

def nth_prime_number(z): #function to find the nth prime number
    p_number = 2 #2 is the first prime number
    counter = 1 #counter for how many prime numbers its been
    prime_tester = 3 #3 is smallest prime number
    while counter < z:
        if is_prime(prime_tester):
            counter  += 1 #add one to the counter when the number is prime
            p_number = prime_tester #it is the corresponding nth prime number
        prime_tester += 2 #skip over even numbers
    return p_number

x = nth_prime_number(10001)

print(x)