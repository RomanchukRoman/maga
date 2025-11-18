# Загрузка настроек проекта (в данном случае только настроек соединения с БД)
# из файла config.yaml.
import yaml
import os

class ProjectConfig:
    """Класс считывает базовые настройки из файла config.yaml"""

    def __init__(self):
        # Получаем директорию, где находится этот файл
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, 'config.yaml')

        with open(config_path) as f:
            config = yaml.safe_load(f)
            self.dbname = config['dbname']
            self.user = config['user']
            self.password = config['password']
            self.host = config['host']
            self.dbtableprefix = config['dbtableprefix']

# Этот метод запускается только, если запускать
# данный файл, а не подключать его.
if __name__ == "__main__":
    x = ProjectConfig()
    print(x.dbfilepath)
