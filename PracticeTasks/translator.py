'''
This program is basically to translate all the vowels into a desired string
'''

##inputStr = "This is a fruit name Orange. You could enjoy it!"
def translate(phrase):
    vowels = "AEIOUaeiou"
    translated = ''
    for chars in phrase:
        if (chars in vowels):
            translated = translated + '_'
        else: 
            translated = translated + chars
    return translated

inputString = input('Enter the string to translate all vowels in underscore:- ')
print(translate(inputString))