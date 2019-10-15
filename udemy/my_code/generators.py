from random import choice
from string import ascii_lowercase as letters


def random_email(length, domains):
    name = ''.join(choice(letters) for _ in range(length))
    return name + '@' + choice(domains)


def random_email_list(name_length, domains, list_length):
    return [random_email(name_length, domains) for _ in range(list_length)]
