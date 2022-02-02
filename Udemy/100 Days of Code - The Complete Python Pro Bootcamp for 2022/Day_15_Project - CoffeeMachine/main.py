# Tentando em  inglês aqui :D
# Penny = 0.01, Nickel = 0.05, Dime = 0.10, Quarter 0.25
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


def cheking_resources():
    """check if there are still resources returning True or False"""
    resouce = ''
    for current_resources, necessary_resources in MENU[order]["ingredients"].items():
        if resources[current_resources] < necessary_resources:
            resouce = current_resources
            break
    if len(resouce) != 0:
        print(f"Sorry there is not enough {resouce}.")
        return False
    else:
        return True


def using_resources():
    """uses the resources"""
    # Utilizando recursos
    resources["water"] -= MENU[order]["ingredients"]["water"]
    if order != "espresso":
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]


def validating_int_input(ask):
    while True:
        try:
            currency = int(input(ask))
        except ValueError:
            print("insert a valid currency")
        else:
            return currency


def ckeking_money():
    """Make sure you have enough money and pay it out, if necessary returning True or False"""
    if payment < MENU[order]["cost"]:
        print("sorry, that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${int((payment - MENU[order]['cost']) * 100) / 100} in change.")
        print(f"Here is your {order} ☕. Enjoy!")
        return True


def report():
    """Shows the remaining resources and the accumulated money"""
    for name, remaining in resources.items():
        if name != "coffee":
            print(f"{name}: {remaining}ml")
        else:
            print(f"{name}: {remaining}g")
    print(f"Money: ${money}")


# Main Program
print("user guide: type 'report' to see resources or 'off' to Turn off")
order = ''
money = 0
# TODO: 6. Keep the money received and the remaining resources and ask again what the customer wants
while order != "off":
    maked_order = False
    while not maked_order:
        change = 0
        # TODO: 1. Asking what type of coffee the customer wants
        order = str(input("What would you like? (espresso/latte/cappuccino): ")).strip().lower()
        # TODO: 2. Check that there are enough resources to make the order and carry it out
        if order == "espresso" or order == "latte" or order == "cappuccino":
            maked_order = cheking_resources()
            if maked_order:
                # TODO: 4. Ask separately how many quarters, dimes, nickles and pennies.
                quaters = validating_int_input("how many quaters? ")
                dimes = validating_int_input("how many dimes? ")
                nickles = validating_int_input("how many nickles? ")
                pennies = validating_int_input("how many pennies? ")
                # TODO: 5. Add it all up and check if you have enough money for the order
                payment = (0.25 * quaters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
                maked_order = ckeking_money()
                if maked_order:
                    money += MENU[order]["cost"]
                    using_resources()
        # TODO: 3. Be able to show the remaining resources when "report" is typed
        elif order == "report":
            if resources["coffee"] == 100:
                money = 0
            report()
        else:
            # TODO: 7. Turn off when "off" is typed
            if order == "off":
                break
