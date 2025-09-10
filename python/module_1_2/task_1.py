def sum(number_1, number_2):
    result = number_1 + number_2
    return result

def difference(number_1, number_2):
    result = number_1 - number_2
    return result

def composition(number_1, number_2):
    result = number_1 * number_2
    return result

def division(number_1, number_2):
    result = number_1 / number_2
    return result

number_1 = int(input('Введите первое число:'))
number_2 = int(input('Введите второе число:'))

print("Сумма:", sum(number_1, number_2))
print("Разность:", difference(number_1, number_2))
print("Произведение:", composition(number_1, number_2))
print("Деление:", division(number_1, number_2))