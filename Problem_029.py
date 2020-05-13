def removeDuplicates(listofstuff): #not my function but it works
    # Create an empty list to store unique elements
    uniqueList = []
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofstuff:
        if elem not in uniqueList:
            uniqueList.append(elem)
    # Return the list of unique elements        
    return uniqueList

mylist = []

for a in range (2,101): 
    for b in range(2,101):
        mylist.append(a**b) #formula in the problem
        
mylist.sort() #from smallest to largest
mylist = removeDuplicates(mylist)
print(len(mylist))
