# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# src_sorted = [i for i in src if i > ]
# print(src_sorted)

src_sorted = [i for i in src[1:] if i > src[(src.index(i) - 1)]]
print(src_sorted)
