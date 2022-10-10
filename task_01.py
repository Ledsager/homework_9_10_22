# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def DigitsSum(elem):
    result = 0
    i = 0
    for i in elem:
        if (i != '.') and (i != '-'):
            result = result + int(i)
    return result


print('Введите вещественное число:')
n = float(input())
elem = str(n)
print(DigitsSum(elem))
