Python Key Points
===========================
Session  =  1   
===========================

Python is the first programming language. Its very simple and generatl purpose language.

Python is like an english language we don't need to write complex logic to do simple things.
 Like if we want to print "Hello World" then in Java / C / C++ we need to import/write some class then only we can do this.
 But in python we can do it in simple way as below:-

 print("Hello World")


 ---> Python is a dynamically typed language. Like we don't need to assign the datatype of any variable. 
 It assigned dynamically based on the value it assigned.

 Like a = 10
 It means a is a type of int. 
 Below is a simple program to identfy or as a prove to find the type of a variable

>>> a =True
>>> print(a)
True
>>> type(a)
<type 'bool'>
>>>
... print(a)
True
>>> a = 10
>>> type(a)
<type 'int'>
>>>

---> We can define our own function in the python.
Ex:-
def f1():print("function one")
f1()

output[function one]

================================
----> Where we can use python:-
================================

1. Desktop application development
2. Web application development
3. Database application
4. Networking application
5. Games
6. Data Analysis / data science
7. Machine learning
8. AI (Artificial Intelegancy)
9. IOT Applications (IOT --> Internet of Things)



Companies where python is using:-
==========================
Google, youtube, facebook, Dropbox, NASA and many more.....
---------------



Session  =  2   
===========================

FEATURES OF THE PYTHON
----------------------

1. simple and easy to learning
2. free-ware and open source
3. high level programming language
4. Platform independent
5. Portability
6. dynamically typed language
7. Both procedure and object oriented language
8. interpreted
9. extensible
10. embeded


---> Example to import a module
Here we are importing math module and printing sqrt of a number 4

import math
print(math.sqrt(4))


[output = 2.0]


----> Example to write the random number from 0,9

from random import *
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

[output:-
236755
113349
684526
]




WORKING WITH STRING
======================================

---> In the string datatype 0 is the first index of string character and if we want to get the reverse index then last character is on index -1

---> index() function is used to find the index of a character or string (provided as parameter of index() function). But it raise exception if the given character not find in the 
string.


 Python has a set of built-in methods that you can use on strings.
---------------
> Note: All string methods returns new values. They do not change the original string.


Method--->Description
-------------------
- **capitalize()**	Converts the first character to upper case
- **casefold()**	Converts string into lower case
- **center()**	Returns a centered string
- **count()**	Returns the number of times a specified value occurs in a string
- **encode()**	Returns an encoded version of the string
- **endswith()**	Returns true if the string ends with the specified value
- **expandtabs()**	Sets the tab size of the string
- **find()**	Searches the string for a specified value and returns the position of where it was found
- **format()**	Formats specified values in a string
- **format_map()**	Formats specified values in a string
- **index()**	Searches the string for a specified value and returns the position of where it was found
- **isalnum()**	Returns True if all characters in the string are alphanumeric
- **isalpha()**	Returns True if all characters in the string are in the alphabet
- **isdecimal()**	Returns True if all characters in the string are decimals
- **isdigit()**	Returns True if all characters in the string are digits
- **isidentifier()**	Returns True if the string is an identifier
- **islower()**	Returns True if all characters in the string are lower case
- **isnumeric()**	Returns True if all characters in the string are numeric
- **isprintable()**	Returns True if all characters in the string are printable
- **isspace()**	Returns True if all characters in the string are whitespaces
- **istitle()**	Returns True if the string follows the rules of a title
- **isupper()**	Returns True if all characters in the string are upper case
- **join()**	Joins the elements of an iterable to the end of the string
- **ljust()**	Returns a left justified version of the string
- **lower()**	Converts a string into lower case
- **lstrip()**	Returns a left trim version of the string
- **maketrans()**	Returns a translation table to be used in translations
- **partition()**	Returns a tuple where the string is parted into three parts
- **replace()**	Returns a string where a specified value is replaced with a specified value
- **rfind()**	Searches the string for a specified value and returns the last position of where it was found
- **rindex()**	Searches the string for a specified value and returns the last position of where it was found
- **rjust()**	Returns a right justified version of the string
- **rpartition()**	Returns a tuple where the string is parted into three parts
- **rsplit()**	Splits the string at the specified separator, and returns a list
- **rstrip()**	Returns a right trim version of the string
- **split()**	Splits the string at the specified separator, and returns a list
- **splitlines()**	Splits the string at line breaks and returns a list
- **startswith()**	Returns true if the string starts with the specified value
- **strip()**	Returns a trimmed version of the string
- **swapcase()**	Swaps cases, lower case becomes upper case and vice versa
- **title()**	Converts the first character of each word to upper case
- **translate()**	Returns a translated string
- **upper()**	Converts a string into upper case
- **zfill()**	Fills the string with a specified number of 0 values at the beginning




WORKING WITH NUMBERS
======

There are lot of number function available in puthon

## There are three numeric types in Python:

1. int  --> (x = 1)
2. float --> (x = 1.10)
3. complex --> (x = 3+5j)

and if we want to access math module we can just impor the math module as below

## from math import *

## Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:


import random

print(random.randrange(1, 10))


Lists
=====

List is like an array in the other programing language or as a sequenece in the xpath/xslt.
In the list index is also start from 0.
ex:- listOFFriends = \["Amarjeet","Pravesh","Prayag","Rajiv","Vishnu"]
index starts from 0:-     0         1           2       3       4

 So if we want to access the Name **Prayag** we will write the below code.
 
 >>>print(listOFFriends\[2])
 
 