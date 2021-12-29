import random


class Domino:

    def __init__(self):
        self.dominoes = []
        while True:
            for i in range(7):
                for j in range(i, 7):
                    self.dominoes.append([i, j])
            random.shuffle(self.dominoes)
            self.player = self.dominoes[:7]
            self.computer = self.dominoes[7:14]
            self.stock = self.dominoes[14:]
            self.snake = [[6, 6]]
            self.next_move = ""
            self.count = 0
            self.domino = 0
            for i in range(5, -1, -1):
                if self.snake[0] in self.player:
                    self.player.remove(self.snake[0])
                    self.next_move = "computer"
                    break
                if self.snake[0] in self.computer:
                    self.computer.remove(self.snake[0])
                    self.next_move = "player"
                    break
                self.snake = [[i, i]]
            else:
                continue
            break

    def status(self):
        if len(self.player) == 0:
            return "Status: The game is over. You won!"
        elif len(self.computer) == 0:
            return "Status: The game is over. The computer won!"
        else:
            if self.snake[0][0] == self.snake[-1][1]:
                for i in self.snake:
                    for j in i:
                        if self.snake[0][0] == j:
                            self.count += 1
            return "Status: The game is over. It's a draw!" if self.count == 8 else None

    def player_move(self):
        while True:
            try:
                self.domino = int(input("\nStatus: It's your turn to make a move. Enter your command."))
            except ValueError:
                print("\nInvalid input. Please try again.")
                continue
            if abs(self.domino) > len(self.player):
                print("\nInvalid input. Please try again.")
                continue
            break
        if self.domino == 0:
            choice = random.choice(self.stock)
            self.stock.remove(choice)
            self.player.append(choice)
        elif self.domino < 0:
            self.snake.insert(0, self.player[abs(self.domino) - 1])
            self.player.remove(self.player[abs(self.domino) - 1])
        else:
            self.snake.append(self.player[self.domino - 1])
            self.player.remove(self.player[abs(self.domino) - 1])

    def computer_move(self):
        any_key = input("\nStatus: Computer is about to make a move. Press Enter to continue...")
        self.domino = random.choice([i for i in range(-len(self.computer), len(self.computer))])
        if self.domino == 0:
            choice = random.choice(self.stock)
            self.stock.remove(choice)
            self.computer.append(choice)
        elif self.domino < 0:
            self.snake.insert(0, self.computer[abs(self.domino) - 1])
            self.computer.remove(self.computer[abs(self.domino) - 1])
        else:
            self.snake.append(self.computer[self.domino - 1])
            self.computer.remove(self.computer[abs(self.domino) - 1])

    def play(self):
        while True:
            print("=" * 70)
            print(f"Stock size: {len(self.stock)}")
            print(f"Computer pieces: {len(self.computer)}\n")
            if len(self.snake) <= 6:
                for i in self.snake:
                    print(i, end="")
            else:
                print(f"{self.snake[0]}{self.snake[1]}{self.snake[2]}...", end="")
                print(f"{self.snake[-3]}{self.snake[-2]}{self.snake[-1]}")
            print(end='\n')
            print(f"\nYour pieces:")
            for i in range(len(self.player)):
                print(f"{i + 1}:{self.player[i]}")
            if self.status() is None:
                if self.next_move == "player":
                    self.player_move()
                    self.next_move = "computer"
                else:
                    self.computer_move()
                    self.next_move = "player"
                continue
            else:
                print(self.status())
                break


dom = Domino()
dom.play()
