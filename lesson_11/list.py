class ListOfNumbers:
    @classmethod
    def add_number(cls):
        array = []
        while True:
            number = input('Введите число: ')
            if number.isdigit():
                array.append(number)
                print(array)
            elif number == 'stop':
                break
            else:
                print('Введите только число.')
        print(f'Список: {array}')


ListOfNumbers.add_number()
