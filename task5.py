import random as r


def shuffle_my_list(sm_list):
    for _ in range(len(sm_list)):
        k = r.randint(0, (len(sm_list) - 1))
        sm_list.append(sm_list.pop(k))

num = abs(int(input('Введите целое число N: ')))
lst = [i for i in range(-num, num + 1)]
print('Наш список:', lst)
new_list = lst[:]
shuffle_my_list(new_list)
print('Перемешанный список:', new_list)