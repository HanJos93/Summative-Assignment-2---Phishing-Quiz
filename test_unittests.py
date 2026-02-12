import unittest #Testing framework 
import re #For validating user input
from quiz_questions import load_questions #Converts questions in csv to a dictionary

class SmokeTest(unittest.TestCase):

    def test_smoke_test(self):
        self.assertTrue(2>1)

class UsernameTest(unittest.TestCase):

    def test_complete_username(self):
        username = "  joshua kneba  "
        username = str(username).strip().title()
        self.assertTrue((username),"Joshua Kneba")

    def test_username_numbers(self):
        username = "123Joshua Kneba"
        username = not re.search(r"\d", username)
        self.assertFalse(username)

class QuizQuestionsTest(unittest.TestCase):
    
    def test_load_questions(self):
        questions = load_questions()
        self.assertIsNotNone(questions)



if __name__ == "__main__":
    unittest.main()