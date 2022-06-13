import random


class Domino:
    def __init__(self):
        self.computer, self.player, self.stock, self.snake = [], [], [], []
        self.next_move, self.status = '', ''  # next_move takes only two values ('player' or 'computer')
        self.dominoes = [[i, j] for i in range(7) for j in range(i, 7)]

    def start_game(self):
        for i in range(6, -1, -1):
            if [i, i] in self.player:
                self.snake.append(self.player.pop(self.player.index([i, i])))
                self.next_move = "computer"
                return True
            elif [i, i] in self.computer:
                self.snake.append(self.computer.pop(self.computer.index([i, i])))
                self.next_move = "player"
                return True
        return False

    def display(self):
        print("=" * 70, f"Stock size: {len(self.stock)}", f"Computer pieces: {len(self.computer)}", sep="\n")
        print("\n", *self.snake, "\n", sep="") if len(self.snake) <= 6 \
            else print("\n", *self.snake[0:3], "...", *self.snake[-3:], "\n", sep="")
        print('Your pieces:')
        for i in range(len(self.player)):
            print(f"{i + 1}:{self.player[i]}")

    def rule_2(self):  # AI for selecting domino for computer
        dominoes = [j for i in self.snake + self.computer for j in i]
        dic = {'0': dominoes.count(0), '1': dominoes.count(1), '2': dominoes.count(2), '3': dominoes.count(3),
               '4': dominoes.count(4), '5': dominoes.count(5), '6': dominoes.count(6)}
        point_table = {}
        for i in self.computer:
            if i[0] != i[1]:
                point_table[tuple(i)] = dic[str(i[0])] + dic[str(i[1])]
            else:
                point_table[tuple(i)] = int((dic[str(i[0])] + dic[str(i[1])]) / 2)
        domino_list = []
        for i in sorted([(value, list(key)) for (key, value) in point_table.items()], reverse=True):
            domino_list.append(self.computer.index(i[1]) + 1)
            domino_list.append(-(self.computer.index(i[1]) + 1))
        domino_list.append(0)
        return domino_list

    def rule_1(self, domino):  # The specified side should have matching number and also reorganize the slide
        if domino == '0':
            return True
        elif domino[0] == '-' and self.snake[0][0] in [i for i in eval('self.' + self.next_move)[int(domino[1]) - 1]]:
            if self.snake[0][0] != eval('self.' + self.next_move)[int(domino[1]) - 1][1]:
                x = eval('self.' + self.next_move)[int(domino[1]) - 1]
                eval('self.' + self.next_move)[int(domino[1]) - 1] = [x[1], x[0]]
        elif domino[0] != '-' and self.snake[-1][1] in [i for i in eval('self.' + self.next_move)[int(domino) - 1]]:
            if self.snake[-1][1] != eval('self.' + self.next_move)[int(domino) - 1][0]:
                x = eval('self.' + self.next_move)[int(domino) - 1]
                eval('self.' + self.next_move)[int(domino) - 1] = [x[1], x[0]]
        else:
            return False
        return True

    def player_move(self):
        print("\nStatus: It's your turn to make a move. Enter your command.")
        while True:
            domino = input()
            if (domino.isdigit() or (domino[0] == '-' and domino[1].isdigit())) \
                    and abs(int(domino)) <= len(self.player):
                if self.rule_1(domino):
                    if domino == '0' and len(self.stock) != 0:
                        self.player.append(self.stock.pop(self.stock.index(random.choice(self.stock))))
                    elif domino[0] == '-':
                        self.snake.insert(0, self.player.pop(int(domino[1]) - 1))
                    else:
                        self.snake.append(self.player.pop(int(domino) - 1))
                    self.next_move = 'computer'
                else:
                    print('Illegal move. Please try again.')
                    continue
                break
            else:
                print('Invalid input. Please try again.')

    def computer_move(self):
        red_1 = input('\nStatus: Computer is about to make a move. Press Enter to continue...')
        for i in self.rule_2():
            domino = i
            if self.rule_1(str(domino)):
                if domino == 0 and len(self.stock) != 0:
                    self.computer.append(self.stock.pop(self.stock.index(random.choice(self.stock))))
                elif domino < 0:
                    self.snake.insert(0, self.computer.pop(abs(int(domino)) - 1))
                else:
                    self.snake.append(self.computer.pop(int(domino) - 1))
                self.next_move = 'player'
                break

    def game_status(self):
        if len(self.player) == 0:
            return "Status: The game is over. You won!"
        elif len(self.computer) == 0:
            return "Status: The game is over. The computer won!"
        elif self.snake[0][0] == self.snake[-1][1] and [j for i in self.snake for j in i].count(self.snake[0][0]) >= 8:
            return "Status: The game is over. It's a draw!"
        else:
            return "not finished"

    def play(self):
        while True:

            random.shuffle(self.dominoes)
            self.computer = self.dominoes[:7]
            self.player = self.dominoes[7:14]
            self.stock = self.dominoes[14:]
            if self.start_game():
                break
        while self.status == 'not finished' or self.status == '':
            self.display()
            if self.next_move == 'player':
                self.player_move()
            else:
                self.computer_move()
            self.status = self.game_status()
        self.display()
        print(self.status)


game = Domino()
game.play()
