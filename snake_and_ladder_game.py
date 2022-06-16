import random

ladder = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
}

# Snake : Jump down
snake = {
    17: 7,
    30: 2,
    54: 34,
    62: 19,
    64: 60,
    72: 55,
    87: 36,
    93: 73,
    95: 75,
    98: 79
}

position1 = 0
position2 = 0


def move(pos):
    dice = random.randint(1, 6)
    print(f"Dice:{dice}")
    pos = int(pos + dice)
    if pos in snake:
        print("Bitten by snake")
        pos = snake[pos]
        print(f"Position:{pos}")
        print("\n")
    if pos in ladder:
        print("Climbed ladder")
        pos = ladder[pos]
        print(f"Position:{pos}")
        print("\n")
    else:
        print(f"Position:{pos}")
        print("\n")
    return pos


while True:
    player1 = input("Player 1 press Enter ")
    position1 = move(position1)
    if position1 == 100:
        print("Game Over!!! \nPlayer 1 wins")
        break

    player2 = input("Player 2 press Enter ")
    position2 = move(position2)
    if position2 == 100:
        print("Game Over!!! \nPlayer 2 wins")
        break