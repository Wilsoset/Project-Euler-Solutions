from itertools import permutations 
  
# all permutatuons from 0123456789
perm = permutations([0,1,2,3,4,5,6,7,8,9]) 

#working wih lists to make things easier
MyList = []

for i in list(perm): 
    MyList.append(i)

#sorting numerically    
sorted_MyList = sorted(MyList)

#the millionth permutation
print(sorted_MyList[999999])
    