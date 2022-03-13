def descending_order(num):
    num1 = str(num)
    list = []
    for i in num1:
        list.append(i)

    list.sort(reverse=True)
    return "".join(list)
