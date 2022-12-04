from random import randint


# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
#     k=2 => 2*x*2 + 4*x + 5 = 0
#     k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0

def create_polynomial(k: int) -> str:
    """
    создает многочлен
    :param k: степень многочлена
    :return: строка
    """
    line = ''
    degrees = [i for i in range(1, k + 1)]
    degrees.reverse()

    coefficients = [randint(0, 101) for i in range(4)]

    if k > 1:
        for key, value in enumerate(degrees):
            if value > 1:
                x = f'x**{str(value)}'

                if coefficients[key] > 1:
                    x = f'{str(coefficients[key])}x**{str(value)}'
            else:
                x = 'x'

            if value > 1:
                end = ' + '
            else:
                end = ''

            line += x + end

        if coefficients[-1] != 0:
            line += f' + {str(coefficients[-1])}'
    else:
        line = 'x'

    return f'{line} = 0'


def write_in_file(value: str):
    with open('file.txt', 'a') as data:
        data.writelines(f'{value}\n')


k = int(input('Задайте степень многочлена: '))
polynomial = create_polynomial(k)
write_in_file(polynomial)
