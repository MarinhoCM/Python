import unittest

from exec import simple_coder

class TestDecoder(unittest.TestCase):
    def test_simple_coder(self: object) -> None:
        self.assertEqual(simple_coder("test"), "][[]")
        self.assertEqual(simple_coder("TEST"), "][[]")
        self.assertNotEqual(simple_coder('TEST'), "]][[]]")
        self.assertEqual(simple_coder("outra palavra"), "[[[]][[][][]]")
        
if __name__ in "__main__":
    unittest.main()
