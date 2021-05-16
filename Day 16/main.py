from CoffeeModule.menu import Menu, MenuItem
from CoffeeModule.coffee_maker import CoffeeMaker
from CoffeeModule.money_machine import MoneyMachine

money = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == 'off':
        print("Shutting down Coffee Machine")
        is_on = False
    elif order == 'report':
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if drink is not None and coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            # print(f"Name: {order.name}")
            # print(f"Cost: {order.cost}")
            # for ingredient in order.ingredients:
            #     print(f"{ingredient}: {order.ingredients[ingredient]}")