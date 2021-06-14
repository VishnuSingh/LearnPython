#basic calculator to do calculation
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
operation = input("Enter operation: ")

if operation == '+' :
    result = float(num1)  + float(num2)
elif operation == '-' : 
    result = float(num1)  - float(num2)
elif operation == '*' :
    result = float(num1)  * float(num2)
elif operation == '/' : 
    result = float(num1)  / float(num2)
else:
     result = float(num1)  % float(num2)

print(result)
