# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле pozition.txt в одной строке одно число.

# формирование списка [-n,n]
def DigitsMas(length):
    mas = []
    for i in range(-length, length+1):
        mas.append(i)
    for i in range(0, len(mas)):
        print(mas[i],end=' ')
    print()
    return mas

# 1й способ: подсчета произведения элементов на указанных позициях.
# позиции беруться из pozition.txt
# построчно считывается информация из файла. Строка преобразуется в число.
# Полученное число в цикле сравнивается с позицией элемента списка.
# Если значения равны выполняем условие перемножения.

def DigitsMultiply(array1):
    multyplypozition = 1
    with open('pozition.txt', 'r') as fileread:
        for line in fileread:
            for i in range(0, len(array1)):
                if int(line) == i+1:
                    multyplypozition = multyplypozition*int(array1[i])
                    # print(line, array1[i])
    return multyplypozition

# 2й способ: считываем весь файл с позициями необходимых элементов и формируем список

def DigitsFileArray():
    with open('pozition.txt', 'r') as f:
        f_contents = f.read()
    filestr=f_contents.split()
    return filestr


print('Введите целое число (n>0):')
n = int(input())
if (n % 1 == 0 and n > 0):
    array1 = DigitsMas(n)
    print('1й вариант: Произведение элементов на заданных позициях = ',DigitsMultiply(array1))
else:
    print('введенное число не соответствует условию!')
# 2й способ продолжение: в циклах проверяем условие задачи.
# Полученный список позиций из файла сравниваем с позициями списка заданным условием задачи.
# Если условие выполняется то перемножаем нужные значения элементов.
pozmulty=DigitsFileArray()
result=1
for i in range(0, len(array1)):
    for line in pozmulty:
        if int(line) == i+1:
            result = result*int(array1[i])
print('2й вариант: Произведение элементов на заданных позициях = ',result)
