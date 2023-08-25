import unittest

from main import Player

class TestChallenge(unittest.TestCase):
    def test_player_class(self):
        player1 = Player('Patrick Mahomes', 24, 188, 104)
        player2 = Player('Jimmy Garoppolo', 28, 188, 102)
        player3 = Player('Julio Jones', 31, 191, 100)
        
        self.assertEqual(player1.get_age(), 'Patrick Mahomes is age 24')
        self.assertEqual(player1.get_height(), 'Patrick Mahomes is 188cm')
        self.assertEqual(
            player1.get_weight(), 'Patrick Mahomes weighs 104kg'
        )
        
        self.assertEqual(player2.get_age(), 'Jimmy Garoppolo is age 28')
        self.assertEqual(player2.get_height(), 'Jimmy Garoppolo is 188cm')
        self.assertEqual(
            player2.get_weight(), 'Jimmy Garoppolo weighs 102kg'
        )

        self.assertEqual(player3.get_age(), 'Julio Jones is age 31')
        self.assertEqual(player3.get_height(), 'Julio Jones is 191cm')
        self.assertEqual(
            player3.get_weight(), 'Julio Jones weighs 100kg'
        )

if __name__ == "__main__":
    unittest.main()