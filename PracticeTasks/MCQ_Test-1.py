from Questions import Questions
'''class Questions:
    def __init__(self, questionPrompt, answer):
        self.questionPrompt = questionPrompt
        self.answer = answer
'''
questionPrompts = [
    "1. Capital of India: \n(a) Jaipur\n(b) Delhi\n(c)Mumbai\n",
    "2. PM of India: \n(a) N Modi\n(b) R Gandhi\n(c)A Kejri\n",
    "3. Indian currency: \n(a) Dollar\n(b) Euro\n(c)Rupees\n",
    "4. Current year: \n(a) 2021\n(b) 2020\n(c)2022\n",
    "5. Current Month: \n(a) May\n(b) June\n(c)July\n"
]

questions = [
    Questions(questionPrompts[0], 'b'),
    Questions(questionPrompts[1], 'a'),
    Questions(questionPrompts[2], 'c'),
    Questions(questionPrompts[3], 'a'),
    Questions(questionPrompts[4], 'b')
]

def runTest():
    score = 0
    for question in questions:
        answer = input(question.questionPrompt)
        if answer == question.answer:
            score += 1
    print("You score " + str(score) + " out of " + str(len(questions)))

runTest()


