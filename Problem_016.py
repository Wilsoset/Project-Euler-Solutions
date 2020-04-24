def is_prime(n): #function to determine if number n is prime
    if n % 2 == 0: 
        return False #if even then not prime
    p = 3 #smallest prime number is 3
    while p < (n ** 0.5) + 1: # only need to check the first half of a number
        if n % p == 0: 
            return False
        p += 2 #skip over even numbers
    return True

def sum_of_primes(max): #function to sum all prime numbers up to max
    sum = 2 #2 is the first prime number
    prime_tester = 3 #again 3 is smallest prime number
    while prime_tester < max:
        if is_prime(prime_tester):
            sum  += prime_tester #sum the number if its a prime
        prime_tester += 2 #again skip over even numbers
    return sum

x = sum_of_primes(2000000)

print(x)