# Stage 2/5: The Interface
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

print("=" * 70)
print(f"Stock size: {len(stock_pieces)}")
print(f"Computer pieces: {len(computer_pieces)}")
print(f"\n{domino[0]}\n")
print("Your pieces:")
for i in range(len(player_pieces)):
    print(f"{i + 1}:{player_pieces[i]}")
if status == "computer":
    print("\nStatus: Computer is about to make a move. Press Enter to continue...")
else:
    print("\nStatus: It's your turn to make a move. Enter your command.")