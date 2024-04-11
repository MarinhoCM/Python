from helpers.Player import Player

p1 = Player("David Jones", 25, 175, 75)

if __name__ == "__main__":
    print(p1.get_age()) # -> "David Jones is age 25"
    print(p1.get_height()) # -> "David Jones is 175cm"
    print(p1.get_weight()) # -> "David Jones weighs 75kg"
