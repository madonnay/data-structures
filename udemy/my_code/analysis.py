import time


def analyze_func(func, *args):
    tic = time.time()
    return_values = func(*args)
    toc = time.time()
    duration = toc - tic
    message = f"{func.__name__.capitalize()} -> Duration: {duration:.5f} seconds"
    return return_values, message
