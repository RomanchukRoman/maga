# Романчук Роман Валерьевич
# Изначально вариант 8, но на платформе Яндекс Практикум ошибка, варианты смещены, поэтому вариант 9-10
# Условия:
# Таблицы категории (без учёта древовидной структуры) и блюда (без связи с остальными таблицами).

import sys
sys.path.append('tables')

from project_config import *
from dbconnection import *
from tables.categories_table import *
from tables.dishes_table import *

class Main:

    config = ProjectConfig()
    connection = DbConnection(config)

    def __init__(self):
        DbTable.dbconn = self.connection
        return

    def db_init(self):
        ct = CategoriesTable()
        dt = DishesTable()
        ct.create()
        dt.create()
        return

    def db_insert_somethings(self):
        ct = CategoriesTable()
        dt = DishesTable()
        
        # categories: name и parent_id
        ct.insert_one(["Салаты", None])
        ct.insert_one(["Супы", None])  
        ct.insert_one(["Десерты", None])
        
        # dishes: category_id, description, image_id, name, technic, time
        dt.insert_one([1, "Салат Цезарь с курицей", None, "Цезарь", "Нарезать, смешать", 30])
        dt.insert_one([1, "Салат Оливье", None, "Оливье", "Варить, резать, смешать", 45])
        dt.insert_one([2, "Красный борщ", None, "Борщ", "Варить овощи", 60])

    def db_drop(self):
        dt = DishesTable()
        pt = CategoriesTable()
        dt.drop()
        pt.drop()
        return

    def show_main_menu(self):
        menu = """Добро пожаловать! 
Основное меню (выберите цифру в соответствии с необходимым действием): 
    1 - просмотр категорий;
    2 - сброс и инициализация таблиц;
    9 - выход."""
        print(menu)
        return

    def read_next_step(self):
        return input("=> ").strip()

    def after_main_menu(self, next_step):
        if next_step == "2":
            self.db_drop()
            self.db_init()
            self.db_insert_somethings()
            print("Таблицы созданы заново!")
            return "0"
        elif next_step != "1" and next_step != "9":
            print("Выбрано неверное число! Повторите ввод!")
            return "0"
        else:
            return next_step
            
    def show_categories(self):
        self.category_id = -1
        menu = """Просмотр списка категорий!
№\tКатегория"""
        print(menu)
        lst = CategoriesTable().all()
        for i in lst:
            print(str(i[0]) + "\t" + str(i[1]))
        menu = """Дальнейшие операции: 
    0 - возврат в главное меню;
    3 - добавление новой категории;
    4 - удаление категории;
    5 - просмотр блюд категории;
    8 - редактирование категории;
    9 - выход."""
        print(menu)
        return

    def after_show_categories(self, next_step):
        while True:
            if next_step == "4":
                self.delete_category()
                return "1"
            elif next_step == "6":
                self.show_add_dish()
                next_step = "5"
            elif next_step == "7":
                self.delete_dish()
                next_step = "5"
            elif next_step == "8":
                self.edit_category()
                return "1"
            elif next_step == "5":
                next_step = self.show_dishes_by_categories()
            elif next_step != "0" and next_step != "9" and next_step != "3":
                print("Выбрано неверное число! Повторите ввод!")
                return "1"
            else:
                return next_step

    def delete_category(self):
        """Удаление выбранной категории"""
        num = input("Укажите номер строки категории для удаления (0 - отмена): ").strip()
        if num == "0":
            return
        
        try:
            num = int(num)
            category = CategoriesTable().find_by_position(num)
            if not category:
                print("Категория с таким номером не найдена!")
                return
            
            # Проверяем есть ли связанные блюда
            dishes_count = len(DishesTable().all_by_category_id(category[0]))
            if dishes_count > 0:
                print(f"Внимание: в категории есть {dishes_count} блюд(о), они будут удалены вместе с категорией!")
            
            confirm = input(f"Вы уверены, что хотите удалить категорию '{category[1]}'? (y/n): ")
            if confirm.lower() == 'y':
                CategoriesTable().delete_by_id(category[0])
                print("Категория удалена!")
            else:
                print("Удаление отменено.")
                
        except ValueError:
            print("Ошибка: введите корректный номер!")

    def edit_category(self):
        """Редактирование выбранной категории"""
        num = input("Укажите номер строки категории для редактирования (0 - отмена): ").strip()
        if num == "0":
            return
        
        try:
            num = int(num)
            category = CategoriesTable().find_by_position(num)
            if not category:
                print("Категория с таким номером не найдена!")
                return
            
            print(f"Текущее название: {category[1]}")
            new_name = input("Введите новое название категории (Enter - оставить без изменений): ").strip()
            
            if new_name:
                while len(new_name.strip()) == 0:
                    new_name = input("Название не может быть пустым! Введите название заново: ").strip()
                
                while len(new_name.strip()) > 64:
                    new_name = input("Название не может быть более 64 символов! Введите название заново: ").strip()
                
                # Обновляем категорию
                CategoriesTable().update_by_id(category[0], {"name": new_name})
                print("Категория обновлена!")
            else:
                print("Изменения отменены.")
                
        except ValueError:
            print("Ошибка: введите корректный номер!")

    def delete_dish(self):
        """Удаление выбранного блюда"""
        if self.category_id == -1:
            print("Сначала выберите категорию!")
            return
        
        print("Блюда:")
        lst = DishesTable().all_by_category_id(self.category_id)
        for i, dish in enumerate(lst, 1):
            print(f"{i}\t{dish[4]}")  # dish[4] - название блюда
        
        num = input("Укажите номер блюда для удаления (0 - отмена): ").strip()
        if num == "0":
            return
        
        try:
            num = int(num)
            if num < 1 or num > len(lst):
                print("Блюдо с таким номером не найдено!")
                return
            
            dish_to_delete = lst[num - 1]
            confirm = input(f"Вы уверены, что хотите удалить блюдо '{dish_to_delete[4]}'? (y/n): ")  # dish[4]
            if confirm.lower() == 'y':
                DishesTable().delete_by_id(dish_to_delete[0])
                print("Блюдо удалено!")
            else:
                print("Удаление отменено.")
                
        except ValueError:
            print("Ошибка: введите корректный номер!")

    def show_add_category(self):
        name = input("Введите название категории (1 - отмена): ").strip()
        if name == "1":
            return
        
        while len(name.strip()) == 0:
            name = input("Название не может быть пустым! Введите название заново (1 - отмена):").strip()
            if name == "1":
                return
        
        while len(name.strip()) > 64:
            name = input("Название не может быть более 64 символов! Введите название заново (1 - отмена):").strip()
            if name == "1":
                return
        
        CategoriesTable().insert_one([name, None])
        return

    def show_add_dish(self):
        """Добавление нового блюда"""
        if self.category_id == -1:
            print("Сначала выберите категорию!")
            return
        
        print("Добавление нового блюда:")
        
        # Название блюда
        name = input("Введите название блюда (1 - отмена): ").strip()
        if name == "1":
            return
        while len(name.strip()) == 0:
            name = input("Название не может быть пустым! Введите название заново (1 - отмена): ").strip()
            if name == "1":
                return
        while len(name.strip()) > 64:
            name = input("Название не может быть более 64 символов! Введите название заново (1 - отмена): ").strip()
            if name == "1":
                return
        
        # Время приготовления
        time_str = input("Время приготовления (в минутах): ").strip()
        try:
            time_val = int(time_str)
            if time_val <= 0:
                print("Время должно быть положительным числом!")
                return
        except ValueError:
            print("Ошибка: введите корректное число!")
            return
        
        # Описание
        description = input("Описание блюда: ").strip()
        while len(description.strip()) == 0:
            description = input("Описание не может быть пустым! Введите описание заново: ").strip()
        
        # Техника приготовления
        technic = input("Техника приготовления: ").strip()
        while len(technic.strip()) == 0:
            technic = input("Техника не может быть пустой! Введите технику заново: ").strip()
        
        # Вставляем блюдо (category_id, description, image_id, name, technic, time)
        DishesTable().insert_one([self.category_id, description, None, name, technic, time_val])
        print("Блюдо добавлено!")

    def show_dishes_by_categories(self):
        if self.category_id == -1:
            while True:
                num = input("Укажите номер строки, в которой записана интересующая Вас категория (0 - отмена):")
                while len(num.strip()) == 0:
                    num = input("Пустая строка. Повторите ввод! Укажите номер строки, в которой записана интересующая Вас категория (0 - отмена):")
                if num == "0":
                    return "1"
                category = CategoriesTable().find_by_position(int(num))
                if not category:
                    print("Введено число, неудовлетворяющее количеству категорий!")
                else:
                    self.category_id = int(category[0]) 
                    self.category_obj = category
                    break
        print("Выбрана категория: " + self.category_obj[1])
        print("Блюда:")
        lst = DishesTable().all_by_category_id(self.category_id)
        for i, dish in enumerate(lst, 1):
            # dish[4] - name (название блюда)
            print(f"{i}\t{dish[4]}")
        
        menu = """Дальнейшие операции:
        0 - возврат в главное меню;
        1 - возврат в просмотр категорий;
        6 - добавление нового блюда;
        7 - удаление блюда;
        9 - выход."""
        print(menu)
        return self.read_next_step()

    def main_cycle(self):
        current_menu = "0"
        next_step = None
        while(current_menu != "9"):
            if current_menu == "0":
                self.show_main_menu()
                next_step = self.read_next_step()
                current_menu = self.after_main_menu(next_step)
            elif current_menu == "1":
                self.show_categories()
                next_step = self.read_next_step()
                current_menu = self.after_show_categories(next_step)
            elif current_menu == "2":
                self.show_main_menu()
            elif current_menu == "3":
                self.show_add_category()
                current_menu = "1"
        print("До свидания!")    
        return

    def test(self):
        DbTable.dbconn.test()

m = Main()
# Откоментируйте эту строку и закоментируйте следующую для теста
# соединения с БД
# m.test()
m.main_cycle()