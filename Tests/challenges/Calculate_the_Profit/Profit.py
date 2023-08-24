class Profit:
    def __init__(self, products_dict: dict) -> None:
        self.__product_dict = products_dict
        
    @property
    def product_dict(self) -> dict:
        return self.__product_dict
    
    def calculate_profit(self) -> float:
        inventory = float(self.product_dict["inventory"])
        total_sales = (
            float(self.product_dict["sell_price"]) * (inventory)
        )
        total_cost = (
            float(self.product_dict["cost_price"]) * (inventory)
        )
        profit: float = total_sales - total_cost
        return profit
