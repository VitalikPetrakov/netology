class NegativeAge(Exception):
    pass
print("Program started")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise NegativeAge("Exception: Negative age!")
    print("Success!")
except NegativeAge as e:
    print(e)
print("Program finished")

