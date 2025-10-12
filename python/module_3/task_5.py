def filter_dict_by_value(d, threshold):
    # Тут будут проверки
    if not isinstance(d, dict):
        raise TypeError('Первый аргумент должен быть словарем')
    if not isinstance(threshold, (int, float)):
        raise TypeError('Второй аргумент должен быть числом')
    
    # Тело программы
    new_d = {}
    for key, value in d.items():
        if value > threshold:
            new_d[key] = value

    return new_d

# Пример использования
data = {'a': 1, 'b': 2, 'c': 3}
limit = 2.4
result = filter_dict_by_value(data, limit)
print("Результат:", result)