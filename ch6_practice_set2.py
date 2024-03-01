'''to check the marks of the student and the criteria is to get above 33% in all the subjects and total % should be 40 or the student 
is fail'''
sub1 = int(input("Enter marks of subject 1 : "))
sub2 = int(input("Enter marks of subject 2 : "))
sub3 = int(input("Enter marks of subject 3 : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("\nYou have failed the test becaise % is less than 33 ")


elif(sub1+sub2+sub3)/3<40:
    print("\nYou have failed the test because overall percentage is below 40%")

else:
    print("You have passed the test")