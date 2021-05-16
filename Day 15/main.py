MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report_status(resource_remaining, money_drawer):
    print(f"Water: {resource_remaining['water']}ml")
    print(f"Milk: {resource_remaining['milk']}ml")
    print(f"Coffee: {resource_remaining['coffee']}g")
    print(f"Money: ${money_drawer}")
    return


def check_resource(choice, resource_left):
    for resource in resource_left:
        if MENU[choice]['ingredients'][resource] > resource_left[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True

def take_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


money = 0
developer = False
while not developer:
    flavor = input("What would you like? (espresso/latte/cappuccino): ")
    if flavor == 'report':
        report_status(resources, money)
    elif flavor == 'off':
        developer = True
    else:
        #print(f"Cash inserted: {cash}")
        if check_resource(flavor, resources):
            cash = take_coins()
            if cash >= MENU[flavor]['cost']:
                cash -= MENU[flavor]['cost']
                money += MENU[flavor]['cost']
                for resource in resources:
                    resources[resource] -= MENU[flavor]['ingredients'][resource]
                if cash > 0:
                    print(f"Here is ${round(cash, 2)} in change.")
                print(f"Here is your {flavor} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")


# TODO: 1. Print Report
# TODO: 2. Check Sufficient Resources
# TODO: 3. Process Coins
# TODO: 4. Check Transaction Successfull
# TODO: 5. Make Coffee