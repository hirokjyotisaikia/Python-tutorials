mylist = {
    "marks" : [1,4,6,3],
    "hirok" : "A CSE student of Dibrugarh University",
     1 : 2,
     "vahicles" : {
         "cars" : "it is a 4 wheele vehicle",
         "bikes" : "it is a 2 wheeler vehicle"
     }
}
print(mylist.keys()) #prints the keys of the dictionary
print(mylist.values()) #prints the values of the keys
print(mylist.items()) #prints the (value and key) for all the contents of the dictionary
updatedict = {
    "narmada" : "friend"
}
mylist.update(updatedict) #update the dictionary and the keyword is updatedict and also updates the values which are already given
print(mylist)
print(mylist.get("narmada")) #will give the value of the dictionary or if the key is not correctly typed it will throw none
print(mylist["narmada"]) #will give the value but if the key is not typed correctly it will throw an error

#the difference between .get() and []
print(mylist.get("narmada2"))
print(mylist["narmada2"])