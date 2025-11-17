import requests
import json

def fetch_and_save_quotes(url, file_path, num_quotes=5):
    'Функция собирает случайные цитаты с веб-сайта и сохраняет их для последующего использования.'
    result = []
    
    for i in range(num_quotes):
        try:
            response = requests.get(url, timeout = 3, verify = False)
            # Специальный метод проверяющий ошибки HTTP и вызывающий исключение при ошибке
            response.raise_for_status()
            data = response.json()
            filtered_data = {
                    'content': data.get('content'),
                    'author': data.get('author')
                }
            result.append(filtered_data)
        except requests.exceptions.RequestException as e:
            print(f'Ошибка сети или HTTP: {e}')
            break
        except json.JSONDecodeError as e:
            print(f'Ошибка декодирования JSON. Получен невалидный ответ: {e}')
            break

        with open(file_path, 'w', encoding = 'utf-8') as file:
            json.dump(result, file, indent = 4, ensure_ascii=False)

# Пример использования
API_URL = "https://api.quotable.io/random"
OUTPUT_FILE = "quotes.json"

fetch_and_save_quotes(API_URL, OUTPUT_FILE, num_quotes=5)
print(f"Собрано и сохранено в файл {OUTPUT_FILE}")