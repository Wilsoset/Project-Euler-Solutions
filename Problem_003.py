n = 600851475143
# i represents all the factors to divide by
i = 2
# would waste time for the product of factors to be larger than the number
while i * i < n:
     if n % i == 0:
         #dividing n by all these integers ensures the final value itself is prime
         n = n / i
     i = i + 1
print(n)