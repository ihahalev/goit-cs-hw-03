import psycopg2
from db_config import host, dbname, user, password

def create_db():
    conn = None
    try:
        # Підключаємось до бази даних
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cur = conn.cursor()

        # Читаємо файл з SQL запитами на створення таблиць
        with open('01_sql/create_tables.sql', 'r') as f:
            sql_requests = f.read()

        # Виконуємо запити створення таблиць
        cur.execute(sql_requests)

        # Завершуємо транзакцію
        conn.commit()

        # Закриваємо з'єднання
        cur.close()
        conn.close()

        print("Tables created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_db()
