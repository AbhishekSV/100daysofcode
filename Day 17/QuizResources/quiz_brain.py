class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self, user_choice, correct_answer):
        if user_choice.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.check_answer(user, current_question.answer)
