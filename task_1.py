from math import pi


# Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

def get_precision(line: str) -> int:
    """
    получает количество символов после запятой в вещественном числе
    :param line:
    :return:
    """

    if '.' not in line:
        return 0

    return len(line[line.index('.') + 1:])


value = input('Введите с какой точностью хотите получить число Пи: ')
precision = get_precision(value)

print(format(pi, f'.{precision}f'))
