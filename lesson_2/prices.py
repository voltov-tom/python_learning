# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# * Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


import random

prices = []
new_price = []
penny = ''


# генерация случайных чисел с точкой в список, два знака
def random_price(quantity):
    for i in range(1, 10):
        number = (random.triangular(1, quantity))
        number = round(number, 2)
        prices.append(number)


random_price(100)

# получаем отдельно копейки <кк> и рубли, обьединяем их лист
for i in prices:
    num = int(round(i % 1, 2) * 100)
    penny = ''.join(f'{num:02} коп. ')
    rubles = int(i)
    rubles = ''.join(f'{rubles} руб.')
    new_price.append(rubles + penny)


# создаем строку из листа, с сепаратором
def string(list):
    list = ', '.join(i for i in list)
    return list


print(prices)  # список чисел
print(string(new_price))  # список цен в строчку с запятой
print(new_price)  # список цен
print(sorted(new_price))  # по возрастанию
print(new_price)  # доказательство

descending_price = list.copy(new_price)
descending_price = sorted(descending_price, reverse=True)
print(descending_price)  # сорт. по убыванию новый список

print(string(descending_price[0:5]))  # пять дорогих товаров
