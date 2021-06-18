from Questions import Questions

questionPrompts = [
    "1. Capital of India: \n(a) Jaipur\n(b) Delhi\(c)Mumbai",
    "2. PM of India: \n(a) N Modi\n(b) R Gandhi\(c)A Kejri",
    "3. Indian currency: \n(a) Dollar\n(b) Euro\(c)Rupees",
    "4. Current year: \n(a) 2021\n(b) 2020\(c)2022",
    "5. Current Month: \n(a) May\n(b) June\(c)July"
]

questions = [
    Questions(questionPrompts[0], b),
    Questions(questionPrompts[0], a),
    Questions(questionPrompts[0], c),
    Questions(questionPrompts[0], a),
    Questions(questionPrompts[0], b)
]

def runTest():
    score = 0
    for question in questions:
        answer = input(question.questionPrompt)
        if answer == question.answer:
            score += 1
    print("You score " + str(score) + "out of" + str(len(questions)))

runTest()


