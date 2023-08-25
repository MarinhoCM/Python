import unittest

from main import Football

class TestPoints(unittest.TestCase):
    def test_football_points(self):
        points1 = Football(3, 4, 2)
        points2 = Football(5, 0, 2)
        points3 = Football(0, 0, 1)
        
        self.assertEquals(points1.football_points(), 13)
        self.assertEquals(points2.football_points(), 15)
        self.assertEquals(points3.football_points(), 0)

if __name__ == "__main__":
    unittest.main()
