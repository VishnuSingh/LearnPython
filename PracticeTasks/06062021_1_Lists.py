#lists
friendsList = ["Amar","Pravesh","Prayag","Raj","Vish","Love","DK","Girish"]
#printing the 3 element of the list
print(friendsList[3:4])

#list can also be slice with elements as we already did for string. Like
#print element index 1 in a step of 3 till the element 6, It should print "Pravesh", "Vish" but not Girish as the index is out of range of index 6.
print(friendsList[1:6:3]) 

#we can also do the reverse of this list (as we alredy did for string for my name) "Vishnu" into "unhsiV"
print(friendsList[::-1])
#list is also provide a method reverse() to reverse the list elements
#The reverse() method does not return any value but reverse the given object from the list. Like if we try to do it like
  #print(friendsList.reverse()) then it will not print anyting and provide 'None' as result.
print("Reverse function")
friendsList.reverse()
print(friendsList)


#change an element let say "Raj" into "Rajeev" here
friendsList[3] = "Rajeev"
print(friendsList)

#append() -- append an element in the list. 
friendsList.append("Vishal")
print(friendsList)

#another list
ageOfFrieds = ["30","35","40","42","32","47","38"]

#extend the friends list
friendsList.extend(ageOfFrieds)
print(friendsList)

#clear() the ageOfFrieds lsit
ageOfFrieds.clear()
print(ageOfFrieds)

#copy of the list
copyofFL = friendsList.copy()
print(copyofFL)

#insert() insert an element on the specific index.
copyofFL.insert(10,"42")
print(copyofFL)

#count() count() an element in the list
print(copyofFL.count('42'))

#pop() pop removes the last element
print(copyofFL.pop())
print(copyofFL)

#sort() sort the list
copyofFL.sort()
print(copyofFL)

#index() is to print the index of an element from the list.
print(copyofFL.index("DK"))

#The remove() method removes the first occurrence of the element with the specified value.
copyofFL.remove("42")
print(copyofFL)



