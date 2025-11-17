import os

def parse_log_file(log_path):
    'Функция для построчного анализа лог-файла и подсчета ошибок каждого типа'
    dir = os.getcwd()
    file = log_path
    path = os.path.join(dir, file)
    errors = ['INFO', 'WARNING', 'ERROR']
    analyse = {}

    try:
        with open(path, 'r') as file:
            for line in file:
                error_type = line.split(':')[0]
                if error_type in errors:
                    analyse[error_type] = analyse.get(error_type, 0) + 1
    except FileNotFoundError:
       raise FileNotFoundError(f'"Log file not found at path: {path}"')
    return analyse

# Пример использования

log_counts = parse_log_file('server.log')
print("Статистика логов:", log_counts)