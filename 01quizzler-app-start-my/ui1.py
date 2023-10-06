from tkinter import *

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.THEME_COLOR = "#375362"
        self.window.config(pady=20, padx=20, bg=self.THEME_COLOR)
        self.create_widgets()
        self.window.mainloop()


    def create_widgets(self):
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2,in_=self.window)
        self.card_word = self.canvas.create_text(150, 125, text="123", font=("Arial", 20, "italic"))

        self.score_label = Label(self.window, text="Score: 0", bg=self.THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, padx=20, pady=20, in_=self.window)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=self.true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2, padx=20, pady=20, in_=self.window)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2, padx=20, pady=20, in_=self.window)


# THEME_COLOR = "#375362"
#
# window = Tk()
# window.title("Quizzler")
# window.config(pady=20, padx=20, bg=THEME_COLOR)
#
# canvas = Canvas(width=300, height=250, bg="white")
# canvas.grid(column=0, row=1, columnspan=2)
# card_word = canvas.create_text(150, 125, text="123", font=("Arial", 20, "italic"))
#
# score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
# score_label.grid(column=1, row=0, padx=20, pady=20)
#
#
# true_image = PhotoImage(file="images/true.png")
# true_button = Button(image=true_image, highlightthickness=0)
# true_button.grid(column=0, row=2, padx=20, pady=20)
# false_image = PhotoImage(file="images/false.png")
# false_button = Button(image=false_image, highlightthickness=0)
# false_button.grid(column=1, row=2, padx=20, pady=20)
#
# window.mainloop()

