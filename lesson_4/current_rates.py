# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
from decimal import Decimal
from urllib.request import urlopen
from xml.etree import ElementTree


def currency_rates(valute):
    try:
        r = urlopen("https://www.cbr.ru/scripts/XML_daily.asp")
        rate = ElementTree.parse(r).findtext(f'.//Valute[@ID="{valute}"]/Value')
        rate = Decimal(rate.replace(',', '.'))
        r = urlopen("https://www.cbr.ru/scripts/XML_daily.asp")
        valute_name = ElementTree.parse(r).findtext(f'.//Valute[@ID="{valute}"]/Name')
        print(f'Цена за один {valute_name} = {rate} рублей.')
    except:
        print(None)
        return None


valute_id = {'usd': 'R01235', 'eur': 'R01239'}

id = input('USD or EUR: ').lower()
currency_rates(valute_id.get(id))
