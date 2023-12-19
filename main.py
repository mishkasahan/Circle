import math


class Circle:
    pi = math.pi

    def __init__(self, name: str, radius: float):
        self.name = name
        self.radius = radius

    def plostcha(self):
        return self.pi * self.radius * self.radius

    def dovkola(self):
        return 2 * self.pi * self.radius


kolo1 = Circle("kolo1", 5)

print(kolo1.plostcha())
print(kolo1.dovkola())
