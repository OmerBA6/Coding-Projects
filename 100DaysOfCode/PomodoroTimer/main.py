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
CHECK_MARK = '✔'
cycles = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global cycles
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    cycles = 0
    check_marks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global cycles
    cycles += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if cycles % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif cycles % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(sec_number):
    count_min = math.floor(sec_number / 60)
    count_sec = sec_number % 60
    canvas.itemconfig(timer_text, text="%02d:%02d" % (count_min, count_sec))

    if sec_number > 0:
        global timer
        timer = window.after(1000, count_down, sec_number - 1)
    else:
        start_timer()
        word_sessions_done = math.floor(cycles/2)
        check_marks = ""
        for _ in range(word_sessions_done):
            check_marks += CHECK_MARK
        check_marks_label.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(row=1, column=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Labels
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
title_label.grid(row=0, column=1)

check_marks_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
check_marks_label.grid(row=3, column=1)


window.mainloop()
