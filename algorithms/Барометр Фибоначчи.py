def main(n):
    # базовый случай
    if n == 0: 
        return 1
    if n == 1:
        return 1
    # посчитать число Фибоначи
    f = main(n - 1) + main(n - 2)
    return f

if __name__ == '__main__':
    print(main(5))