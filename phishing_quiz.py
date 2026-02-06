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
        self.username = tk.StringVar
        self.questions = questions
        self.current_question = 0
        self.results = tk.IntVar(value=0)
        self.var_results = []

        self.quiz_header()
        self.quiz_username()

    def quiz_header(self):
        tk.Label(self, text="Buckinghamshire Council - Phishing 101", font=("Cabin", 64), bg="#2C2D84", fg="white").pack(fill="x")

    def quiz_username(self):
        tk.Label(self, text="Please enter your name", font=("Cabin", 20), bg="#F5F5F5", anchor="n", height=2, width= 20, padx=10, pady= 100).pack()
        tk.Entry(self, textvariable=self.username, font=("Cabin", 20), bg="white").pack(pady=5)
        tk.Button(self, command=self.record_data, text="Enter", font=("Cabin", 20), bg="#F5F5F5", anchor="n", padx=2, pady= 2).pack()

    def record_data(self):
        user_name = self.username.get()
        current_time = datetime.now().strftime("%H:%M:%S %D:%M:%Y")

        score = []
        for var in self.var_results:
            score.append(var.get(self))

        with open("results.csv") as results_file:
            writer = csv.writer(results_file)
            writer.writerow([user_name, score, current_time])

    def generate_questions(self):

        for question in self.questions:
            display_question = tk.Label (self, text={question["questions"]}, font=("Cabin", 20))
            display_question.pack(anchor="center", padx=40, pady=(20, 5))


if __name__ == "__main__":
    app = PhishingQuiz(questions)
    app.mainloop()
