# сортировка методом пузырька

example_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubble_sort(data):
    last_index = len(data) - 1

    for i in range(last_index):
        for i in range(last_index):
            item_index = i
            swapped = False
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = data[item_index + 1], data[item_index]
                swapped = True
                last_index - 1

    return data


print(bubble_sort(example_array))