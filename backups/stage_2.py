# Project: Dominoes
# Stage 2/5: The Interface
import random


class Dominoes:
    def __init__(self):
        self.dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
        self.computer, self.player, self.stock, self.snake = [], [], [], []
        self.status = ""

    def start_game(self):
        while True:
            random.shuffle(self.dominoes)
            self.computer = self.dominoes[:7]
            self.player = self.dominoes[7:14]
            self.stock = self.dominoes[14:]
            for i in range(6, -1, -1):
                if [i, i] in self.player:
                    self.status = "computer"
                    self.snake.append(self.player.pop(self.player.index([i, i])))
                    break
                elif [i, i] in self.computer:
                    self.status = "player"
                    self.snake.append(self.computer.pop(self.computer.index([i, i])))
                    break
            if self.status:
                break

    def display(self):
        print("======================================================================")
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.computer)}\n")
        print(self.snake[0], "\n\nYour pieces:")
        for i in range(len(self.player)):
            print(f"{i + 1}:{self.player[i]}")

    def play(self):
        self.start_game()
        self.display()
        if self.status == "computer":
            print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        elif self.status == "player":
            print("\nStatus: It's your turn to make a move. Enter your command.")


game_1 = Dominoes()
game_1.play()
