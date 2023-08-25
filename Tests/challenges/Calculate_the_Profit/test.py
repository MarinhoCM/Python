import os
import sys
import json
import unittest

from main import Profit

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


with open(f"{SCRIPT_DIR}/products_info.json", 'r') as file:
    content = json.load(file)


class TestProfit(unittest.TestCase):
    def test_products_profit(self) -> None:
        profit1 = Profit(content[0])
        profit2 = Profit(content[1])
        profit3 = Profit(content[2])
        
        self.assertEquals(round(profit1.calculate_profit()), 14796)
        self.assertEquals(round(profit2.calculate_profit()), 32411)
        self.assertEquals(round(profit3.calculate_profit()), 44030)


if __name__ == "__main__":
    unittest.main()
