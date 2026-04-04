# номер посылки 159848640

NUMBERS: str = '0123456789'
START_RANGE: str = '['
END_RANGE: str = ']'

def decode_instructions(instructions: str) -> str:
    '''Расшифровка сжатых сообщений и возврат строки с командами.'''
    stack: list[tuple[int, str]] = [] 
    current_instruction: str = ''
    current_repeat: str = ''

    for instruction in instructions:
        if instruction in NUMBERS:
            current_repeat += instruction
        elif instruction == START_RANGE:
            repeat_count = int(current_repeat) if current_repeat else 1
            stack.append((repeat_count, current_instruction))
            current_instruction = ''
            current_repeat = ''
        elif instruction == END_RANGE:
            repeat_count, prev_instruction = stack.pop()
            current_instruction = prev_instruction + current_instruction * repeat_count
        else:
            current_instruction += instruction

    return current_instruction

def main() -> str:
    '''Основная функция для ввода данных.'''
    instructions: str = input()
    result: str = decode_instructions(instructions)
    return result

if __name__ == '__main__':
    result = main()
    print(result)