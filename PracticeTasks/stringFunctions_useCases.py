#pythong differnet predefine 'string' function usecases

inputString = "this is the input string as a use case to check the possible string functions in PYTHON"

#capitalize()	Converts the first character to upper case
    #Note: It chnage the rest of character in lower case.
print(inputString.capitalize())
#This is the input string as a use case to check the possible string functions in python

#casefold()	Converts string into lower case
print(inputString.casefold())

#center()	Returns a centered string
#string.center(length, character)
    #length	Required. The length of the returned string
    #character	Optional. The character to fill the missing space on each side. Default is " " (space)

print(inputString.center(50,'>'))

#count()	Returns the number of times a specified value occurs in a string
    #string.count(value, start, end)
        #value	Required. A String. The string to value to search for
        #start	Optional. An Integer. The position to start the search. Default is 0
        #end	Optional. An Integer. The position to end the search. Default is the end of the string
print(inputString.count('the'))

# we can provide a character or word to find its occurance and give the start and end point for search.


