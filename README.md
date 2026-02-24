# Buckinghamshire Council - Phishing 101

## User Documentation

This quiz has been developed using the Python programming language, please ensure you have Python installed before proceeding. You can install Python here:  
[Python - Download](https://www.python.org/downloads/)  

Visual Studio Code was used to build the quiz and I recommend installing it to ensure the quiz works as intended. You can install VSCode here:  
[Visual Studio Code - download](https://code.visualstudio.com/Download)
   
Once installed or if you already have it, download the GitHub repository by clicking code and choosing 'Download ZIP' 
<img width="1381" height="178" alt="image" src="https://github.com/user-attachments/assets/de070468-014d-4f57-91c5-06c95fb626a1" />
**Figure 1:** _Screenshot of the GitHub repository code button_
   
After downloading the repository, locate the downloaded .zip file, right click it and select extract all.

![Extract](https://github.com/user-attachments/assets/97954ba1-d998-4c9e-98d5-7e7bb2f3cd7b)
**Figure 2:** _Animated GIF demonstrating .zip file extraction_

Open the extracted file and double click phishing_quiz.py, code will now open via Visual Studio Code. From here you can click the 'Play' button in the top right to start the quiz.

To begin, type your username and select the enter button. You will now be met with multiple choice questions of which you can answer in any order, make a selection for each question to submit and end the quiz.
![Open Quiz](https://github.com/user-attachments/assets/b58dc5c4-ec4e-4ce8-bb82-09679276c3c0)
**Figure 3:** _Animated GIF demonstrating how to open the quiz and how to start_

Once you submit your answers you can view the results in the file named 'results.csv'

## Introduction and Proposed MVP

The Buckinghamshire Council is a large organisation with approximately 5000 employees and acts as the local authority for Buckinghamshire County. The organisation provides a vast array of service from adult’s and children’s social care to waste collection and even business licenses, permits and rates. With such a large variety of skills, knowledge and experience it is vital that everyone is on the same page when it comes to IT security, therefore I proposed a quiz that would ensure that those who take it understand the fundamentals of phishing attacks. As more systems become digitised cyber-attacks become increasingly common, understanding how the most frequent type of attack, phishing, works will serve to reduce the potential risks to the organisation. 

The quiz will ask a series of questions which tests awareness about the nature of phishing attacks, the user will need to achieve a score of at least 80% to pass. The results will be permanently stored within a .csv file along with the user’s name, the answers they chose, the score they achieved, the date they took the quiz and whether they achieved a passing score. The information stored within the .csv file can then be used to identify which users could benefit from further cyber security training. Overall, I believe this quiz will further strengthen the councils already robust cyber security measures as the weakest link in almost all potential cyber-attacks is the human element, reducing the risks here will decrease the overall risk of a successful attack and assist in heightening security standards.  

## Design

### GUI Design

To begin designing this quiz, I first considered what this quiz should look like and how users will interact with it. With this in mind, I decided on using the cloud-based design tool Figma to visualise the graphical user interface and simulate the customer journey. Below is the completed diagram.
<img width="1523" height="754" alt="Figma Board" src="https://github.com/user-attachments/assets/19dd41c4-100a-4fb1-ace1-c94f550b72ab" />
**Figure 4:** _[Wireframe](https://www.figma.com/design/N2lCCsXgoQUMk3etvyxnPV/Phishing-Quiz-GUI-Design?node-id=0-1&t=H2QeXzAVHVivouVx-1) developed on Figma_

Before building this visualisation I gathered examples of current Buckinghamshire Council employee training course and elected to use a similar layout and the exact colours used to represent the organisation. This ensures that it follows the brand guidelines as well as being recognisable to internal staff as a Buckinghamshire Council product. Designing the first frame of the quiz was the most important as it would set a design precedent that all following GUI frames, buttons and labels would need to adhere to maintain the integrity of the not only the quiz design but also the brand image. As the data this quiz generates needs to be stored permanently, it is vital that the user is required to enter the necessary information before being able to move on. Therefore, this first frame needed to be easy to understand and linear to reduce chances users become lost, as a result I decided to include only a quiz header, username entry field as well as a help button. The quiz header and help button are static elements which appear in all stages of the quiz. Once the user enters their name, they can select the enter button to confirm the name and move on to the quiz.

After designing the initial layout, the next step was to consider the style of question the quiz would ask. Again, I took references from existing training courses and found the majority of them use multiple-choice style questions to test users’ knowledge, therefore the logical choice would be to create my quiz as multiple-choice as it should be an easily recognisable format to the majority of users. Once the user has selected an answer to each question, they will be able to select a submit button to record their information and end the quiz. The overall user journey is very linear and leaves little room for confusion or misunderstanding.

### Functional and non-functional requirements

<img width="600" height="350" alt="image" src="https://github.com/user-attachments/assets/2ac898d2-101f-47ec-a18e-a4e78ad78d7e" />

**Figure 5:** _Functional and Non-functional requirements table_

### Technical Stack Outline

<ins>Languages</ins>

- Python

The program will be built entirely within python due to its ability to write clear modular code and utilise tkinter to create graphical user interfaces.

<ins>Libraries</ins>

- tkinter

Allows for the creation of graphical user interfaces. It is required to build the GUI and user journey outline on the Figma board.

- messagebox

Allows message boxes to be displayed via the code. This will be used for the help menu, displaying errors and displaying the results to the user.

- csv

Enables reading to and permanent storage of data through .csv files. It will be used to read the questions from a .csv file and record user information in another file.

- re

Allows user input to be validate via regular expressions. This will be used to ensure the user's name does not cause errors within the program.

- datetime

Enables recording/reading of dates and times. This will be used to log the date/time the user completed the quiz.

<ins>Tools</ins>

- Visual Studio Code

VSCode is the environment the software will be built in using the Python programming language, this is due to its ability to run and display the output of code as well as set up a continuous integration pipeline with this GitHub repository.

<ins>Storage methods</ins>

- .csv

The information the user enters will be stored in a .csv file due to their text formatting and simple design.

### Class Diagram

<img width="1278" height="1297" alt="image" src="https://github.com/user-attachments/assets/d90ba002-1b93-41d2-9130-834d5a68a2ec" />

**Figure 6:** _Class diagram developed on draw.io_

## Development

Before developing the quiz, the questions needed to be determined. To do this I used information from the Buckinghamshire Council's own phishing guidance and created questions which included answers relevant and specific to the organisation. These questions are stored in quiz_questions.csv.

With the questions in a .csv file, these needed to be converted to a format easily to read from and manipulate. To achieve this, I created a module which converts the data from the .csv into a Python dictionary that the main file could call from using the following code.
```python
import csv

def load_questions(filepath="quiz_questions.csv"):
    questions = []

    with open (filepath) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            question = {
                "questions": row["questions"],
                "options": [
                    row["choice1"],
                    row["choice2"],
                    row["choice3"],
                    row["choice4"],
                ],
                "answer": int(row["answer"]) - 1
            }
            questions.append(question)

    return questions
```
The reader variable ensures the script is only reading the csv and not making and changes to it. The dictionary (questions) creates a key for each row in the questions column, and each question is assigned the value of the options in the same row, this results in a dictionary with 5 distinct questions ready for the main file to call upon. With this module complete, the quiz can now be developed.

The primary file is called phishing_quiz.py and contains the rest of the code necessary for the quiz to function. To begin I imported the quiz_questions module and defined a variable which is assigned the function which creates the questions dictionary.
```python
from quiz_questions import load_questions #Gets the quiz questions from quiz_questions.py

questions = load_questions()
```
All of the remaining code sits within a super class, PhishingQuiz, this allows me to access methods in the super class in all sub classes and definitions. The class contains the questions variable, allowing it to be called wherever needed.
```python
class PhishingQuiz(tk.Tk):

    def __init__(self, questions):
        super().__init__()
```
A set of variables are defined within the super class and initialised for use within definitions that will be created later.
```python
self.username = tk.StringVar()
self.questions = questions
self.current_question = 0
self.results = tk.IntVar(value=0)
self.var_results = []
```
The following code block creates and places the help button on the GUI. The button is locked to the top left and is a persistent element which will not move or change.
```python
self.help_button = tk.Button(self, command=self.help_messagebox, text="ℹ️", font=("Cabin", 30), anchor="center", justify="center", height=1, width=4)
self.help_button.pack(anchor="nw")
```
When the help button is selected, the command it runs is defined below. In order to preserve the layout of the quiz the help menu was created as a message box allowing it to be accessed at any point without disrupting the flow of the user experience.
```python
def help_messagebox(self):
messagebox.showinfo("Help", "To begin the quiz, please type your name in to the box and select the enter button. " \
"To finish the quiz select an answer in each of the multiple choice questions, then click the submit button.")
```
Once the user types a name in to the name entry field and selects the enter button, it runs a function which validates the username and confirms if it is not empty, between 3 to 30 characters, doesn't contain numbers or special characters.
```python
    def username_validation(self):

        self.complete_username = self.username.get().title().strip() 

        try:
            if bool(self.complete_username) == False:
                messagebox.showerror("Username Error", "Name can not be empty")
                raise ValueError ("Name can not be empty")
            
            elif len(self.complete_username) <= 2:
                messagebox.showerror("Username Error", "Name can not be 3 or more characters")
                raise ValueError ("Name can not be 3 or more characters")

            elif len(self.complete_username) >= 30:
                messagebox.showerror("Username Error", "Name can not be over 30 characters")
                raise ValueError ("Name can not be over 30 characters")

            elif re.search(r"\d", self.complete_username):
                messagebox.showerror("Username Error", "Name can not not contain numbers")
                raise ValueError ("Name should not contain numbers")
            
            elif not re.fullmatch(r"[a-zA-Z-\s]+", self.complete_username):
                messagebox.showerror("Username Error", "Name can only contain letters, hyphens or spaces")
                raise ValueError ("Name should only contain letters, hyphens or spaces")
```
If the username passes the previous validations, it then generates the questions from the csv file. First the questions themselves are generated via tkinter labels.
```python
for question in self.questions:
            display_question = tk.Label (self, text=question["questions"], font=("Cabin", 16))
            display_question.pack(anchor="center", padx=40, pady=(20, 5))
```
Once the question labels are generated, the multiple-choice buttons are created based on the questions dictionary.
```python
            option_value = 0
            for option in question["options"]:
                answer_radiobtns = tk.Radiobutton(self, text=option, variable=results, value=option_value, font=("Cabin", 12))
                answer_radiobtns.pack(anchor="n", padx=20)
                option_value += 1
```
Finally, once the user clicks the submit button to submit their answers, the results variable tracks which answers they chose and adds +1 to the score for each correct question.
```python
answers = []
        for var in self.var_results:
            answers.append(var.get())

        score = 0
        if answers[0] == 2:
            score = score + 1
        if answers[1] == 3:
            score = score + 1
        if answers[2] == 1:
            score = score + 1
        if answers[3] == 1:
            score = score + 1
        if answers[4] == 3:
            score = score + 1
        else:
            score = score + 0
        score = str(score)
```
Before the information is recorded, the answers submitted are first checked for any blanks. If a question is left unchecked it results in a -1 making it easy to identify.
```python
empty_question = -1
        if answers.count(empty_question):
            messagebox.showerror("Quiz Error", "All questions must be answered to submit")
            return "All questions must be answered to submit"
```
If no questions are left empty, the users information is written to a file named results.csv, displays a message box with the users results and closes the quiz.
```python
with open("results.csv", "a", newline="") as results_file:
  writer = csv.writer(results_file)
  writer.writerow([name, answers, score, current_time])
messagebox.showinfo("Quiz Complete","You scored " + score + "/5\n" + "\n" 
                    "Thank you for participating in this quiz, your answers have been submitted.")
self.destroy()
```

## Testing

To test the code and functions of the script, I elected to use Pythons inbuilt unit testing framework. This is to reduce the amount libraries the need to be installed and imported into the code. I used a combination of automated and manual tests to ensure that any errors are caught before they have the opportunity to cause issues. To begin I performed a basic smoke test and uploaded to GitHub to confirm the core functionality was working as intended and the CI pipeline.
<img width="1500" height="578" alt="image" src="https://github.com/user-attachments/assets/dfc4955e-cb31-4d11-bf8a-887e6a7ce684" />
**Figure 7:** _Smoke test completed on VScode and confirmation of continous integration pipeline_

Once the smoke tests were confirmed to be passing, I began writing unit tests for the username entry field. This was to ensure that the name users’ input could not be unexpected or result in an error.
<img width="671" height="799" alt="image" src="https://github.com/user-attachments/assets/32531a69-073e-4b2c-a953-26b8c3703cb0" />
**Figure 8:** _Automated unit uests using example user inputs, built on VScode_

As we can see from the passing tests, names cannot have numbers or special characters but most importantly it does allow for names with hyphens separating them.

Before incorporating the quiz_questions() function into the main code, it was important that I validate whether the function generates an output to do this with a unit test I wrote the following test case.
<img width="617" height="598" alt="image" src="https://github.com/user-attachments/assets/74ffd76c-a57e-4faa-9676-66f86b87dece" />
**Figure 9:** _Automated unit test confirming presence of data within the quiz_questions function, built on VScode_

Below are the results of the manual testing performed

<img width="575" height="816" alt="image" src="https://github.com/user-attachments/assets/73528337-9e15-48ed-be20-14481ac2998d" />

<img width="566" height="819" alt="image" src="https://github.com/user-attachments/assets/c5a67662-1d8b-4373-8ee2-822b7e359497" />

**Figure 10:** _Manual testing_

## Technical Documentation

All libraries used in development are included in all recent Python installtions. 

**1.** This program was developed on Python 3.13 and has been tested on later versions, please ensure you have Python 3.13 or higher. You can run the following commands in your terminal to check the version
```
python -v
```
**2.** Clone this repo 


### Cloning the repo

## Evaluation

Overall, I believe this project has been successful in achieving the goals it has set out to, assisting in bolstering knowledge on phishing cyber-attacks, providing software in line with brand guidelines and the necessary functional and non-functional requirements. However, it has also provided enumerable ideas and insights into how my software can be improved in future endeavours.  

Through the design and development of this quiz I have learnt much about the types of considerations that need to be made when building software for an organisation such as brand consistency and intuitive user journeys. While I believe the user experience on the quiz is intuitive and user-friendly, the steps required to access the quiz such as installing Python and Visual Studio Code risk turning user’s aways as they may perceive these steps as cumbersome. I need to know more about converting my code into easily accessible executables to reduce the risk of losing users before they have the opportunity to access the software.  

Although the code achieves the bulk of the requirements, upon reflection the scalability of the application, despite it supporting the addition of new questions, does suffer due to how they are displayed in the application window. Currently, the questions are all listed simultaneously which means adding more risks having them hidden off screen thus making the quiz impossible. To remedy this in future projects, I will learn from tkinter’s documentation and develop code to display one question at a time, which will enhance scalability.

