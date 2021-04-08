class Division:
    @classmethod
    def division(cls, a, b):
        if b != 0:
            c = round(a / b, 2)
            return print(f'{a} / {b} = {c}')
        else:
            print('Деление на ноль.')


Division.division(float(input('a = ')), float(input('b = ')))
