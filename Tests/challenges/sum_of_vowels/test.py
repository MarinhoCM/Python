import unittest

from exec import sum_of_vowels

class TestSum(unittest.TestCase):
    def test_sum_of_vowels(self) -> None:
        self.assertEqual(sum_of_vowels("Let\'s test this function."), 8)
        self.assertEqual(sum_of_vowels("Do I get the correct output?"), 10)
        self.assertEqual(sum_of_vowels("I love edabit!"), 12)
    
if __name__ in "__main__":
    unittest.main()