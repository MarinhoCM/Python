import unittest

from HighestInteger import HighestInteger


class TestHigherInteger(unittest.TestCase):
    def test_higher_numbers(self) -> None:
        number1 = HighestInteger([-1, 3, 5, 6, 99, 12, 2])
        number2 = HighestInteger([0, 12, 4, 87])
        number3 = HighestInteger([8])
        
        self.assertEquals(number1.find_highest_integer(), 99)
        self.assertEquals(number2.find_highest_integer(), 87)
        self.assertEquals(number3.find_highest_integer(), 8)
            
            
if __name__ == "__main__":
    unittest.main()