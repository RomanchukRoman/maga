def to_fahrenheit(celsius):
    result = celsius * 9/5 + 32
    return round(result, 1)

def to_kelvin(celsius):
    result = celsius + 273.15
    return round(result, 1)

celsius = float(input("Введите температуру в Цельсиях: "))
print("Фаренгейт:", to_fahrenheit(celsius))
print("Кельвин:", to_kelvin(celsius))