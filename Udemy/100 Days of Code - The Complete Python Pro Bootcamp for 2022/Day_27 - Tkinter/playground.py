def add(*num):
    print(f"A soma é {sum(num)}")


add(2, 3, 9, 8, 2, 5, 1, 1, 0, 8)


def calculate(n, **kwargs):  # **kwargs é um dicionário.
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="nissan")
print(my_car.make)
print(my_car.model)  # Usando o método get, não é retornado um ERRO e sim um None.
