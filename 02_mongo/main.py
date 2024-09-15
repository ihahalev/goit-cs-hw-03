from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from methods import *

# Підключення до MongoDB
try:
    client = MongoClient("mongodb+srv://ihahalev:7Tw5OLAWDpnury5p@cluster0.xtr3p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["cat_database"]
    collection = db["cats"]
    # Перевірка з'єднання
    client.admin.command('ismaster')
    print("MongoDB підключено успішно")
except ConnectionFailure:
    print("Не вдалося підключитися до MongoDB, перевірте з'єднання")

def main():
    while True:
        print("\nДоступні дії:")
        print("1 - Створити запис про тварину")
        print("2 - Показати всі записи")
        print("3 - Пошук запису за ім'ям тварини")
        print("4 - Оновити вік тварини")
        print("5 - Додати особливість до тварини")
        print("6 - Видалити запис про тварину")
        print("7 - Видалити всі записи")
        print("8 - Вийти")
        choice = input("Виберіть дію: ")

        match choice:
            case "1":
                name = input("Вкажіть ім'я: ")
                age = int(input("Вкажіть вік: "))
                features = input("Вкажіть особливості улюбленця (через кому): ").split(",")
                create_cat(collection, name, age, features)
            case "2":
                read_all_cats(collection)
            case "3":
                name = input("Вкажіть ім'я: ")
                read_cat_by_name(collection, name)
            case "4":
                name = input("Вкажіть ім'я: ")
                new_age = int(input("Вкажіть вік: "))
                update_cat_age(collection, name, new_age)
            case "5":
                name = input("Вкажіть ім'я: ")
                feature = input("Вкажіть особливість: ")
                add_feature_to_cat(collection, name, feature)
            case "6":
                name = input("Вкажіть ім'я: ")
                delete_cat(collection, name)
            case "7":
                delete_all_cats(collection)
            case "8":
                break
            case _:
                print("Не вірна команда, спробуйте ще.")

if __name__ == "__main__":
    main()
