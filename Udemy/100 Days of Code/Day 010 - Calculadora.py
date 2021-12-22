# Note na linha 64, temos um exemplo de função recursiva (ela chama ela mesma para reiniciar.)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")

operações = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculadora():
    num1 = float(input("Qual o primeiro número? "))
    for key in operações:
        print(key)
    repetir = True
    while repetir:
        operação = input("Escolha uma operação: ")[0]
        num2 = float(input("Qual o proximo número? "))
        função = operações[operação]
        resposta = função(num1, num2)

        print(f"{num1} {operação} {num2} = {resposta:.2f}")

        print(f"Deseja continuar operando com {resposta}?\n"
              "[S] = Continuar\n"
              "[N] = Reiniciar a calculadora\n"
              "[X] = Encerrar a calculadora")
        repetir = input(f"Qual a sua resposta? ").upper()[0]
        if repetir == "S":
            num1 = resposta
        elif repetir == "N":
            calculadora()
        else:
            break
        repetir = False



calculadora()
