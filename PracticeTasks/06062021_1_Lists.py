#lists
friendsList = ["Amar","Pravesh","Prayag","Raj","Vish","Love","DK","Girish"]
#printing the 3 element of the list
print(friendsList[3:4])

#list can also be slice with elements as we already did for string. Like
#print element index 1 in a step of 3 till the element 6, It should print "Pravesh", "Vish" but not Girish as the index is out of range of index 6.
print(friendsList[1:6:3]) 

#we can also do the reverse of this list (as we alredy did for string for my name) "Vishnu" into "unhsiV"
print(friendsList[::-1])

#change an element let say "Raj" into "Rajeev" here
friendsList[3] = "Rajeev"
print(friendsList)