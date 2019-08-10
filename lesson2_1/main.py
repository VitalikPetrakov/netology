from application.salary import calculate_salary
from db.people import get_employees


def main():
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()
