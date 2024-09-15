import psycopg2
from db_config import host, dbname, user, password

def create_db():
    conn = None
    try:
        # Підключаємось до бази даних
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cur = conn.cursor()

        # Читаємо файл з описом запитів
        with open('01_sql/description.txt', 'r', encoding='utf-8') as f:
            descriptions = f.readlines()
        # Читаємо файл з SQL запитами
        with open('01_sql/requests.sql', 'r') as f:
            sql_requests = f.readlines()

        for i in range(len(descriptions)):
            print(descriptions[i])
            # Виконуємо запит
            cur.execute(sql_requests[i])
            try:
                if sql_requests[i].startswith("INSERT"):
                    get = sql_requests[i]
                    words = get.split(" ")
                    where = words[3].replace("(","").split(",")[0]
                    for w in words:
                        if w.startswith("VALUES"):
                            search = w
                            break
                    search = search.replace("VALUES(","").split(",")[0]
                    sql = f"SELECT * FROM {words[2]} WHERE {where}={search};"
                    print(sql)
                    cur.execute(sql)
                if sql_requests[i].startswith("UPDATE"):
                    get = sql_requests[i]
                    words = get.split(" ")
                    where = words[len(words)-1].split(";")[0]
                    sql = f"SELECT * FROM {words[1]} WHERE {where};"
                    print(sql)
                    cur.execute(sql)
                if sql_requests[i].startswith("DELETE"):
                    get = sql_requests[i]
                    words = get.split(" ")
                    where = words[len(words)-1].split(";")[0]
                    sql = f"SELECT * FROM {words[2]} WHERE {where};"
                    print(sql)
                    cur.execute(sql)
                print(cur.fetchall())
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        # Завершуємо транзакцію
        conn.commit()

        # Закриваємо з'єднання
        cur.close()
        conn.close()

        print("Requests run successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_db()
