import time
from random import choice
from string import ascii_lowercase as letters


def bisection_iter(target, array):
    start = 0
    stop = len(array) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if target == array[mid]:
            return mid, f"{target} found at index {mid}"
        elif target < array[mid]:
            stop = mid - 1
        else:
            start = mid + 1
    return None, f"{target} not found in list"


def analyze_func(func, *args):
    tic = time.time()
    return_values = func(*args)
    toc = time.time()
    duration = toc - tic
    message = f"{func.__name__.capitalize()} -> Duration: {duration:.5f} seconds"
    return return_values, message


def random_email(length, domains):
    name = ''.join(choice(letters) for _ in range(length))
    return name + '@' + choice(domains)


def random_email_list(name_length, domains, list_length):
    return [random_email(name_length, domains) for _ in range(list_length)]
