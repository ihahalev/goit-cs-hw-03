from pymongo.errors import PyMongoError

def db_operation_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PyMongoError as e:
            print(f"Помилка при роботі з MongoDB: {e}")
        except ValueError as e:
            print(f"Помилка введення: {e}")
    return inner