from Data import DATA

class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: $ {self.profit}")

    def make_payment(self, user_prompt):
        user_input_dollar = int(input("Please insert dollars:"))
        user_input_halfdollar = int(input("Please insert half-dollars:"))
        user_input_quarter = int(input("Please insert quarters:"))
        user_input_dimes = int(input("Please insert dimes:"))

        total_amount = (user_input_dollar * 1) + (user_input_halfdollar * 0.50) + (user_input_quarter * 0.25) + (user_input_dimes * 0.10) 

        if DATA[user_prompt]["cost"] == total_amount:
            self.profit = self.profit + total_amount
            print("---AMOUNT PAID---")
            return True
        elif DATA[user_prompt]["cost"] < total_amount:
            change = total_amount - DATA[user_prompt]["cost"]
            self.profit = self.profit + total_amount - change
            print("---AMOUNT PAID---")
            print(f"---PLEASE COLLECT CHANGE: $ {round(change,2)}")
            return True
        else:
            print(f"---SORRY NOT ENOUGH MONEY. AMOUNT REFUNDED: $ {total_amount}")
            return False
