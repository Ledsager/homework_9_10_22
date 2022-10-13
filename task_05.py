# Реализуйте алгоритм перемешивания списка.
from random import randint

# формируем случайные неповторяющиеся индексы от 1 до значения длинны заданного списка


def digits_mas_random(list_a):
    mas = []
    k = len(list_a)
    mas.append(randint(1, k))
    i = 0
    while i < k-1:
        j = randint(1, k)
        if not (j in mas):
            mas.append(j)
            i = i+1
    # print(mas)
    return mas

# ввод списка через пробел


def input_mas():
    mas = []
    mas = [i for i in input().split()]
    return mas

# используя список случайных позиций (list_random_index) формирую доп список в которой записываю значения из заданого
# списка позиции,индексы которых совпадают с сформированным списком случайных позиций


def random_list_a(list_a):
    list_temp = []
    for i in range(0, len(list_a)):
        temp_b = int(list_random_index[i])-1
        # print(list_a[temp_b],'-',list_random_index[i])
        list_temp.append(list_a[temp_b])
    list_a=list_temp
    return list_a


print('Введите массив переменных : ')
list_a = input_mas()
# list_a = [1, 23, 'rt', 'u', 234, 6, 'dr4', 214,5]
list_random_index = digits_mas_random(list_a)
print(list_random_index)
print(list_a)
print(random_list_a(list_a))
