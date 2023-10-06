from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    # 设置传入的参数的数据类型是 QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        # 初始化时就调用这个方法
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_next = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_next)


    def answer_true(self):
        check_result = self.quiz.check_answer("True")
        if check_result == "True":
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def answer_false(self):
        check_result = self.quiz.check_answer("False")
        if check_result == "False":
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()



