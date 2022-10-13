# Реализуйте алгоритм перемешивания списка.
from random import randint

# формируем случайные неповторяющиеся индексы от 1 до значения длинны заданного списка


def digits_mas_random(list_a):
    mas = []
    k = len(list_a)-1
    mas.append(randint(0, k))
    i = 0
    while i < k:
        j = randint(0, k)
        if not (j in mas):
            mas.append(j)
            i = i+1
    print(mas)
    return mas


def input_mas():
    mas = []
    mas = [int(i) for i in input().split()]
    return mas


# print('Введите массив значений : ')
# list_a = input_mas()
list_a = [1, 23, 'rt', 'u', 234, 6, 'dr4', 214]
list_random_index = digits_mas_random(list_a)

for i in range(0,4):
    # print(list_a[i],' - ', list_random_index[i])
    temp_b=int(list_random_index[i])
    print(temp_b,' - ',list_a[temp_b])
    temp_a = list_a[i]
    list_a[i] = list_a[temp_b]
    list_a[temp_b] = temp_a

print(list_random_index)
print(list_a)
