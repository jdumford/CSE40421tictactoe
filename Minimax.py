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
		
def score(board, symbol, opponent)
    if win(board, symbol)
        return 10
    elsif win(board, opponent)
        return -10
    else
        return 0
    end
end
