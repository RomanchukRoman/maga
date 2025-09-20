def replace_characters(lst, old, new):
    # сначала проверка типов данных и если не ок, то вывод ошибки и прерывание программы
    if not isinstance(lst, list):
        raise TypeError("lst must be a list of strings")
    if not isinstance(old, str) or not isinstance(new, str) or len(old) != 1 or len(new) != 1:
        raise TypeError("old and new must be single characters and str")
    
    # логика программы
    new_lst = []
    if not lst:
        return new_lst
    for i in lst:
        if not isinstance(i, str):
            raise TypeError("All elements in lst must be strings")
        new_lst.append(i.replace(old, new))
    return new_lst


# Тест кейсы
#result = replace_characters(["hello", "world"], "o", "1")               # ["hell1", "w1rld"]
result = replace_characters(["apple", "banana", "cherry"], "a", "o")    # ["opple", "bonono", "cherry"]
#result = replace_characters(["abracadabra"], "a", "o")                  # ["obrocodobro"]
#result = replace_characters([1], "a", "o")                               # All elements in lst must be strings

print(result)