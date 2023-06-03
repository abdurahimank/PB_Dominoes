# Project: Dominoes
# Stage 1/5: Setting Up the Game
import random


dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
# print(dominoes)
# print(len(dominoes))
while True:
    random.shuffle(dominoes)
    # print(dominoes)
    computer = dominoes[:7]
    player = dominoes[7:14]
    stock = dominoes[14:]
    snake = []
    status = ""
    for i in range(6, -1, -1):
        if [i, i] in player:
            status = "computer"
            snake.append(player.pop(player.index([i, i])))
            break
        elif [i, i] in computer:
            status = "player"
            snake.append(computer.pop(computer.index([i, i])))
            break
    if status:
        break
print(f"Stock pieces: {stock}")
print(f"Computer pieces: {computer}")
print(f"Player pieces: {player}")
print(f"Domino snake: {snake}")
print(f"Status: {status}")
