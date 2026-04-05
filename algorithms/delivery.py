# номер посылки 159908626

def calculate_platforms(robots: list[int], limit: int) -> int:
    '''Определение количества транспортных платформ для перевозки роботов.'''
    sorted_robots = sorted(robots)
    light: int = 0
    heavy: int = len(sorted_robots) - 1
    platforms: int = 0

    while light <= heavy:
        if sorted_robots[light] + sorted_robots[heavy] <= limit:
            light += 1
        heavy -= 1
        platforms += 1
    
    return platforms

def main() -> int:
    '''Основная функция для ввода данных.'''
    robots: list[int] = [int(robot) for robot in input().split()]
    limit: int = int(input())
    
    result: int = calculate_platforms(robots, limit)
    return result

if __name__ == '__main__':
    result = main()
    print(result)