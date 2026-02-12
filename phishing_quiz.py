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

        #Builds and displays the quiz header
        self.quiz_header = tk.Label(self, text="Buckinghamshire Council - Phishing 101", font=("Cabin", 64), bg="#2C2D84", fg="white")
        self.quiz_header.pack(fill="x")

        #Builds and displays the help button
        self.help_btn = tk.Button(self, command=self.help_messagebox, text="ℹ️", font=("Cabin", 30), anchor="center", justify="center", height=1, width=4)
        self.help_btn.pack(anchor="nw")

        #Builds and displays the username entry label and input fields
        self.username_label = tk.Label(self, text="Please enter your name", font=("Cabin", 30), bg="#F5F5F5", anchor="n", height=2, width=20, padx=10, pady=10)
        self.username_field = tk.Entry(self, textvariable=self.username, font=("Cabin", 20), bg="white")
        self.enter_button = tk.Button(self, command=self.username_validation, text="Enter", font=("Cabin", 20), bg="#F5F5F5", anchor="n", padx=2, pady= 2)
        self.username_entry()

        #Builds the submit button
        self.submit_button = tk.Button(text="Submit", command=self.record_data, font=("Cabin", 20))

    #Packs the labels ready to display once the function is called
    def username_entry(self):
        self.username_label.pack()
        self.username_field.pack(pady=10)
        self.enter_button.pack()

    #Validates the username after the user selects the enter button
    def username_validation(self):

        self.complete_username = self.username.get().title().strip() #Retrieves the username, removes white spaces and capitalises each word

        #Checks if username is empty
        if bool(self.complete_username) == False:
            messagebox.showerror("Username Error", "Name can not be empty")
            return "Name can not be empty"
        
        #Checks if username contains 3 or more characters
        if len(self.complete_username) <= 2:
            messagebox.showerror("Username Error", "Name can not be 3 or more characters")
            return "Name can not be 3 or more characters"

        #Checks if username contains over 30 characters
        if len(self.complete_username) >= 30:
            messagebox.showerror("Username Error", "Name can not be over 30 characters")
            return "Name can not be over 30 characters"

        #Checks if username contains numbers
        if re.search(r"\d", self.complete_username):
            messagebox.showerror("Username Error", "Name can not not contain numbers")
            return "Name should not contain numbers"
        
        #Checks if username contains special characters aside from hyphens or spaces
        if not re.fullmatch(r"[a-zA-Z-\s]+", self.complete_username):
            messagebox.showerror("Username Error", "Name can only contain letters, hyphens or spaces")
            return "Name should only contain letters, hyphens or spaces"
        
        #Disables the username fields and displays the questions
        self.username_label.destroy()
        self.enter_button.destroy()
        self.username_field.destroy()
        self.generate_questions()

    #Defines the help window displayed when the help button is clicked
    def help_messagebox(self):
        messagebox.showinfo("Help", "To begin the quiz, please type your name in to the box and select the enter button. " \
        "To finish the quiz select an answer in each of the multiple choice questions, then click the submit button.")

    #Defines the quiz submission process
    def record_data(self):

        name = self.complete_username.strip().title() #Gets the username and removes white spaces and capitalised each word
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Records current date and time

        #Records users choices for each question
        answers = []
        for var in self.var_results:
            answers.append(var.get())
        
        #Checks that no questions are left blank
        empty_question = -1
        if answers.count(empty_question):
            messagebox.showerror("Quiz Error", "All questions must be answered to submit")
            return "All questions must be answered to submit"

        #If no questions are blank, record the results in a csv file then end the quiz
        else:
            with open("results.csv", "a", newline="") as results_file:
                writer = csv.writer(results_file)
                writer.writerow([name, answers, current_time])
            messagebox.showinfo("Quiz Complete", "Thank you for participating in this quiz, your answers have been submitted")
            self.destroy()

    #Defines the generation of the quiz questions
    def generate_questions(self):
        
        qnumber = 1

        #For each row in quiz_questions.csv create a question label
        for question in self.questions:
            display_question = tk.Label (self, text=question["questions"], font=("Cabin", 16))
            display_question.pack(anchor="center", padx=40, pady=(20, 5))

            results = tk.IntVar(value=-1)
            self.var_results.append(results)

            #For each answer create a radio button under their respective question
            option_value = 0
            for option in question["options"]:
                answer_radiobtns = tk.Radiobutton(self, text=option, variable=results, value=option_value, font=("Cabin", 12))
                answer_radiobtns.pack(anchor="n", padx=20)
                option_value += 1

            qnumber += 1
        
        #Displays the submit button 
        self.submit_button.pack(anchor="s", padx=30)
            


if __name__ == "__main__":
    app = PhishingQuiz(questions)
    app.mainloop()
