import psycopg2

"создание базы данных"


def create_db():
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute("""CREATE TABLE People """)