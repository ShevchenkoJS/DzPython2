# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random as r
num = abs(int(input('Введите целое число N: ')))
lst = [i for i in range(-num, num + 1)]
'''Заполняем список от -N до N.  
r.randint(-num, num + 1) - Заполнение случайными числами'''
print('Наш список:', lst)
path = 'file.txt'  # работа с текстовым файлом
text = open(path, 'w')  # запись в файл
for _ in range(num):
    text.write(f'{r.randint(1, num)}\n')
text.close()

multi = 1

text = open(path, 'r')  # чтение из файла
for _ in text:
    print(f'{_}')
    multi *= lst[int(_)]

print(f'Произведение равно {multi}')
text.close()