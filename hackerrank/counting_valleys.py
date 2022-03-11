def countingValleys(steps, path):
    valley = 0
    seaLevel = 0

    for i in path:
        if i == 'D':
            seaLevel += 1
        else:
            seaLevel -= 1
        if  i == 'U' and seaLevel == 0:
            valley += 1

    return valley


#print(countingValleys(8, 'UDDDUDUU'))