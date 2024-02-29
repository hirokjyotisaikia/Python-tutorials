greeting = "Good Morning, "
name = "Hirok"
print(greeting + name)
print(type(greeting))
#concenating two strings
print(name[0:]) #prints the characters from the string "Hirok" from where till where we want it

#string Functions
print("\nThis is string function")
string = "today i went  with gaja to deliver a  package at chabua and also met pondit who was at mohonabri"
print(len(string)) #counts the total number of characters
print(string.endswith("chabua")) #checks whether the string ends with the given string
print(string.count("went")) #counts the number of characters or strings which was used
print(string.capitalize()) #to capitalize the first string if it is in small
print(string.find("pondit")) #to find the string at which position it is located
print(string.replace("pondit","Mriganka")) #replace old word with new word
print(string.startswith("p")) #will print the word that starts with s
