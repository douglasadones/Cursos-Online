# Class inheritance study
class Animal:
    def __init__(self):
        self.num_eye = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()

print(nemo.swim())  # Característica prórpia
print(nemo.num_eye)  # Característica herdada da classe Animal
print(nemo.breathe())
