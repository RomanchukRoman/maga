# номер посылки 159776166

def main() -> None:
    '''Определение минимального количества транспортных платформ, необходимых для перевозки всех роботов, описанных в массиве.'''
    robots: list[int] = list(map(int, input().split()))
    limit: int = int(input())
    platforms: int = 0

    robots.sort()
    lo: int = 0
    hi: int = len(robots) - 1

    while lo <= hi:
        if robots[lo] + robots[hi] <= limit:
            lo += 1
            hi -= 1
        else:
            hi -= 1
        platforms += 1
    print(platforms)

if __name__ == '__main__':
    main()