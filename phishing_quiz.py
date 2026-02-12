import tkinter as tk #Used to present the quiz via a graphical user interface
from tkinter import messagebox

import csv #Allows saving results to a .csv file

import re #Used to validate user inputs via regular expressions

from datetime import datetime #Used to log what time the quiz was completed

from quiz_questions import load_questions #Gets the quiz questions from quiz_questions.py

questions = load_questions()

class PhishingQuiz(tk.Tk):

    def __init__(self, questions):
        super().__init__()

        #Configures the quiz window
        self.geometry("1920x1080")
        self.title("Buckinghamshire Counil - Phishing 101")
        self.config(bg="#F5F5F5")

        #Initialises the variables
        self.username = tk.StringVar()
        self.questions = questions
        self.current_question = 0
        self.results = tk.IntVar(value=0)
        self.var_results = []

        self.quiz_header = tk.Label(self, text="Buckinghamshire Council - Phishing 101", font=("Cabin", 64), bg="#2C2D84", fg="white")
        self.quiz_header.pack(fill="x")

        self.help_btn = tk.Button(self, command=self.help_messagebox, text="ℹ️", font=("Cabin", 30), anchor="center", justify="center", height=1, width=4)
        self.help_btn.pack(anchor="nw")

        self.username_label = tk.Label(self, text="Please enter your name", font=("Cabin", 30), bg="#F5F5F5", anchor="n", height=2, width=20, padx=10, pady=10)
        self.username_field = tk.Entry(self, textvariable=self.username, font=("Cabin", 20), bg="white")
        self.enter_button = tk.Button(self, command=self.username_validation, text="Enter", font=("Cabin", 20), bg="#F5F5F5", anchor="n", padx=2, pady= 2)
        self.username_entry()

        self.submit_button = tk.Button(text="Submit", command=self.record_data, font=("Cabin", 20))

    def username_entry(self):
        self.username_label.pack()
        self.username_field.pack(pady=10)
        self.enter_button.pack()

    def username_validation(self):

        self.complete_username = self.username.get()

        if not re.search (r"[A-Z]", self.complete_username):
            messagebox.showerror("Username Error", "Name must contain a capital letter")
            return "Name should contain a capital"

        if re.search(r"\d", self.complete_username):
            messagebox.showerror("Username Error", "Name should not contain numbers")
            return "Name should not contain numbers"
        
        if not re.fullmatch(r"[a-zA-Z-\s]+", self.complete_username):
            messagebox.showerror("Username Error", "Name should only contain letters, hyphens or spaces")
            return "Name should only contain letters"
        
        self.enter_button.config(state="disabled")
        self.username_field.config(state="disabled")
        self.generate_questions()


    def help_messagebox(self):
        messagebox.showinfo("Help", "To begin the quiz, please type your name in to the box and select the enter button. " \
        "To finish the quiz select an answer in each of the multiple choice questions, then click the submit button.")

    def record_data(self):


        name = self.complete_username.strip()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        answers = []
        for var in self.var_results:
            answers.append(var.get())
        
        empty_question = -1
        if answers.count(empty_question):
            messagebox.showerror("Quiz Error", "All questions must be answered to submit")
            return "All questions must be answered to submit"

        else:
            with open("results.csv", "a", newline="") as results_file:
                writer = csv.writer(results_file)
                writer.writerow([name, answers, current_time])
            messagebox.showinfo("Quiz Complete", "Thank you for participating in this quiz, your answers have been submitted")
            self.destroy()

    def generate_questions(self):
        
        qnumber = 1

        for question in self.questions:
            display_question = tk.Label (self, text=question["questions"], font=("Cabin", 16))
            display_question.pack(anchor="center", padx=40, pady=(20, 5))

            results = tk.IntVar(value=-1)
            self.var_results.append(results)

            option_value = 0
            for option in question["options"]:
                answer_radiobtns = tk.Radiobutton(self, text=option, variable=results, value=option_value, font=("Cabin", 12))
                answer_radiobtns.pack(anchor="n", padx=20)
                option_value += 1

            qnumber += 1
        
        self.submit_button.pack(anchor="s", padx=30)
            


if __name__ == "__main__":
    app = PhishingQuiz(questions)
    app.mainloop()
