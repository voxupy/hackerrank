import random
from collections import Counter

#n - ile jest skarpet
#x - ile jest kolorów skarpet

#zadanie polega na wpisaniu ile jest skarpet oraz ile kolorów.
#Polega na sparowaniu skarpet i policzeniu ile faktycznie jest par

def sales_by_match(n, x):
    list = []
    for item in range(n):
        list.append(random.randint(1,x))

    c = Counter(list)
    pair = 0

    for i in c.values():
        int(i/2)
        pair += 1

    return pair

sales_by_match(12,4)