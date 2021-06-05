#02062021_2 Write a .py script to get the occurances of a character (irrespective case sensitivity) from a sentence and get the index of that character as well. 
#For example the sentence is = "Python is a preferred programming language in today world of informations" and we need to get it for "p". Input should be provided by a variable.
sentence = "Python is a preferred programming language in today world of informations"
print("Sentence is:- " + sentence)
#input string for which we need to perform action
input_string = 'o'
print("Find occurances of character (ignore letter case): " + input_string)
#printig the length of sentence
lengthOfSentence = len(sentence)
#making the sentence in lower case
lowerSentence = sentence.lower()
replacedSentence = lowerSentence.replace(input_string.lower(),'')
replacedSentenceLength = len(replacedSentence)
occurancesOfChar = (lengthOfSentence - replacedSentenceLength)
print(occurancesOfChar)