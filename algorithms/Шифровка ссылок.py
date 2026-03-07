from random import choice

class MarsURLEncoder:

    def __init__(self, symbols='thequickbrownfoxjumpsoverthelazydog0123456789', dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.symbols = symbols
        self.dictionary = dictionary

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        while True:
            short_url = ''
            for i in range(6):
                short_url += choice(self.symbols)

            if 'https://ma.rs/' + short_url  not in self.dictionary:
                break
            
        short_url = 'https://ma.rs/' + short_url 
        self.dictionary[short_url] = long_url

        return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.dictionary.get(short_url, 'Not found')
    
test = MarsURLEncoder()
print(test.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))
print(test.decode('https://ma.rs/8voe36'))

# Для проверки хеша на уникальность примените цикл while: «пока среди ключей итогового словаря есть получившийся хеш, генерируй хеш заново».