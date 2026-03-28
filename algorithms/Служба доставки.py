def main() -> int:
    '''Определение минимального количества транспортных платформ, необходимых для перевозки всех роботов, описанных в массиве.'''
    robots: list = list(map(int, input().split()))
    limit: int = int(input())
    platforms: int = 0
    weight: int = 0

# надо попробовать скользящим окном, потому что мне нужно находить слайсы, подходящие под лимит
    for robot in robots:
        if robot <= limit and weight < limit:
            weight += robot
        elif weight == limit:
            platforms += 1
            weight = 0
        else:
            return 'None'
        
    return platforms

if __name__ == '__main__':
    main() 

# 1 2 3 - роботы
# 3 - лимит
# 2 - платформа