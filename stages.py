# Stage 3/5: Taking Turns
import random


def check_game_status():
    if len(computer_pieces) <= 0:
        return "computer win"
    elif len(player_pieces) <= 0:
        return "player win"
    else:
        snake_elements = [j for i in snake for j in i]
        if snake[0][0] == snake[-1][1] and snake_elements.count(snake[0][0]) == 8:
            return "draw"
        return None


def display():
    print("=" * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}\n")
    if len(snake) <= 6:
        for i in snake:
            print(i, end="")
    else:
        print(f"{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}")
    print("\n\nYour pieces:")
    for i in range(len(player_pieces)):
        print(f"{i + 1}:{player_pieces[i]}")
    if status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")


def player_move():
    global status
    status = "computer"
    while True:
        domino_no = input()
        if domino_no.isdigit() and int(domino_no) <= len(player_pieces) \
                or len(domino_no) == 2 and domino_no[1].isdigit() and len(domino_no[1]) <= len(player_pieces):
            break
        else:
            print("Invalid input. Please try again.")
    if domino_no == "0" and len(stock_pieces) > 0:
        player_pieces.append(stock_pieces.pop())
    elif len(domino_no) == 2:
        snake.insert(0, player_pieces.pop(int(domino_no[1]) - 1))
    elif int(domino_no) > 0:
        snake.append(player_pieces.pop(int(domino_no) - 1))


def computer_move():
    global status
    status = "player"
    input()
    k = len(computer_pieces)
    domino_no = random.choice([i for i in range(-k, k + 1)])
    if domino_no == 0 and len(stock_pieces) > 0:
        computer_pieces.append(stock_pieces.pop())
    elif domino_no < 0:
        snake.insert(0, computer_pieces.pop(abs(domino_no) - 1))
    else:
        snake.append(computer_pieces.pop(domino_no - 1))


dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
while True:
    random.shuffle(dominoes)
    stock_pieces = dominoes[:14]
    computer_pieces = dominoes[14:21]
    player_pieces = dominoes[21:]
    snake = []
    status = ""
    for i in range(6, -1, -1):
        if [i, i] in computer_pieces:
            snake.append(computer_pieces.pop(computer_pieces.index([i, i])))
            status = "player"
            break
        elif [i, i] in player_pieces:
            snake.append(player_pieces.pop(player_pieces.index([i, i])))
            status = "computer"
            break
    if snake and status:
        break
while True:
    game_status = check_game_status()
    display()
    if game_status == "computer win":
        print("Status: The game is over. The computer won!")
    elif game_status == "player win":
        print("Status: The game is over. You won!")
    elif game_status == "draw":
        print("Status: The game is over. It's a draw!")
    else:
        if status == "player":
            player_move()
        else:
            computer_move()
        continue
    break
