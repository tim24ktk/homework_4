from sympy import Symbol


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму
# многочленов. В file1.txt : 2*x**2 + 4*x + 5 В file2.txt: 4*x**2 + 1*x + 4 Результирующий файл: 6*x**2 + 5*x + 9

def read_file(value: str):
    """
    считывает из файла значение value
    :param value:
    """
    text_file = open(value, 'r')
    lines = text_file.read().split('\n')
    text_file.close()

    return lines


def sum_of_polynomials(first_values, second_values):
    x = Symbol('x')
    y = Symbol('y')
    result = []

    for i in range(len(first_values)):
        a = first_values[i][:-4].split(' + ')
        b = second_values[i][:-4].split(' + ')

        for k in range(len(a)):
            result.append(f'{eval(a[k]) + eval(b[k])}')

    return f'{" + ".join(result)} = 0'


def write_in_file(value: str):
    """
    записывает в файл значение value
    :param value:
    """
    with open('result.txt', 'a') as data:
        data.write(f'{value}\n')


first_file = read_file('file_1.txt')
second_file = read_file('file_2.txt')
result = sum_of_polynomials(first_file, second_file)

write_in_file(result)
