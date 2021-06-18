#exception handling
#name = str(input('Enter the name: '))
phone = int(input('Enter the phone number: '))

try :
    #print(name)
    print(phone)
except ValueError:
    print('Invalid input')
    

