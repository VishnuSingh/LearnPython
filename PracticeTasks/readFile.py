friendsList = open("friends_list.txt","r")
for friends in friendsList.readlines():
    print(friends)
friendsList.close()