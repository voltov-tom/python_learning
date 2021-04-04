class Cell:
    num_cells = None


class actions(Cell):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return print(f'Клетки размером {self.num} и {other.num} вместе стали размером '
                     f'{(self.num + other.num)} ячеек, это '
                     f'{round((self.num + other.num) / self.num_cells)} целые клетки')

    def __sub__(self, other):
        if self.num - other.num > 0:
            return print(f'Клетка размером {self.num} ячеек лишилась {other.num} ячеек и теперь размером '
                         f'{self.num - other.num} ячейки, это '
                         f'{round((self.num - other.num) / self.num_cells)} целых клетки')
        elif self.num - other.num == 0:
            return print('От клетки не осталось ничего.')
        else:
            print('Клетка слишком мала для вычитания.')

    def __mul__(self, other):
        return print(f'Клетки размером {self.num} и {other.num} перемножились и получилось '
                     f'{self.num * other.num} ячеек а это размер '
                     f'{round(self.num * other.num / self.num_cells)} целых клеток.')

    def __floordiv__(self, other):
        return print(f'Клетка размером {self.num} поделила на себя ячейку размером {other.num} и получилась '
                     f'{self.num // other.num} целых клеток.')


class make_order(Cell):
    def make_order(self, cell):
        return print(('*' * self.num_cells + '\n') * (cell // self.num_cells) + (cell % self.num_cells) * '*')


Cell.num_cells = 4  # количество ячеек в клетке
a = actions(40)
b = actions(17)
a + b
a - b
a * b
a // b
mk = make_order()
mk.make_order(14)
