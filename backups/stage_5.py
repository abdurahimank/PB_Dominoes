# Project: Dominoes
# Stage 5/5: The AI
import random


class Dominoes:
    def __init__(self):
        self.dominoes = [[i, j] for i in range(7) for j in range(i, 7)]
        self.computer, self.player, self.stock, self.snake = [], [], [], []
        self.next_player, self.status = "", ""

    def start_game(self):
        while True:
            random.shuffle(self.dominoes)
            self.computer = self.dominoes[:7]
            self.player = self.dominoes[7:14]
            self.stock = self.dominoes[14:]
            for i in range(6, -1, -1):
                if [i, i] in self.player:
                    self.next_player = "computer"
                    self.snake.append(self.player.pop(self.player.index([i, i])))
                    break
                elif [i, i] in self.computer:
                    self.next_player = "player"
                    self.snake.append(self.computer.pop(self.computer.index([i, i])))
                    break
            if self.next_player:
                break

    def display(self):
        print("=" * 70)
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.computer)}\n")
        if len(self.snake) <= 6:
            print(*self.snake, "\n\nYour pieces:")
        else:
            print(*self.snake[:3], "...", *self.snake[-3:], "\n\nYour pieces:", sep="")
        for i in range(len(self.player)):
            print(f"{i + 1}:{self.player[i]}")

    def game_status(self):
        if len(self.computer) == 0:
            self.status = "Status: The game is over. The computer won!"
        elif len(self.player) == 0:
            self.status = "Status: The game is over. You won!"
        elif self.snake[0][0] == self.snake[-1][1]:
            if [i for j in self.snake for i in j].count(self.snake[0][0]) == 8:
                self.status = "Status: The game is over. It's a draw!"
        return self.status

    def legal_move(self, player, domino_pos):
        if domino_pos == 0:
            return True
        elif domino_pos < 0 and self.snake[0][0] in player[abs(domino_pos) - 1]:
            if player[abs(domino_pos) - 1][1] != self.snake[0][0]:
                player.insert(abs(domino_pos) - 1, (lambda x: [x[1], x[0]])(player.pop(abs(domino_pos) - 1)))
            return True
        elif domino_pos > 0 and self.snake[-1][1] in player[domino_pos - 1]:
            if player[domino_pos - 1][0] != self.snake[-1][1]:
                player.insert(domino_pos - 1, (lambda x: [x[1], x[0]])(player.pop(domino_pos - 1)))
            return True
        return False

    def computer_domino_score(self):
        dominoes = [j for i in self.snake + self.computer for j in i]
        score_dict = {}
        for i in self.computer:
            score_dict[tuple(i)] = dominoes.count(i[0]) + dominoes.count(i[1]) if i[0] != i[1] else dominoes.count(i[0])
        dominoes_list = []
        for i in sorted(score_dict.items(), key=lambda x: x[1], reverse=True):
            dominoes_list.append(list(i[0]))
        return dominoes_list

    def computer_move(self):
        dominoes = self.computer_domino_score()
        # print(self.computer, dominoes)  # test
        for i in dominoes:
            domino_pos = self.computer.index(i) + 1
            # print("test 1: ", self.computer)  # test
            if self.legal_move(self.computer, -1 * domino_pos):
                # print("test 2: ", self.computer)  # test
                self.snake.insert(0, self.computer.pop(domino_pos - 1))
                break
            elif self.legal_move(self.computer, domino_pos):
                self.snake.append(self.computer.pop(domino_pos - 1))
                break
        else:
            if len(self.stock) > 0:
                self.computer.append(self.stock.pop(0))

    def player_move(self):
        while True:
            try:
                domino_pos = int(input())
                if -len(self.player) <= domino_pos <= len(self.player):
                    if self.legal_move(self.player, domino_pos):
                        break
                    print("Illegal move. Please try again.")
                    continue
                raise ValueError
            except ValueError:
                print("Invalid input. Please try again.")
        if domino_pos == 0 and len(self.stock) > 0:
            self.player.append(self.stock.pop(0))
        elif domino_pos < 0:
            self.snake.insert(0, self.player.pop(abs(domino_pos) - 1))
        else:
            self.snake.append(self.player.pop(domino_pos - 1))

    def play(self):
        self.start_game()
        while self.status == "":
            self.display()
            if self.next_player == "computer":
                input("\nStatus: Computer is about to make a move. Press Enter to continue...")
                self.computer_move()
                self.next_player = "player"
            elif self.next_player == "player":
                print("\nStatus: It's your turn to make a move. Enter your command.")
                self.player_move()
                self.next_player = "computer"
            self.game_status()
        self.display()
        print(self.status)


game_1 = Dominoes()
game_1.play()
