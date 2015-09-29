def win(board, symbol):
	for i in range(3):
		#Check vertical
		if board[i]==board[i+3]==board[i+6] and board[i]==symbol:
			return True
		#Check horizontal
		if board[i*3]==board[(i*3)+1]==board[(i*3)+2] and board[i*3]==symbol:
			return True
		#Check Diagonal
		if(i==0):
			if board[i]==board[i+4]==board[i+8] and board[i]==symbol:
					return True
			#Check Diagonal
		if(i==2):
			if board[i]==board[i+2]==board[i+4] and board[i]==symbol:
					return True
	return False
def available_moves(game_board):
	moves=[]
	for i in range(len(game_board)):
		if game_board[i]==".":
			moves.append(i+1)
	return moves
def get_new_state(board, move, symbol):
	new_state=[]
	for i in range(len(board)):
		new_state.append(board[i])
	new_state[move-1]=symbol
	return new_state
		
def score(board, symbol):
    if win(board, symbol):
        return 10
    if symbol=='X':
    	if win(board, 'O'):
        	return -10
    elif symbol=='O':
	if win(board,'X'):
		return -10
    else:
        return 0
    
def is_full(board):
		for e in board:
			if e == ".":
				return False
		return True
def minimax(board,player,symbol):
	moves = available_moves(board)
	action=1
        if win(board,symbol) or is_full(board):
		return [score(board,symbol),action]
        if player == 1:
        	v=-100000
                for move in moves:
                        newboard=get_new_state(board,move,'X')
                        new_score=minimax(newboard, 2,'O')[0]
                        if new_score>v:
                        	action=move
                        	v=new_score
        else:
        	v=1000000
                for move in moves:
                        newboard=get_new_state(board,move,'O')
                        new_score=minimax(newboard, 1,'X')[0]
                        if new_score<v:
                        	action=move
                        	v=new_score
        return [v,action]
