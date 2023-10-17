import unittest

from main import count_the_digits

class TestCounter(unittest.TestCase):
    def test_count_the_digits(self: object) -> None:
        self.assertEqual(count_the_digits(1123), 4)
        self.assertNotEqual(count_the_digits(11234), 4)
        self.assertEqual(count_the_digits(0), 1)
        self.assertEqual(count_the_digits(1289396387328), 13)
        self.assertEqual(count_the_digits(121317), 6)


if __name__ in "__main__":
    unittest.main()