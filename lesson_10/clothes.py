class Clothes:
    def __init__(self, h, v):
        self.h = 2 * h + 0.3
        self.v = v / 6.5 + 0.5

    def __str__(self):
        return f"Всего ткани: {round(self.h + self.v, 2)}"


C = Clothes(3, 10)
print(C)
