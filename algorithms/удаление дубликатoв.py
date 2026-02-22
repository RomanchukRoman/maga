def main():
    count_items = int(input())
    items = input().split()
    new_items = []
    underlines = []

    for item in items:
        if item in new_items:
            underlines.append('_')
        else:
            new_items.append(item)
    
    new_items.extend(underlines) 
    print(' '.join(new_items))   

if __name__ == '__main__':
    main() 