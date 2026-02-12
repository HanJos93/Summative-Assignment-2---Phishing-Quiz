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

        quiz_header = tk.Label(self, text="Buckinghamshire Council - Phishing 101", font=("Cabin", 64), bg="#2C2D84", fg="white")
        quiz_header.pack(fill="x")

        self.username_entry()
    
    def username_entry(self):
        tk.Label(self, text="Please enter your name", font=("Cabin", 20), bg="#F5F5F5", anchor="n", height=2, width= 20, padx=10, pady= 100).pack()
        tk.Entry(self, textvariable=self.username, font=("Cabin", 20), bg="white").pack(pady=5)
        tk.Button(self, command=self.generate_questions, text="Enter", font=("Cabin", 20), bg="#F5F5F5", anchor="n", padx=2, pady= 2).pack()

    def record_data(self):
        user_name = self.username.get().strip()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        score = []
        for var in self.var_results:
            score.append(var.get())

        with open("results.csv", "a", newline="") as results_file:
            writer = csv.writer(results_file)
            writer.writerow([user_name, score, current_time])

    def generate_questions(self):
        
        qnumber = 1

        for question in self.questions:
            display_question = tk.Label (self, text=question["questions"], font=("Cabin", 20))
            display_question.pack(anchor="center", padx=40, pady=(20, 5))

            results = tk.IntVar(value=-1)
            self.var_results.append(results)

            option_value = 0
            for option in question["options"]:
                answer_radiobtns = tk.Radiobutton(self, text=option, value=option_value, font=("Cabin", 16))
                answer_radiobtns.pack(anchor="n", padx=20)
                option_value += 1

            qnumber += 1
        
        submit_button = tk.Button(text="Submit", command=self.record_data, font=("Cabin", 20))
        submit_button.pack(anchor="s", padx=30)
            


if __name__ == "__main__":
    app = PhishingQuiz(questions)
    app.mainloop()
