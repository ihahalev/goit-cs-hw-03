import psycopg2
from db_config import host, dbname, user, password
from faker import Faker
import random

# Налаштування Faker
fake = Faker()

# Функції для генерації даних
def generate_users(n=10):
    """ Генерує випадкові дані для таблиці користувачів """
    users = []
    emails = []
    for _ in range(n):
        email = fake.email()
        while email in emails:
            email = email = fake.email()
        users.append((fake.name(), email))
        emails.append(email)
    return users

def generate_statuses():
    """ Генерує фіксовані статуси для таблиці статусів """
    statuses = [('new',), ('in progress',), ('completed',)]
    return statuses

def generate_tasks(users: list, statuses: list, n=30):
    """ Генерує випадкові дані для таблиці завдань """
    tasks = []
    random.choices
    for _ in range(n):
        tasks.append((
            fake.text(max_nb_chars=20),
            fake.sentence(nb_words=10),
            random.choice(statuses),
            random.choice(users)
        ))
    return tasks


# Функція для заповнення бази даних
def populate_database():
    conn = None
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cur = conn.cursor()

        # Вставка користувачів
        users = generate_users()
        cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)
        cur.execute("SELECT id FROM users")
        users_id = cur.fetchall()

        # Вставка статусів
        statuses = generate_statuses()
        cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)
        cur.execute("SELECT id FROM status")
        statuses_id = cur.fetchall()

        # Вставка завдань
        tasks = generate_tasks(users_id, statuses_id)
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        conn.commit()
        cur.close()
        print("Database population ended")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # Виклик функції для заповнення бази даних
    populate_database()
