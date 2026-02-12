import unittest #Testing framework 
from quiz_questions import load_questions

class SmokeTest(unittest.TestCase):

    def smoke_test(self):
        self.assertTrue(1)