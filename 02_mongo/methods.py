from pymongo.collection import Collection
from wrappers import db_operation_error

@db_operation_error
def create_cat(collection: Collection, name:str, age:int, features:list[str]):
    cat = {"name": name, "age": age, "features": features}
    print(cat)
    collection.insert_one(cat)
    print(f"Кицька {name} додана до бази")

@db_operation_error
def read_all_cats(collection: Collection):
    cats = collection.find()
    print("В базі маємо такі записи")
    for cat in cats:
        print(cat)

@db_operation_error
def read_cat_by_name(collection: Collection, name: str):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кицьку на ім'я {name} не знайдено")

@db_operation_error
def update_cat_age(collection: Collection, name: str, new_age: int):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кицьки {name} оновлено на {new_age}")
    else:
        print(f"Кицьку на ім'я {name} не знайдено")

@db_operation_error
def add_feature_to_cat(collection: Collection, name: str, feature: str):
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.matched_count > 0:
        print(f"Кицькі '{name}' було додано особливість {feature}")
    else:
        print(f"Кицьку на ім'я {name} не знайдено")

@db_operation_error
def delete_cat(collection: Collection, name: str):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кицька {name} була видалена з бази")
    else:
        print(f"Кицьку на ім'я {name} не знайдено")

@db_operation_error
def delete_all_cats(collection: Collection):
    result = collection.delete_many({})
    print(f"Всі записи було видалено. Загальна кількість видалених записів: {result.deleted_count}")
