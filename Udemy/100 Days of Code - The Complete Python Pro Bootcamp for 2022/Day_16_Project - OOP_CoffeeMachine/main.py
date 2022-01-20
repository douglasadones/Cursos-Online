# Documentação: https://www.udemy.com/course/100-days-of-code/learn/lecture/19914252#overview (Vídeo 150)
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# choice = str(input(f"What would you like? ({options}): ")).lower().strip()

# Criando meus objetos a partir das classes para uso no código.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
tipos = menu.get_items()
ligado = True

while ligado:
    escolha = str(input(f"What would you like? ({tipos}): ")).lower().strip()
    if escolha == "report":
        coffee_maker.report()
        money_machine.report()
    elif escolha == "off":
        ligado = False
    else:
        pedido = menu.find_drink(escolha)
        if coffee_maker.is_resource_sufficient(pedido) and money_machine.make_payment(pedido.cost):
            coffee_maker.make_coffee(pedido)
