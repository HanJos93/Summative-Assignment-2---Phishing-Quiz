# Buckinghamshire Council - Phishing 101

## Introduction and Proposed MVP

The Buckinghamshire Council is a large organisation with approximately 5000 employees and acts as the local authority for Buckinghamshire County. The organisation provides a vast array of service from adult’s and children’s social care to waste collection and even business licenses, permits and rates. With such a large variety of skills, knowledge and experience it is vital that everyone is on the same page when it comes to IT security, therefore I proposed a quiz that would ensure that those who take it understand the fundamentals of phishing attacks. As more systems become digitised cyber-attacks become increasingly common, understanding how the most frequent type of attack, phishing, works will serve to reduce the potential risks to the organisation. 

The quiz will ask a series of questions which tests awareness about the nature of phishing attacks, the user will need to achieve a score of at least 80% to pass. The results will be permanently stored within a .csv file along with the user’s name, the answers they chose, the score they achieved, the date they took the quiz and whether they achieved a passing score. The information stored within the .csv file can then be used to identify which users could benefit from further cyber security training. Overall, I believe this quiz will further strengthen the councils already robust cyber security measures as the weakest link in almost all potential cyber-attacks is the human element, reducing the risks here will decrease the overall risk of a successful attack and assist in heightening security standards.  

## Design

### GUI Design

To begin designing this quiz, I first considered what this quiz should look like and how users will interact with it. With this in mind, I decided on using the cloud-based design tool Figma to visualise the graphical user interface and simulate the customer journey. Below is the completed diagram.
<img width="1523" height="754" alt="Figma Board" src="https://github.com/user-attachments/assets/19dd41c4-100a-4fb1-ace1-c94f550b72ab" />
[Phishing Quiz GUI Design](https://www.figma.com/design/N2lCCsXgoQUMk3etvyxnPV/Phishing-Quiz-GUI-Design?node-id=0-1&t=H2QeXzAVHVivouVx-1)

Before building this visualisation I gathered examples of current Buckinghamshire Council employee training course and elected to use a similar layout and the exact colours used to represent the organisation. This ensures that it follows the brand guidelines as well as being recognisable to internal staff as a Buckinghamshire Council product. Designing the first frame of the quiz was the most important as it would set a design precedent that all following GUI frames, buttons and labels would need to adhere to maintain the integrity of the not only the quiz design but also the brand image. As the data this quiz generates needs to be stored permanently, it is vital that the user is required to enter the necessary information before being able to move on. Therefore, this first frame needed to be easy to understand and linear to reduce chances users become lost, as a result I decided to include only a quiz header, username entry field as well as a help button. The quiz header and help button are static elements which appear in all stages of the quiz. Once the user enters their name, they can select the enter button to confirm the name and move on to the quiz.

After designing the initial layout, the next step was to consider the style of question the quiz would ask. Again, I took references from existing training courses and found the majority of them use multiple-choice style questions to test users’ knowledge, therefore the logical choice would be to create my quiz as multiple-choice as it should be an easily recognisable format to the majority of users. Once the user has selected an answer to each question, they will be able to select a submit button to record their information and end the quiz. The overall user journey is very linear and leaves little room for confusion or misunderstanding.

### Functional and non-functional requirements

<ins>Functional</ins>

- Users can enter their name

- Help button with assistance on the process

-	Display quiz questions 

-	Display quiz options as radio buttons

-	Users are shown their score on submit

-	User information (Entered name, selected answers, score and current time) is permanently stored

<ins>Functional</ins>

-	The programme should respond to user input in <1 second

-	The user journey is as linear as possible

-	The system should be able to handle scalability 

### Technical Stack Outline

<ins>Languages</ins>

- Python

The program will be built entirely within python due to its ability to write clear modular code and utilise tkinter to create graphical user interfaces.

<ins>Libraries</ins>

- tkinter

Allows for the creation of graphical user interfaces. It is required to build the GUI and user journey outline on the Figma board.

- csv

Enables reading to and permanent storage of data through .csv files. It will be used to read the questions from a .csv file and record user information in another file.

- re

Allows user input to be validate via regular expressions. This will be used to ensure the user's name does not cause errors within the program.

- datetime

Enables recording/reading of dates and times. This will be used to log the date/time the user completed the quiz.

<ins>Tools</ins>

- Visual Studio Code

VSCode is the environment the software will be built in using the Python programming language, this is due to its ability to run and display the output of code as well as set up a continous integration pipeline with this github repository.

<ins>Storage methods</ins>

- .csv

The information the user enters will be stored in a .csv file due to their text formatting and simple design.
