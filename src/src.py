from datetime import datetime


def timeprocessing(some_func):
    # декоратор для вывода длительности операции
    timing = False

    def inner(*args, **kwargs):
        nonlocal timing
        if timing == False:
            timing = True
            t = datetime.now()
            result = some_func(*args, **kwargs)
            print(f"Accomplished in {datetime.now()-t} seconds")
            return result
        return some_func(*args, **kwargs)
    return inner
