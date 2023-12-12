"""An array is a data structure which is composed of a group of elements which are all of the same data type"""

names=["","","","",""]

for i in range(0,5): # names input into array, only takes 5 names
    names[i]=input("name? ")

for i in range (len(names)): # print names individually
    print(names[i])