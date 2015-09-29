import sys
import Minimax
class Game_Board:
	"""Tic Tac Toe board"""
	def __init__(self):
		self.board=[".",".",".",".",".",".",".",".","."]
		self.p1=[]
		self.p2=[]
	def display_board(self):
		for i in range(len(self.board)):
			print self.board[i],
			if ((i+1)%3)==0:
				print
	def mark_board(self, place, player):
		if place>9 or place<1:
			return False
		else:
			if player==2 :
				if self.empty_cell(place-1):
					self.board[place-1]="X"
					self.p1.append(place)
				else:
					return False
			else:
				if self.empty_cell(place-1):
					self.board[place-1]="O"
					self.p2.append(place)
				else:
					return False
			return True
	def is_empty(self):
		for e in self.board:
			if e != ".":
				return False
		return True
	def is_full(self):
		for e in self.board:
			if e == ".":
				return False
		return True
	def empty_cell(self,i):
		if self.board[i]==".":
			return True
		else:
			return False
	def check_win(self):
		for i in range(3):
			#Check vertical
			if self.board[i]==self.board[i+3]==self.board[i+6] and self.board[i]!=".":
				return True
			#Check horizontal
			if self.board[i*3]==self.board[(i*3)+1]==self.board[(i*3)+2] and self.board[i*3]!=".":
				return True
			#Check Diagonal
			if(i==0):
				if self.board[i]==self.board[i+4]==self.board[i+8] and self.board[i]!=".":
					return True
			#Check Diagonal
			if(i==2):
				if self.board[i]==self.board[i+2]==self.board[i+4] and self.board[i]!=".":
					return True
		return False
		
num_players= int(input('Enter the number of AI players: '))
x = Game_Board()
x.display_board
state=Minimax.State(x.board, 0)
if num_players==1:
	while True:
		if x.is_empty():
			player = 1
		if player==1:
			place = int(input("What spot would you like to mark: "))
		elif player==2:
			result=Minimax.minimax(state, 2, 'X')
			place=result[1]
			print place
		if x.mark_board(place, player)==False:
			print "Invalid move, Choose again"
		
		else:
			print "Player %d has marked %d: " % (player, place)
			state=Minimax.State(x.board, place)
			if x.check_win():
				if player==1:
					x.display_board()
					print "Player 1 wins!"
					sys.exit()
				else:
					x.display_board()
					print "Player 2 wins!"
					sys.exit()
			if player==1:
				player=2
			else:
				player=1
		
		x.display_board()
		if x.is_full():
			print "The game is a draw"
			sys.exit()

else:
	while True:
		if x.is_empty():
			player = 1
		if player==1:
			place = Minimax.minimax(state, 1,'O')[1]
		elif player==2:
			place=Minimax.minimax(state, 1, 'X')[1] 
		if x.mark_board(place, player)==False:
			print "Invalid move, Choose again"
		
		else:
			print "Player %d has marked %d: " % (player, place)
		if x.check_win():
			if player==1:
				x.display_board()
				print "Player 1 wins!"
				sys.exit()
			else:
				x.display_board()
				print "Player 2 wins!"
				sys.exit()
		if player==1:
			player=2
		else:
			player=1
		x.display_board()
		if x.is_full():
			print "The game is a draw"
			sys.exit()
		
