class Date:
    def __init__(self, string):
        self.string = string

    @classmethod
    def parse(cls, params):
        s = str(params.get('string'))
        s = s.split('-')
        return s

    @staticmethod
    def validator(params):
        try:
            if int(params[0]) not in range(0, 32):
                raise ValueError(print(f'{params[0]} - Неверный формат даты, нужен дд-мм-гггг'))
            elif int(params[1]) not in range(0, 13):
                raise ValueError(print(f'{params[1]} - Неверный формат даты, нужен дд-мм-гггг'))
            elif int(params[2]) not in range(1969, 9999):
                raise ValueError(print(f'{params[2]} - Неверный формат даты, нужен дд-мм-гггг'))
        except ValueError:
            print('ValueError')
        except IndexError:
            print('IndexError')
        else:
            print('Всё в порядке.')


d = Date(input('Введите дату в формате дд-мм-гггг: '))
val = Date.parse(d.__dict__)
Date.validator(val)
