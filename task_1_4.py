# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.

a, b = float(input('Введите a: ')), float(input('Введите b: '))
print('Среднее арифметическое a и b: ', ((a + b) / 2))
print('Среднее геометрическое a и b; ', ((a * b) ** 0.5))