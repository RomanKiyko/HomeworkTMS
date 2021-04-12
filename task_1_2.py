# Даны действительные числа x и y. Получить (|x|-|y|)/(1+|xy|)

x, y = float(input('Введите x: ')), float(input('Введите y: '))
print("(|x|-|y|)/(1+|xy|) =", (abs(x) - abs(y)) / (1 + abs(x * y)))