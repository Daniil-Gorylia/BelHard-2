print ('Арифметичские операторы')

a = 5
b = 8
print(a + b)
print(a - b)
print(a + b - a * b)

print(a / b % a ** b // a)
print(a + 0.857 - b)
print('Операторы сравнения')
c = 250

if c != a:
    d = c - 10
    print(d)

if c >= a:
    print('больше или равно')
else:
    print('не больше, и не равно')

if c <= a:
    print('меньше или равно')
else:
    print('не меньше, и не равно')

print('операторы присвоения')
a += 5

print(a)

a -= b
print(a)

print('Побитовые операторы')

# Я не совсем понял как работают побитовые операторы

a = 60
b = 13

c = (a & b)

print(c)

a = 60
b = 13

c = (a | b)

print(c)

a = 13
d = (~a)
print(d)


print('Логические операторы')
a = 5
b = 8

if a > 0 \
        and b > 0:
    print('a и b положительные числа')
else:
    print('условия не выполнены')

if a < 0 \
        or b < 0:
    print('условия выполнены')
else:
    print('условия не выполнены')

print('Операторы членства')

a = [2, 4, 6, 8, 10]

b = 8

if b in a:
    print('число b - четное')
else:
    print('число b - нечетное')

a = [1, 5, 3, 81, 100200]

b = input('введите любое значение')

c = int(b)
if c in a:
    print('введенное значение есть в списке')
else:
    print('введенных данных нету в списке')
