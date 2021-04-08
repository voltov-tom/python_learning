class ComplexNumber:
    def __init__(self, num, num_2):
        self.num = complex(num, num_2)
        print(self.num)

    def __add__(self, other):
        return print(self.num + other.num)

    def __mul__(self, other):
        return print(self.num * other.num)


x = ComplexNumber(1, 2)
y = ComplexNumber(3, 4)

x + y
x * y
