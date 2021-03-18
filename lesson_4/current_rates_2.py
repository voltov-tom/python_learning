# Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?
from decimal import Decimal
from urllib.request import urlopen
from xml.etree import ElementTree


def currency_rates(valute_id):
    valute_id = valute_id.lower()
    valutes = {'usd': 'R01235', 'eur': 'R01239'}
    valute = valutes.get(valute_id)
    try:
        r = urlopen("https://www.cbr.ru/scripts/XML_daily.asp")
        rate = ElementTree.parse(r).findtext(f'.//Valute[@ID="{valute}"]/Value')
        rate = Decimal(rate.replace(',', '.'))
        r = urlopen("https://www.cbr.ru/scripts/XML_daily.asp")
        valute_name = ElementTree.parse(r).findtext(f'.//Valute[@ID="{valute}"]/Name')
        r = urlopen("https://www.cbr.ru/scripts/XML_daily.asp")
        date_today = ElementTree.parse(r).getroot().get('Date')
        print(f'По состоянию на {date_today}, цена за один {valute_name} = {rate} рублей.')
    except:
        print(None)
        return None
