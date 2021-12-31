import random


class Domino:
    def __init__(self):
        self.dominoes = []
        self.next_move = ""
        self.count = 0
        self.domino = 0
        while True:
            for i in range(7):
                for j in range(i, 7):
                    self.dominoes.append([i, j])
            random.shuffle(self.dominoes)
            self.player = self.dominoes[:7]
            self.computer = self.dominoes[7:14]
            self.stock = self.dominoes[14:]
            self.snake = [[6, 6]]
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
                self.count = 0
                for i in self.snake:
                    for j in i:
                        if self.snake[0][0] == j:
                            self.count += 1
            return "Status: The game is over. It's a draw!" if self.count == 8 else None

    def legal_move(self, turn):
        if self.domino == 0:
            return "not good"
        slide = turn[abs(self.domino) - 1]
        if self.domino < 0:
            if slide[1] == self.snake[0][0]:
                return "good"
            elif slide[0] == self.snake[0][0]:
                turn[abs(self.domino) - 1] = [slide[1], slide[0]]
                return "good"
            else:
                return "not good"
        else:
            if slide[0] == self.snake[-1][1]:
                return "good"
            elif slide[1] == self.snake[-1][1]:
                turn[abs(self.domino) - 1] = [slide[1], slide[0]]
                return "good"
            else:
                return "not good"

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
            if self.legal_move(self.player) == "not good" and self.domino != 0:
                print("Illegal move. Please try again.")
                continue
            break
        if self.domino == 0:
            if len(self.stock) != 0:
                choice = random.choice(self.stock)
                self.stock.remove(choice)
                self.player.append(choice)
        elif self.domino < 0:
            self.snake.insert(0, self.player[abs(self.domino) - 1])
            self.player.remove(self.player[abs(self.domino) - 1])
        else:
            self.snake.append(self.player[self.domino - 1])
            self.player.remove(self.player[abs(self.domino) - 1])

    def domino_score(self, snake, computer):
        num_score = {i: 0 for i in range(7)}
        snake_comp = [j for i in (snake + computer) for j in i]
        for i in snake_comp:
            for k in range(7):
                if k == i:
                    num_score[k] += 1
        # print(num_score)  # for testing
        # To find score for dominoes in computer inventory
        domino_rank = []
        domino_rank = sorted([f"{num_score[i[0]] + num_score[i[1]]}{i[0]}{i[1]}" for i in computer], reverse=True)
        return [[int(i[1]), int(i[2])] if len(i) == 3 else [int(i[2]), int(i[3])] for i in domino_rank]

    def computer_move(self):
        any_key = input("\nStatus: Computer is about to make a move. Press Enter to continue...")
        computer_list = [i for j in self.computer for i in j]
        # Below code is used to directly go to skipping if there are no legal moves
        if self.snake[0][0] not in computer_list and self.snake[-1][1] not in computer_list:
            if len(self.stock) != 0:
                choice = random.choice(self.stock)
                self.stock.remove(choice)
                self.computer.append(choice)
        # Method - 1
        # The domino is found by highest score method
        else:
            domino_ranked = self.domino_score(self.snake, self.computer)
            for i in domino_ranked:
                if self.snake[0][0] == i[0]:
                    self.snake.insert(0, [i[1], i[0]])
                elif self.snake[0][0] == i[1]:
                    self.snake.insert(0, i)
                elif self.snake[-1][1] == i[0]:
                    self.snake.append(i)
                elif self.snake[-1][1] == i[1]:
                    self.snake.append([i[1], i[0]])
                else:
                    continue
                self.computer.remove(i)
                break

        '''
        # Method - 2
        # The domino is found by random choice subject to other conditions
        else:
            legal_list = []
            for i in self.computer:
                if self.snake[0][0] == i[0] or self.snake[0][0] == i[1]:
                    legal_list.append(i)
                    continue
                if self.snake[-1][1] == i[0] or self.snake[-1][1] == i[1]:
                    legal_list.append(i)
                    continue
            choice = random.choice(legal_list)
            self.computer.remove(choice)
            if choice[0] == self.snake[0][0]:
                self.snake.insert(0, [choice[1], choice[0]])
            elif choice[1] == self.snake[0][0]:
                self.snake.insert(0, choice)
            elif choice[0] == self.snake[-1][1]:
                self.snake.append(choice)
            else:
                self.snake.append([choice[1], choice[0]])'''

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
