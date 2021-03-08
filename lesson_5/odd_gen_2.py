# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

max_num = (int(input('Введите максимальное число: ')))
odd_nums = (num for num in range(0, max_num + 1))
for i in odd_nums:
    print(next(odd_nums))
