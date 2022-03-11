import random

CHOOSE = {'1':'rock', '2':'paper', '3':'scissors'}
score = 0

print('Hello, choose your figure:')


def human():
    human_choice = input("Select: \n1-Paper,\n2-Rock \n3-Scissors?\n\n")

    return CHOOSE[human_choice]


def bot():
 bot_choice = random.randint(1,3)

 return CHOOSE[bot_choice]


while score != 3:
    human = human()
    bot = bot()
    if human == 1 and bot == 3:
        score += 1
    elif human == 2 and bot == 1:
        score += 1
    else:
        score += 1

    print(score

