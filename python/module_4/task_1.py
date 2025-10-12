def is_palindrome(string):
    # Проверка типа
    if not isinstance(string, str):
        raise TypeError('Аргумент должен быть строкой')
    # Программа
    return string == string[::-1]

def is_palindrome_recursive(string):
    # Проверка типа
    if not isinstance(string, str):
        raise TypeError('Аргумент должен быть строкой')
    # Программа
    if len(string) <= 1:
        return True
    result = string[0] == string[-1]
    return result and is_palindrome_recursive(string[1:-1])

# Получение ввода от пользователя
string_input = 'топот'

# Вывод результатов
print("Обычный метод:", is_palindrome(string_input))
print("Рекурсивный метод:", is_palindrome_recursive(string_input)) 