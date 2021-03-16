# Написать генератор нечётных чисел от 1 до n (включительно)
def gen_nums(max_num):
    for num in range(0, max_num + 1):
        yield num


gen = gen_nums(int(input('Введите максимальное число: ')))
for i in gen:
    print(next(gen))
