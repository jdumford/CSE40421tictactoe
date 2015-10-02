import random
def mark_board(board, player, location):
    gridlist = list(board)
    gridlist[location] = player
    return ''.join(gridlist)
def display(board):
    new_board=list(board)
    for i in range(len(new_board)):
	   print board[i],
	   if ((i+1)%3)==0:
		  print
winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]


def winner(board):
    for row in winning_combos:
        if (board[row[0]] != '.') and (equal([board[i] for i in row])):
            return board[row[0]]

def equal(row):
    return row == [row[0]] * 3

def can_win(board,combos,player):
    win_move=[]
    for c in combos:
        if board[c[0]]==board[c[1]] and board[c[0]]==player:
            if board[c[2]]=='.':
                win_move.append(c[2])
        if board[c[0]]==board[c[2]] and board[c[0]]==player:
            if board[c[1]]=='.':
                win_move.append(c[2])
        if board[c[1]]==board[c[2]] and board[c[1]]==player:
            if board[c[0]]=='.':
                win_move.append(c[0])
    return win_move
def available_moves(board):
    moves=[]
    b=list(board)
    for i in range(9):
        if b[i]=='.':
            moves.append(i)

    return moves

def terminal_test(board):
    if winner(board):
        return True
    return available_moves(board) == []

def x_won(board):
    return winner(board) == 'X'

def o_won(board):
    return winner(board) == 'O'

def draw(board):
    return terminal_test(board) and winner(board) is None

def opponent(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def score(board):
    if x_won(board):
        return -1
    elif o_won(board):
        return 1
    elif draw(board):
        return 0

def minimax(board, player):
    if terminal_test(board):
        return score(board)
    best = None
    for move in available_moves(board):
        new_board = mark_board(board, player, move)
        val = minimax(new_board, opponent(player))
        if player == 'O':
            if best is None or val > best:
                best = val
        else:
            if best is None or val < best:
                best = val
    return best
def is_empty(board):
    for i in board:
        if i!='.':
            return False
    return True
def best_move(board, player):
    a =-2
    win=0
    choices = []
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
    possible_win=can_win(board,combos,player)
    if possible_win!=[]:
        return possible_win[0]
    if is_empty(board):
        return 4
    print available_moves(board)
    for move in available_moves(board):
        new_board = mark_board(board, player, move)
        if player=='X':
            if x_won(new_board):
                return move
                win=1
        else:
            if o_won(new_board):
                return move
                win=1
        val = minimax(new_board, opponent(player))
        if player == 'X':
            if val > a:
                a = val
                choices = [move]
            elif val== a:
                choices.append(move)
        elif player =='O':
            if val>a:
                a=val
                coices=[move]
            elif val==a:
                choices.append(move)
        if 1:
            for move in available_moves(board):
                opponent_board=mark_board(board,opponent(player), move)
                if player=='X':
                    if o_won(opponent_board):
                        return move
                else:
                    if x_won(opponent_board):
                        return move
    if choices != []:
        return random.choice(choices)
    else:
        return available_moves[0]

def get_input(board, turn):
    move = input('Move #%d enter choice for player 1: ' % (turn))
    if move-1 not in available_moves(board):
        print 'Invalid move'
        get_input(board, turn)
    else:
        return move
    


class Tic_Tac_Toe(object):
    def __init__(self, grid=''):
        if grid:
            self.grid = grid
        else:
            self.grid = '.'*9
        self._currentTurn = 'O'
        self.move_cnt=0

    def nextTurn(self):
        if self._currentTurn == 'X':
            self._currentTurn = 'O'
        else:
            self._currentTurn = 'X'
        self.move_cnt=self.move_cnt+1

    def play(self):
        agents=int(input("Enter choice (1 for single agent, 2 for dual agents):"))
        print
        display(self.grid)
        print 
        if agents==1:
            while not terminal_test(self.grid):
                if self._currentTurn == 'O':
                    move = get_input(self.grid, self.move_cnt+1)
                    move=move-1
                    self.grid = mark_board(self.grid, self._currentTurn, move)
                    print 
                elif self._currentTurn == 'X':
                    move=best_move(self.grid, self._currentTurn)
                    print 'Move #%d enter choice for player 2: %d' % (self.move_cnt+1, move+1)
                    print
                    self.grid = mark_board(self.grid, self._currentTurn, move)

                self.nextTurn()
                display(self.grid)
                print
        if agents==2:
            while not terminal_test(self.grid):
                if self._currentTurn == 'O':
                    move=best_move(self.grid, self._currentTurn)
                    print 'Move #%d enter choice for player 1: %d' % (self.move_cnt+1, move+1)
                    print
                    self.grid = mark_board(self.grid, self._currentTurn, move)
                elif self._currentTurn == 'X':
                    move=best_move(self.grid, self._currentTurn)
                    print 'Move #%d enter choice for player 2: %d' % (self.move_cnt+1, move+1)
                    print
                    self.grid = mark_board(self.grid, self._currentTurn, move)

                self.nextTurn()
                display(self.grid)
                print
        if winner(self.grid)=='X': 
            print 'Player 2 has won'
        elif winner(self.grid)=='O':
            print 'Player 1 has won'
        else:
            print 'The game is a tie'

game = Tic_Tac_Toe()
game.play()
