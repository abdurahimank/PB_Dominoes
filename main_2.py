import random


class Domino:
    dominoes = [[i, j] for i in range(0, 7) for j in range(0, i + 1)]

    def __init__(self):
        self.player, self.computer, self.stock, self.snake = [], [], [], []
        self.next_move, self.status = '', ''  # next_move takes only two values ('player' or 'computer')

    def start_game(self):
        for i in range(6, 0, -1):
            if [i, i] in self.computer:
                self.next_move = 'player'
                self.snake.append(self.computer.pop(self.computer.index([i, i])))
                return True
            elif [i, i] in self.player:
                self.next_move = 'computer'
                self.snake.append(self.player.pop(self.player.index([i, i])))
                return True
        return None

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
            else:
                print('Invalid input. Please try again.')
                continue
            break

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
            else:
                continue
            break

    def game_status(self):
        if len(self.player) == 0:
            return '\nStatus: The game is over. You won!'
        elif len(self.computer) == 0:
            return '\nStatus: The game is over. The computer won!'
        elif self.snake[0][0] == self.snake[-1][1] and \
                sum([1 for i in self.snake for j in i if self.snake[0][0] == j]) == 8:
            return "\nStatus: The game is over. It's a draw!"
        else:
            return 'not finished'

    def display(self):
        print('=' * 70)
        print(f'Stock size: {len(self.stock)}')
        print(f'Computer pieces: {len(self.computer)}\n')
        if len(self.snake) <= 6:
            for i in range(len(self.snake)):
                print(self.snake[i], end='')
        else:
            print(f'{self.snake[0]}{self.snake[1]}{self.snake[2]}...{self.snake[-3]}{self.snake[-2]}{self.snake[-1]}')
        print('\n\nYour pieces:')
        for i in range(len(self.player)):
            print(f'{i + 1}:{self.player[i]}')

    def play(self):
        while True:
            random.shuffle(Domino.dominoes)
            self.player = Domino.dominoes[0:7]
            self.computer = Domino.dominoes[7:14]
            self.stock = Domino.dominoes[14:]
            if not self.start_game():
                continue
            else:
                while self.status == 'not finished' or self.status == '':
                    self.display()
                    if self.next_move == 'player':
                        self.player_move()
                    else:
                        self.computer_move()
                    self.status = self.game_status()
                self.display()
                print(self.status)
            break


domino_game = Domino()
domino_game.play()
