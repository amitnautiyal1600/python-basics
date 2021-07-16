class Question:
        def __init__(self, prompt, answer):
                self.prompt = prompt
                self.answer = answer


questions_prompts = [
    "\n\nWhat colors are Apple? \n(a) Red\n(b) Blue\n(c) Yellow\n(d) Black\n\n",
    "\n\nWhat colors are Banana? \n(a) Red\n(b) Blue\n(c) Yellow\n(d) Black\n\n",
    "\n\nWhat colors are Sky? \n(a) Red\n(b) Blue\n(c) Yellow\n(d) Black\n\n",
    "\n\nWhat colors are Night? \n(a) Red\n(b) Blue\n(c) Yellow\n(d) Black\n\n"
]

questions = [
    Question(questions_prompts[0], 'a'),
    Question(questions_prompts[1], 'c'),
    Question(questions_prompts[2], 'b'),
    Question(questions_prompts[3], 'd'),
]

def run_test(questions):
    score = 0
    for question in questions :
        answer =  input(question.prompt)
        if answer == question.answer:
            score +=1
    print( "You got : "+ str(score) + "/"+ str(len(questions)) + " correct")

run_test(questions)
