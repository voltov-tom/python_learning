# на это задание нет мотивации)))
class Stock:
    # def __init__(self, subdivision, number):
    #     self.subdivision = subdivision
    #     self.number = number
    pass


class OfficeEquip(Stock):
    brand = 'Epson'

    @classmethod
    def to_move(cls, subdivision, number):
        n = OfficeEquip.brand, {subdivision: number}
        return n


class Printer(OfficeEquip):
    colors = 4


class Copier(OfficeEquip):
    black_and_white = True
    pass


class Scanner(OfficeEquip):
    dpi = 500
    pass


p = OfficeEquip.to_move('mrst', 4)
b = OfficeEquip.to_move('mrst', 34)
print(p)
print(b + p)
