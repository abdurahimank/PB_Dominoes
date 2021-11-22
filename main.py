import random


def dom_select(computer, player):
    com_double = [x for x in computer if x[0] == x[1]]
    pla_double = [x for x in player if x[0] == x[1]]
    if len(com_double) == 0 and len(pla_double) == 0:
        return "no_double"
    elif len(com_double) == 0:
        return ["computer", max(pla_double)]
    elif len(pla_double) == 0:
        return ["player", max(com_double)]
    else:
        if max(com_double) > max(pla_double):
            return ["player", max(com_double)]
        else:
            return ["computer", max(pla_double)]


dominoes = [[x, y] for x in range(0, 7) for y in range(x, 7)]

# domino_snake
while True:
    random.shuffle(dominoes)
    player_pieces= dominoes[:7]
    computer_pieces = dominoes[7:14]
    stock_pieces = dominoes[14:]
    status = dom_select(computer_pieces, player_pieces)
    if status == "no_double":
        continue
    else:
        if status[0] == "computer":
            player_pieces.remove(status[1])
            break
        else:
            computer_pieces.remove(status[1])
            break

print(f"Stock pieces: {stock_pieces}")
print(f"Computer pieces: {computer_pieces}")
print(f"Player pieces: {player_pieces}")
print(f"Domino snake: {[status[1]]}")
print(f"Status: {status[0]}")
