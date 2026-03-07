def valid_mountain_array():
    from array import array
    items = list(map(int, input().split()))
    data = array('i', items)

    # Если точек 3 и меньше, то неправильная гора
    if len(data) < 3:
        return False
    
    # Если пики по краям, то неправильная гора
    peak_index = data.index(max(data))
    if peak_index == 0 or peak_index == len(data)-1:
        return False

    # Такая вершина единственная
    if data.count(data[peak_index]) > 1:
        return False
    
    # Проверка подъема до вершины
    for i in range(peak_index):
        if data[i] >= data[i+1]:
            return False
        
    # Проверка спуска с вершины
    for i in range(peak_index, len(data)-1):
        if data[i] <= data[i+1]:
            return False
        
    return True


if __name__ == '__main__':
    print(valid_mountain_array())
