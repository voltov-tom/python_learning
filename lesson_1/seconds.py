import math
import time


def calculation(seconds):
    seconds = int(seconds)
    minutes = math.trunc(seconds / 60)
    remaining_seconds = seconds - minutes * 60
    hours = math.trunc(minutes / 60)
    remaining_minutes = minutes - hours * 60
    days = math.trunc(hours / 24)
    remaining_hours = hours - days * 24
    weeks = math.trunc(days / 7)
    remaining_days = days - weeks * 7
    time.sleep(1)
    print(weeks, "недель,", remaining_days, "дней,", remaining_hours, "часов,", remaining_minutes, "минут,", remaining_seconds, "секунд.")


while True:
    number = input("Введите кол-во секунд для пересчета в другие единицы: ")
    if number.isdigit():
        calculation(number)
    else:
        break
