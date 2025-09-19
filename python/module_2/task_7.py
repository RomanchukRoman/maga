def triangle_type(trian1, trian2, trian3):
    if (trian1 and trian2 and trian3) <= 0:
        return 'Невозможно'
    
    # неравенство треугольника: a + b > c, a + c > b, b + c > a
    if (trian1 + trian2 > trian3 and trian1 + trian3 > trian3 and trian2 + trian3 > trian1):
        if trian1 == trian2 == trian3:
            result = 'Равносторонний'
        elif trian1 == trian2 or trian1 == trian3 or trian2 == trian3:
            result = 'Равнобедренный'
        else:
            result = 'Разносторонний'
    else:
        return 'Невозможно'
    return result

# Пример использования
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

result = triangle_type(a, b, c)
print(f"Тип треугольника: {result}")