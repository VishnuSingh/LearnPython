friendsList = open("/Users/vis/Documents/Private/Python/LearnPython/PracticeTasks/friends_list.txt","r")
#print(friendsList.readable())
#print(friendsList.read())
#print(friendsList.readline())
#print(friendsList.readline())
#print(friendsList.readline())
#print(friendsList.readlines())

for friends in friendsList.readlines():
    print(friends,end='')
friendsList.close()
