import random

def mini_lotto():
    numbers = []
    for i in range(0, 5):
        numbers.append(random.randint(1, 43))
    return numbers

def lotto():
    numbers = []
    for i in range(0,6):
        numbers.append(random.randint(1,50))
    return numbers


def multi_multi():
    numbers = []
    for i in range(0, 10):
        numbers.append(random.randint(1, 81))
    return numbers
