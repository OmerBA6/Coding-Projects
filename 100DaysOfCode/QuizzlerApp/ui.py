from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox


THEME_COLOR = "#375362"
QUESTION_FONT = ('Ariel', 20, 'italic')
SCORE_FONT = ('Ariel', 20, 'bold')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Images ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        check_mark_image = PhotoImage(file="images/true.png")
        x_mark_image = PhotoImage(file="images/false.png")
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Buttons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        self.check_mark_button = Button(image=check_mark_image, highlightthickness=0, borderwidth=0,
                                        command=self.check_if_true)
        self.x_mark_button = Button(image=x_mark_image, highlightthickness=0, borderwidth=0,
                                    command=self.check_if_false)

        self.check_mark_button.grid(row=2, column=0)
        self.x_mark_button.grid(row=2, column=1)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Canvas ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Title",
                                                     font=QUESTION_FONT,
                                                     fill=THEME_COLOR
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Label ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        self.score_label = Label(text="Score: ", highlightthickness=0,
                                 bg=THEME_COLOR, fg='white', font=SCORE_FONT)
        self.score_label.grid(row=0, column=1)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        try:
            q_text = self.quiz.next_question()
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz.\nYour final score was: "
                                                            f"{self.quiz.score}/{len(self.quiz.question_list)}")
            self.check_mark_button.config(state='disabled')
            self.x_mark_button.config(state='disabled')
        else:
            self.canvas.itemconfig(self.question_text, text=q_text)
        finally:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg='white')

    def check_if_true(self):
        if self.quiz.check_answer("True"):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def check_if_false(self):
        if self.quiz.check_answer("False"):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, is_answer_corrct):
        if is_answer_corrct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
