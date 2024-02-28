#creating an empty set and adding values to it by using its function
b = set()

b.add(3)
b.add(2)
b.add(4) #set.add() takes exactly one argument
b.add((5,6,7))# to take multiple argument we have to add tuple ()
print(b)

#in sets we cannot add dictionary or list 

print(len(b)) #tells the length of the set
b.remove(4) #removes a specific value from the set
print(b.pop())