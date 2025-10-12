def count_char(lst, char):
    # Проверки на список и строку
    if not isinstance(lst, list):
        raise TypeError("Первый аргумент должен быть списком строк")
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("Второй аргумент должен быть строкой длинной 1 символ")
    
    # Основная часть программы
    new_lst = []
    for i in lst:
        new_lst.append(i.count(char))
    return new_lst

# Пример использования
test_list = ["helloo", "world", ""]
char_to_count = "o"

result = count_char(test_list, char_to_count)
print("Результат:", result)