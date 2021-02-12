my_list = []


# вычисление суммы цифр числа
def count_sum(number, sum_digit):
    while number > 0:
        j = number % 10
        sum_digit = sum_digit + j
        number = number // 10
    return sum_digit


# вычисление суммы цифр чисел делящихся на 7
def list_count(numbers, sum_numbers=0, sum=0):
    for num in numbers:
        sum = count_sum(num, sum)
        if sum % 7 == 0:
            sum_numbers = + num
    print(sum_numbers)


# создание листа в кубе
for i in range(1, 1000, 2):
    my_list.append(i ** 3)

print(my_list)
list_count(my_list)

# не создавая новый список прибавляем к каждому элементу 17
for i in my_list:
    my_list.insert(0, i + 17)
    my_list.remove(i)

my_list.reverse()

print(my_list)
list_count(my_list)
