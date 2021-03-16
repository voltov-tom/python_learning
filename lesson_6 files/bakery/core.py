def write_log(text):
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
        f.write('{}: {}'.format(str(get_last_id()), (text + '\n')))
        print('{}: {}'.format(str(get_last_id()), text))


def get_last_id():
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        id = 1
        for i in f:
            id += 1
        return id


def read_log(start, end=get_last_id()):
    if int(start) <= get_last_id():
        log_slice = []
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().split('\n')
                log_slice.append(line)
            for i in log_slice[int(start) - 1: int(end)]:
                print(i)
    else:
        print('Нет записи с таким номером')


def read_log_all():
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())


def get_help():
    print('Чтобы добавить запись введите "w",\n'
          'Чтобы получить все значения, не вводите ничего\n'
          'Чтобы получить диапазон значений, введите id этих значений(мах 2), через пробел\n'
          'Чтобы получить значения от id до конца, введите id')


if __name__ == '__main__':
    # write_log('some str')
    # read_log_all()
    read_log(155)
    # get_help()
