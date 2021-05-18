from QuizResources.data import question_data
from QuizResources.question_model import Question
from QuizResources.quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

quiz_play = QuizBrain(question_bank)
while quiz_play.still_has_questions():
    quiz_play.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz_play.score}/{quiz_play.question_number}")