import unittest

from main import add_name

class TestDict(unittest.TestCase):
    def test_add_name(self: object) -> None:
        self.assertEqual(add_name({}, "Brutus", 300), {"Brutus": 300 })
        self.assertEqual(
            add_name({"piano": 500}, "Brutus", 400),
            {"piano": 500, "Brutus": 400}
        )
        self.assertEqual(
            add_name({"piano": 500, "stereo": 300 }, "Caligula", 440),
            {"piano": 500, "stereo": 300, "Caligula": 440 }
        )
        
        
if __name__ in "__main__":
    unittest.main()
