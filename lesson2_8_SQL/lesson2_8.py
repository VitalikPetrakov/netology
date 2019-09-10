import psycopg2

"""Student:
 id     | integer                  | not null
 name   | character varying(100)   | not null
 gpa    | numeric(10,2)            |
 birth  | timestamp with time zone |

Course:
 id     | integer                  | not null
 name   | character varying(100)   | not null
 """


# for row in curs:
#     print(row)

def create_db(): # создает таблицы
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute("""CREATE TABLE Student (
                id serial PRIMARY KEY not NULL,
                name varchar(100) not NULL,
                gpa numeric(10, 2),
                birth timestamp with time zone);
                """)
            curs.execute("""CREATE TABLE Course (
                id serial PRIMARY KEY not NULL,
                name varchar(100) not NULL);
                """)


def del_all_tables():
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute('DROP TABLE Student;')
            curs.execute('DROP TABLE Course;')


def get_students(course_id): # возвращает студентов определенного курса
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute('select ')


def add_students(course_id, students): # создает студентов и
                                       # записывает их на курс
    pass


def add_student(student): # просто создает студента
    pass


def get_student(student_id):
    pass


if __name__ == '__main__':
    create_db()
    # del_all_tables()
