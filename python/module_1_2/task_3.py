def Factorial(Number):
    if Number == 0:
        return 1
    elif Number < 0:
        return 'Факториал отрицательного числа не существует'
    else:
        return Number * Factorial(Number-1)

n = int(input('Введите число:'))
print(Factorial(n))