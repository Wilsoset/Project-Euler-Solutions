# a saves the left term while placeholder saves the right term
a = 1
count = 1
placeholder = 1
sum = 0
while count <= 4000000:
    if (count % 2 == 0):
        sum = count + sum
    #Fibbonaci Sequence is just addition of two terms  
    count = count + placeholder
    #update the left Fibbonaci Term to complete the next additon
    placeholder = a
    #save the right Fibbonaci Term for the updation
    a = count
print(sum)