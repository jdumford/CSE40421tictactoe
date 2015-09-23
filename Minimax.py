def win(board, symbol):
	for i in range(3):
		#Check vertical
		if self.board[i]==self.board[i+3]==self.board[i+6] and self.board[i]==symbol:
			return True
		#Check horizontal
		if self.board[i*3]==self.board[(i*3)+1]==self.board[(i*3)+2] and self.board[i*3]==symbol:
			return True
		#Check Diagonal
		if(i==0):
			if self.board[i]==self.board[i+4]==self.board[i+8] and self.board[i]==symbol:
					return True
			#Check Diagonal
		if(i==2):
			if self.board[i]==self.board[i+2]==self.board[i+4] and self.board[i]==symbol:
					return True
	return False
def available_moves(game_board):
	moves=([])
	for i in range(len(game_board.board)):
		if game_board.board[i]==".":
			moves.append(i)
	return moves
def get_new_state(board, move, symbol):
	new_state=board
	new_state[move]=symbol
	return new_state
		
def score(board, symbol, opponent):
    if win(board, symbol):
        return 10
    elsif win(board, opponent):
        return -10
    else
        return 0
    
def is_full(board):
		for e in board:
			if e == ".":
				return False
		return True
def Max_value(board)
	return score(board) if win(board,symbol) or is_full(board)
	v=-100000
	moves=available_moves(board)
	symbol='X'
	for move in moves:
		v=max(v,Min_value(generate_new_state(board, move, symbol))
	return v
def Min_value(board)
	return score(board) if win(board,symbol) or is_full(board)
	v=100000
	moves=available_moves(board)
	symbol='O'
	for move in moves:
		v=min(v,Max_value(generate_new_state(board, move, symbol))
	return v
def minimax(board,player):
	action=-1
        return [score(board),action] if win(board,symbol) or is_full(board)
        moves = available_moves(board)
        if player == 1:
        	v=-100000
                for move in moves:
                        newboard=generate_new_state(board,move,"X")
                        new_score=minimax(newboard, 2)
                        if (new_score>v):
                        	action=move
                        	v=new_score
        else:
        	v=1000000
                for move in moves:
                        newboard=generate_new_state(board,move,"O")
                        new_score=minimax(newboard, 1)
                        if (new_score<v):
                        	action=move
                        	v=new_score
        return [v,action]
