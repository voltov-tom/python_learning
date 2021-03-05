# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#    "И": ["Иван", "Илья"], 
#    "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?

by_letters = {}


def thesaurus(names):
    for name in names:
        by_letters.setdefault(name[0].upper(), []).append(name)
    return by_letters


# workers = (input("Введите имена, через запятую: "))
workers = ('  ивасик, Андрей, иван,стас,     глеб, герасим')
words = workers.title().split()  # убираем пробелы
words = ''.join(words)
words = words.split(',')

thesaurus(words)

print(by_letters)

sort_keys = by_letters.keys()  # сортировка по ключам
sort_keys = sorted(sort_keys)
sort_dist = {}
for i in sort_keys:
    sort_dist.setdefault(i, [by_letters.get(i)])
print(sort_dist)
