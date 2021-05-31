from os import path, sys
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomorodo")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas with tomato image and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file=path.join(sys.path[0], 'tomato.png'))
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

#Buttons
start = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()