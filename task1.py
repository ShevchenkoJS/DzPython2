# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
num = abs(float(input('Введите вещественное число: ')))
sum = 0
for i in str(num):
    if i != '.':
        sum = sum + int(i)
print('Сумма цифр  равна ', sum)