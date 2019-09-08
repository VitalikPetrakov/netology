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


def create_db(): # создает таблицы
    with psycopg2.connect('dbname=netology user=netology') as conn:
        with conn.cursor() as curs:
            curs.execute("""CREATE TABLE Student (
                id serial PRIMARY KEY is not NULL,
                name varchar(100) is not NULL,
                gpa numeric(10, 2),
                birth timestamp with time zone);
                """)
            curs.execute("""CREATE TABLE Course (
                id serial PRIMARY KEY is not NULL,
                name varchar(100) is not NULL);
                """)


def get_students(course_id): # возвращает студентов определенного курса
    pass


def add_students(course_id, students): # создает студентов и
                                       # записывает их на курс
    pass


def add_student(student): # просто создает студента
    pass


def get_student(student_id):
    pass
