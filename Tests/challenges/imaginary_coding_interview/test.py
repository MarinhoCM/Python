import unittest

from main import Interview

class TestInterview(unittest.TestCase):
    def test_interview_function(self) -> None:
        interview1 = Interview([5, 5, 10, 10, 15, 15, 20, 20], 120)
        interview2 = Interview([2, 3, 8, 6, 5, 12, 10, 18], 64)
        interview3 = Interview([5, 5, 10, 10, 25, 15, 20, 20], 120)
        interview4 = Interview([5, 5, 10, 10, 15, 15, 20], 120)
        interview5 = Interview([5, 5, 10, 10, 15, 15, 20, 20], 130)
        
        self.assertEquals(interview1.interview(), "qualified")
        self.assertEquals(interview2.interview(), "qualified")
        self.assertEquals(interview3.interview(), "disqualified") 
        self.assertEquals(interview4.interview(), "disqualified")
        self.assertEquals(interview5.interview(), "disqualified") 

if __name__ == "__main__":
    unittest.main()
