a = 78
if(a>90):
    print("Th value of a is greater than 90")
if(a<90):
    print("The value of a is smaller than 90")

if(a == 78):
        print("the value of a is same")
else:
    print("The values are equal")

    #logical and relational operators

age_limit = int(input("Enter your age: "))

if(age_limit >=18 and age_limit <= 35): #with and operators
     print("you can work with us")
else:
     print("you cannot work with us")

age_criteria = int(input("Enter your age: "))

if(age_criteria >=18 or age_criteria <= 35): #with or operators
     print("you can work with us")
else:
     print("you cannot work with us")


g = None
if(g is None): #pointing to the same object
     print("yes")
else:
     print("no")





h = [1,2,3,4,5]
print(2 in h) #it will check whether 2 is in the list or not if it is in the list then it will show true ot if it is not present then it will show false
