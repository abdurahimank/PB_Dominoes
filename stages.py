# Stage 1/5: Setting Up the Game
import random


dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
while True:
    random.shuffle(dominoes)
    stock_pieces = dominoes[:14]
    computer_pieces = dominoes[14:21]
    player_pieces = dominoes[21:]
    domino = ""
    status = ""
    for i in range(6, -1, -1):
        if [i, i] in computer_pieces:
            domino = [[i, i]]
            computer_pieces.remove([i, i])
            status = "player"
            break
        elif [i, i] in player_pieces:
            domino = [[i, i]]
            player_pieces.remove([i, i])
            status = "computer"
            break
    if domino and status:
        break

print(f"Stock pieces:  {stock_pieces}")
print(f"Computer pieces: {computer_pieces}")
print(f"Player pieces: {player_pieces}")
print(f"Domino snake: {domino}")
print(f"Status: {status}")
