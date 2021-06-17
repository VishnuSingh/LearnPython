var = input('Enter a string: ')
vowels = "AEIOUaeiou"
for x in var:
    if x in vowels:
        print('_')
    else:
        print(x)