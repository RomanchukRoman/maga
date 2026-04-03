# номер посылки 159787694

def main() -> None:
    '''Программа, которая расшифровывает сжатые сообщения и возвращает строку с командами.'''
    instructions: str = input()
    numbers: str = '0123456789'
    start_range: str = '['
    end_range: str = ']'
    
    result: str = ''
    stack: list = [] 
    current_str: str = ''
    current_num: str = ''

    for instruction in instructions:
        if instruction in numbers:
            current_num += instruction
        elif instruction == start_range:
            stack.append((int(current_num) if current_num else 1, current_str))
            current_str = ''
            current_num = ''
        elif instruction == end_range:
            num, prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += instruction
    
    result = current_str
    print(result)

if __name__ == '__main__':
    main()