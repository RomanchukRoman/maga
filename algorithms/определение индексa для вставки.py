# реализация поиска индекса элемента через бинарный поиск
def main():
    items = list(map(int, input().split()))
    item = int(input())

    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == item:
            print(mid)
            return
        if items[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    print(left)

if __name__ == '__main__':
    main() 
