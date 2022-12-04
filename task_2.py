# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]


def get_multipliers(value: int) -> list:
    """"
    составляет список простых множителей числа N
    :param value: int
    :return: list
    """

    lst = []

    for i in range(2, value + 1):

        if value % i == 0:
            count = 1

            for j in range(2, (i//2 + 1)):
                if i % j == 0:
                    count = 0
                    break

            if count == 1:
                lst.append(i)

    return lst


n = int(input('Задайте натуральное число N: '))
line = get_multipliers(n)
print(f'Список простых множителей числа {n}: {line}')
