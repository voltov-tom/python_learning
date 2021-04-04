def type_logger(func):
    def logger(*args, **kvargs):
        t = func(*args, **kvargs)
        print(func.__name__, (*args, type(t)))
        return t

    return logger


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3)
