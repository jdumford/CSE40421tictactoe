
class State(object):
	def __init__(self, board, action):
		self.board=board
		self.children=([])
		self.action=action
		self.score=0
	def successors(self, player):
		moves=available_moves(self)
		for move in moves:
			new_state=get_new_state(self,move,player)
			self.children.append((move, new_state))
		return self.children				
def win(state, symbol):
	for i in range(3):
		#Check vertical
		if (state.board[i]==state.board[i+3]==state.board[i+6]) and state.board[i]==symbol:
			return True
		#Check horizontal
		if (state.board[i*3]==state.board[(i*3)+1]==state.board[(i*3)+2]) and state.board[i*3]==symbol:
			return True
		#Check Diagonal
		if(i==0):
			if (state.board[i]==state.board[i+4]==state.board[i+8]) and state.board[i]==symbol:
					return True
			#Check Diagonal
		if(i==2):
			if (state.board[i]==state.board[i+2]==state.board[i+4]) and state.board[i]==symbol:
					return True
	return False
def available_moves(state):
	moves=[]
	for i in range(len(state.board)):
		if state.board[i]==".":
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
    if win(state, symbol):
        return 10
    if win(state, opposite(symbol)):
	return -10
    else:
        return 0
    
def is_full(state):
		for e in state.board:
			if e == ".":
				return False
		return True
def terminal_test(state, symbol):
	if win(state,symbol) or is_full(state) or win(state,opposite(symbol)):
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
            return score(state, symbol)
        v = -10000
        for a in available_moves(state):
            v = max(v, min_value(get_new_state(state, a, symbol), symbol))
	return v
def min_value(state, symbol):
	if terminal_test(state, symbol):
            return score(state, symbol)
        v = 10000
        for a in available_moves(state):
            v = min(v, max_value(get_new_state(state, a, symbol),  symbol))
	return v
def argmin(seq, fn):
    """Return an element with lowest fn(seq[i]) score; tie goes to first one.
    >>> argmin(['one', 'to', 'three'], len)
    'to'
    """
    best = seq[0]; best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best
def argmax(seq, fn):
	return argmin(seq, lambda x: -fn(x))
def minimax(state,player,symbol):
	actions=state.successors(symbol)
	for i in actions:
		if win(i[1], symbol):
			return i[0]
	action, state = argmax(state.successors(symbol),
                           lambda ((a, s)): min_value(s, symbol))
    	#action= argmax(state.successors(symbol),symbol)
        return action
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
