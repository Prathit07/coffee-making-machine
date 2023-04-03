from Data import DATA, AVAILABLE_DRINKS
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True
while coffee_machine_on != False:
    user_prompt = input("---WELCOME TO PS COFFEE MACHINE---\nWhat would you like? (espresso/latte/cappuccino):")
    #Convert the input to lowercase
    user_prompt = user_prompt.lower()
    if user_prompt == "off":
        coffee_machine_on = False
    elif user_prompt == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_prompt in AVAILABLE_DRINKS:
        if coffee_maker.is_resource_sufficient(user_prompt) and money_machine.make_payment(user_prompt):
            coffee_maker.make_coffee(user_prompt)
    else:
        print("---PLEASE ENTER A CORRECT DRINK---")
    
