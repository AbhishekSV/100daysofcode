from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Game Over!")
            self.correct.config(state='disabled')
            self.wrong.config(state='disabled')
    
    
    def score_update(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    
    
    def user_answer_true(self):
        self.score_update(self.quiz.check_answer("True"))
    
    
    def user_answer_false(self):
        self.score_update(self.quiz.check_answer("False"))
    
        
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Test 123", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        right_img = PhotoImage(file='images/true.png')
        self.correct = Button(image=right_img, highlightthickness=0, command=self.user_answer_true)
        self.correct.grid(column=0, row=2)
        
        wrong_img = PhotoImage(file='images/false.png')
        self.wrong = Button(image=wrong_img, highlightthickness=0, command=self.user_answer_false)
        self.wrong.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
    