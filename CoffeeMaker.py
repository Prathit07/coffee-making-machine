from Data import DATA

class CoffeeMaker:
    def __init__(self):
        self.water = 1000
        self.milk = 700
        self.coffee = 800
    
    def report(self):
        print("---RESOURCES---")
        print(f"Water: {self.water} ml\nMilk: {self.milk} ml\nCoffee: {self.coffee} g")

    def is_resource_sufficient(self, user_prompt):
        if self.water > DATA[user_prompt]["ingredients"]["water"] and self.milk > DATA[user_prompt]["ingredients"]["milk"] and self.coffee > DATA[user_prompt]["ingredients"]["coffee"]:
            print("---PROCESSING YOUR DRINK---")
            return True
        else:
            print("---INSUFFICIENT RESOURCES---")
            return False
    
    def make_coffee(self, user_prompt):
        self.water = self.water - DATA[user_prompt]["ingredients"]["water"]
        self.milk = self.milk - DATA[user_prompt]["ingredients"]["milk"]
        self.coffee = self.coffee - DATA[user_prompt]["ingredients"]["coffee"]
        return print(f"---ENJOY YOUR {(user_prompt).upper()} !---\n")
        




