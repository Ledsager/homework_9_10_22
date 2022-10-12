# Задайте список из n чисел последовательности $(1+1/n)**n$ и выведите на экран их сумму.

def DigitsMas(elem):
    result = 0
    mas = {}

    for i in range(1, elem+1):
        result = result+(1+1/i)**i
        mas[i] = round((1+1/i)**i, 5)
    print(mas)
    return result


print('Введите целое число (n>0):')
n = int(input())
if (n % 1 == 0 and n > 0):
    print(f'Сумма элемнтов последовательности = {DigitsMas(n)}')
else:
    print('введенное число не соответствует условию!')
