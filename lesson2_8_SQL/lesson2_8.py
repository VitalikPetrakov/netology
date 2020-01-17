import psycopg2


def create_db():
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
            curs.execute("""CREATE TABLE student_course (
                id serial PRIMARY KEY not NULL,
                student_id integer references student(id),
                course_id integer references course(id));
                """)


def del_all_tables():
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute('DROP TABLE Student CASCADE;')
            curs.execute('DROP TABLE Course CASCADE;')
            curs.execute('DROP TABLE student_course CASCADE;')


def get_students(course_id):
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute("""select * from student 
            join student_course on student.id = student_course.student_id
            and course_id = (%s);""", (course_id, ))
            for row in curs:
                print(row)


def add_students(course_id, students):
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            for student in students:
                curs.execute("insert into Student (name, gpa, birth) values (%s, %s, %s)",
                             (student['name'], student['gpa'], student['birth']))
                curs.execute("""insert into student_course (student_id, course_id)
                 select student.id, (%s) from student where student.name = (%s);""",
                             (course_id, student['name'],))


def add_student(student):
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute("insert into Student (name, gpa, birth) values (%s, %s, %s)",
                         (student['name'], student['gpa'], student['birth']))


def get_student(student_id):
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute("select * from Student where id = (%s)", (student_id, ))
            for row in curs:
                print(row)


def add_course(name_of_course):
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute("insert into Course (name) values (%s)", (name_of_course, ))


def entry_course(student_id, course_id):
    with psycopg2.connect(dbname='netology', user='netology', password='123') as conn:
        with conn.cursor() as curs:
            curs.execute("insert into student_course (student_id, course_id) values (%s, %s)",
                         (student_id, course_id))


if __name__ == '__main__':
    test = {'name': 'test3', 'gpa': 3, 'birth': '11.09.2019'}
    test2 = [{'name': 'test1', 'gpa': 3, 'birth': '11.09.2019'},
             {'name': 'test2', 'gpa': 4, 'birth': '11.09.2019'}]
    # create_db()
    # del_all_tables()
    # add_student(test)
    # get_student(3)
    # get_students(1)
    # add_course('prog')
    # entry_course(2, 1)
    # add_students(1, test2)
    # get_students(2)


