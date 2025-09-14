def calculate_months_to_threshold(start, rate, threshold):
    rate = rate / 100
    month = 0
    # результат должен быть 0 — цель уже достигнута
    if start >= threshold:
        return month
    # процент роста отрицательный или 0
    if rate <= 0:
        return 'ValueError: "Growth rate must be greater than 0."'
    if start <= 0 or threshold <= 0:
        return 'ValueError: "Start and threshold must be positive numbers."'

    while start < threshold:
        start += start * rate
        month += 1
        # защита от бесконечного цикла
        if month > 1000:
            print("Бесконечный цикл")
            break
    return month

# Пример использования
start = int(input("Введите начальное количество пользователей: "))
rate = float(input("Введите темп роста в процентах: "))
threshold = int(input("Введите пороговое значение: "))

months = calculate_months_to_threshold(start, rate, threshold)
print(f"Количество месяцев для достижения порога: {months}")