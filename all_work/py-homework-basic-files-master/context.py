from datetime import datetime


class TimeManager:

    def __init__(self):
        self.time_in = datetime.now()
        for i in range(1000):
            print(i ** i)

    def __enter__(self):
        self.time_out = datetime.now()
        self.delta = self.time_out - self.time_in
        return self.time_in, self.time_out, self.delta

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with TimeManager() as a:
    print(a[0].strftime("%Y-%m-%d-%H.%M.%S"))
    print(a[1].strftime("%Y-%m-%d-%H.%M.%S"))
    print(a[2])
