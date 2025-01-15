class QuizBrain:
    def __init__(self, quest_list):
        self.score = 0
        self.question_number = 0
        self.question_list = quest_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)? : ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print('Well Done You Are Right!!')
            self.score += 1
        else:
            print('Sorry!! You Are Wrong.')

        print(f"Correct Answer is {question_answer}")
        print(f"Your Score is {self.score}/{self.question_number} \n")



