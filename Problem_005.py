#function to determine if number is divisble by 1 to 20
def isDivisible(n):
    for i in range(1,21):
        if n%i != 0:
            return False
    return True
    
number = 20
while True:
    if isDivisible(number):
        break
    number += 20 #has to be divisible by 20 so increment by 20
    
print (number)