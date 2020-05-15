import math
# n! / r!(n-r)! - combination forumla
#if n is even then the formula equals
#(2n)! / (n!)**2
def Path_Routes(GridSize):
    p = math.factorial(GridSize*2)\
    /(math.factorial(GridSize)**2)
    return p

print(Path_Routes(20))
    
    