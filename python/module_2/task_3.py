def how_many_times(message):
    # Эта проверка добавлена по требованию в задании, но кажется бесполезной, так как input() и так всегда строку возвращает
    if not isinstance(message, str):
        error = "ошибка №1 - введите строку"
        return error

    message = message.strip().lower()
    total = 0

    for char in message:
        if not ('a' <= char <= 'z'):
            error = "ошибка №2 - символы должны находятся в диапаоне 'a'–'z'"
            return error
        total += ord(char) - ord('a') + 1
    return total

# Пример использования
message = input("Введите сообщение (строчные буквы): ")
clicks = how_many_times(message)
print(f"Количество нажатий: {clicks}")