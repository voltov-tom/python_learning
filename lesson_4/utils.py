# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит
# Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. python utils.py EuR
from sys import argv
from current_rates_2 import currency_rates

currency_rates(argv[1])
