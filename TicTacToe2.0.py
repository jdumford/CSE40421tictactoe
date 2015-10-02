import random
def mark_board(board, player, location):
    gridlist = list(board)# get the board as a list
    gridlist[location] = player# set the board location to the player symbol.
    return ''.join(gridlist)# return the grid list as a string
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
    return row == [row[0]] * 3 # Return true if all three elements are equal.

def can_win(board,combos,player): # Determines if a winning move can be played.
    win_move=[]
    for c in combos:
        if board[c[0]]==board[c[1]] and board[c[0]]==player: # if two in the same combo are equal
            if board[c[2]]=='.': # and there is an empty cell in between the two
                win_move.append(c[2]) # Add the winning move to the list of winning moves
		winning_combo=c
        if board[c[0]]==board[c[2]] and board[c[0]]==player:
            if board[c[1]]=='.':
                win_move.append(c[1])
		winning_combo=c
        if board[c[1]]==board[c[2]] and board[c[1]]==player:
            if board[c[0]]=='.':
		winning_combo=c
                win_move.append(c[0])
    return win_move
def available_moves(board):
    moves=[]
    b=list(board)
    for i in range(9):
        if b[i]=='.': # if the cell has a dot it is empty.
            moves.append(i) # add it to the list of available moves

    return moves # Return available moves

def terminal_test(board):
    if winner(board):
        return True
    return available_moves(board) == [] #if available moves is empty or there is a winner return true.

def x_won(board):
    return winner(board) == 'X' # Winner returns the symbol of the winner

def o_won(board):
    return winner(board) == 'O'

def draw(board):
    return terminal_test(board) and winner(board) is None

def opponent(player):# Switch who is playing
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

def minimax(board, player, alpha, beta):# minimax with alpha beta pruning
    if terminal_test(board):
        return score(board)
    best = None
    for move in available_moves(board):
        new_board = mark_board(board, player, move)
        if player == 'O':
	    val=alpha
            val2 = minimax(new_board, opponent(player),val,beta)
	    if val2 > val:#val2> alpha
		val=val2 # val 2 is new alpha
            if val > beta:
                return beta #val should be less than beta
            return val
        else:
	    val=beta
            val2 = minimax(new_board, opponent(player),alpha,val)
	    if val2 < val:
		val=val2
            if val < alpha:
                return alpha
	    return val

def is_empty(board):# checks to see if the board is empty
    for i in board:
        if i!='.':
            return False
    return True
def best_move(board, player):
    a = 0
    choices = []
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
    possible_win=can_win(board,combos,player)# if the player can win it should
    if possible_win!=[]:
        return possible_win[0]#Return any winning move
    for move in available_moves(board):
        new_board = mark_board(board, player, move)
        if player=='X':
            if x_won(new_board):
                return move #If the next move is a winning move return that move
                win=1
        else:
            if o_won(new_board):
                return move
                win=1
        val = minimax(new_board, opponent(player),-999,999)#call minimax with initial alpha beta of -inf to inf
        if player == 'X':
            if val > a:#Val is a better move than a
                a = val
                choices = [move]#add move to choices
            elif val== a:
                choices.append(move)# if val is comparable to a add move to choices
        elif player =='O':
            if val>a:
                a=val
                choices=[move]
            elif val==a:
                choices.append(move)
        if 1:#if the opponent can win block that move before making a non-winning move of your own.
            for move in available_moves(board):
                opponent_board=mark_board(board,opponent(player), move)
                if player=='X':
                    if o_won(opponent_board):
                        return move
                else:
                    if x_won(opponent_board):
                        return move
    if choices != []:#if there are good available moves
        return random.choice(choices)
    else:#otherwise just make any available move
        return available_moves[0]

def get_input(board, turn):
    while True:
    	move = input('Move #%d enter choice for player 1: ' % (turn))
    	if move-1 in available_moves(board):
        	return move
	else:
		print "Invalid move"
    


class Tic_Tac_Toe(object):
    def __init__(self, grid=''):
        if grid:
            self.grid = grid
        else:
            self.grid = '.'*9#board of 9 dots initially
        self._currentTurn = 'O'#First turn is O
        self.move_cnt=0 # initialize move count.

    def nextTurn(self):
        if self._currentTurn == 'X':
            self._currentTurn = 'O'
        else:
            self._currentTurn = 'X'
        self.move_cnt=self.move_cnt+1# increment move count when the turn changes.

    def play(self):
        agents=int(input("Enter choice (1 for single agent, 2 for dual agents):"))# enter the number of agents
        print
        display(self.grid)#print the grid.
        print 
        if agents==1:
	    corners=[0,2,6,8]#holds the values of remaining corner spaces.
            while not terminal_test(self.grid):
                if self._currentTurn == 'O':
                    move = get_input(self.grid, self.move_cnt+1)
                    move=move-1
		    if move in corners:#remove any taken corners
			corners.remove(move)
                    self.grid = mark_board(self.grid, self._currentTurn, move)
                    print 
                elif self._currentTurn == 'X':
                    if self.move_cnt==1 and list(self.grid)[4]=='.':#always mark in the middle if it is open.
			move=4
		    elif self.move_cnt<=3 and list(self.grid)[4]=='O':#block the corners if the first player has marked in the middle
			move=random.choice(corners)
			for moves in available_moves(self.grid):#Make sure to block the opponents winning moves.
                		opponent_board=mark_board(self.grid,'O', moves)
                    		if o_won(opponent_board):
                        		move=moves
			corners.remove(move)
		    else:# This hierarchy of moves is repeated for any ai move
                    	move=best_move(self.grid, self._currentTurn)
                    print 'Move #%d enter choice for player 2: %d' % (self.move_cnt+1, move+1)
                    print
                    self.grid = mark_board(self.grid, self._currentTurn, move)

                self.nextTurn()
                display(self.grid)
                print
        if agents==2:
	    corners=[0,2,6,8]
            while not terminal_test(self.grid):
                if self._currentTurn == 'O':
                    move=best_move(self.grid, self._currentTurn)
		    if move in corners:
			corners.remove(move)
                    print 'Move #%d enter choice for player 1: %d' % (self.move_cnt+1, move+1)
                    print
                    self.grid = mark_board(self.grid, self._currentTurn, move)
                elif self._currentTurn == 'X':
		    if self.move_cnt==1 and list(self.grid)[4]=='.':
			move=4
		    elif self.move_cnt<=3 and list(self.grid)[4]=='O':
			move=random.choice(corners)
			for moves in available_moves(self.grid):
                		opponent_board=mark_board(self.grid,'O', moves)
                    		if o_won(opponent_board):
                        		move=moves
			corners.remove(move)
		    else:
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
