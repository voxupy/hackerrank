list = [6,4,3,2,1,8,8,3,1]


def bubble_sort(list):
    indexing_length = len(list) - 1
    swap = 0
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,indexing_length):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
                swap += 1


    print('Array is sorted in', swap, 'swaps.')
    print('First Element:', list[0])
    print('Last Element:', list[-1])


bubble_sort(list)
