#from numpy import argmax
class State(object):
	def __init__(self, board, action):
		self.board=board
		self.children=([])
		self.action=action
	def successors(self, player):
		moves=available_moves(self)
		for move in moves:
			new_state=State(get_new_state(self,move,player), move)
			self.children.append(new_state)
		return self.children				
def win(board, symbol):
	for i in range(3):
		#Check vertical
		if (board[i]==board[i+3]==board[i+6]) and board[i]==symbol:
			return True
		#Check horizontal
		if (board[i*3]==board[(i*3)+1]==board[(i*3)+2]) and board[i*3]==symbol:
			return True
		#Check Diagonal
		if(i==0):
			if (board[i]==board[i+4]==board[i+8]) and board[i]==symbol:
					return True
			#Check Diagonal
		if(i==2):
			if (board[i]==board[i+2]==board[i+4]) and board[i]==symbol:
					return True
	return False
def available_moves(game_board):
	moves=[]
	for i in range(len(game_board.board)):
		if game_board.board[i]==".":
			moves.append(i+1)
	return moves
def get_new_state(current, move, symbol):
	board=[]
	for i in range(len(current.board)):
		board.append(current.board[i])
	board[move-1]=symbol
	new_state=State(board, move)
	return new_state
		
def score(state, symbol):
    if win(state.board, symbol):
        return 10
    if win(state.board, opposite(symbol)):
	return -10
    else:
        return 0
    
def is_full(board):
		for e in board:
			if e == ".":
				return False
		return True
def terminal_test(state, symbol):
	if symbol=='X':
        	if win(state.board,symbol) or is_full(state.board) or win(state.board,'O'):
                        return True
		else:
			return False
        else:
                if win(state.board,symbol) or is_full(state.board) or win(state.board, 'X'):
                        return True
		else:
			return False
def opposite(symbol):
	if symbol=='X':
		return 'O'
	else:
		return 'X'
def max_value(state, symbol):
	if terminal_test(state, symbol):
            return score(state.board, symbol)
        v = -10000
        for a in available_moves(state):
            v = max(v, min_value(get_new_state(state, a, opposite(symbol))))
	return v
def min_value(state, symbol):
	if terminal_test(state, symbol):
            return score(state.board, symbol)
        v = 10000
        for a in available_moves(state):
            v = min(v, max_value(get_new_state(state, a, opposite(symbol))))
	return v

def argmax(states, symbol):
	m=-100000
	index=0
	for i in states:
		print i
		y=min_value(i,symbol)
		if (y>m):
			m=y
			index=i.action
	return index
def minimax(state,player,symbol):
	actions=available_moves(state)
    	action= argmax(state.successors(symbol),symbol)
        return actions[actions]
#	successors=state.successors(symbol)
#	action=state.action
#	if terminal_test(state.board, symbol):
#		action=state.action
#		print action, v
#		return [v,action]
 #       if player == 1:
#        	v=-100000
 #               #for i in successors:
  #              new_score=max_value(state	,opposite(symbol))
   #             if new_score[0]>v:
    ##                  	v=new_score[0]
       # else:
      #  	v=10000
              # for i in successors:
        #        new_score=min_value(state,opposite(symbol))
         #       if new_score[0]<v:
          ##		v=new_score[0]
        #return [v,action]
