#reusing the code from problem 002

a = 1 # a saves the left term
placeholder = 1 #placeholder saves the right term
count = 1
index = 2 #2nd index = 1

while len(str(count)) < 1000:
    
    #Fibbonaci Sequence is just addition of two terms  
    count = count + placeholder
    
    #update the left Fibbonaci Term to complete the next additon
    placeholder = a
    
    #save the right Fibbonaci Term for the updation
    a = count
    
    #update index each time
    index += 1
    
print(index)

