import random

class TicTacToe(object):
	winning_combos = (
		[0, 1, 2], [3, 4, 5], [6, 7, 8],
		[0, 3, 6], [1, 4, 7], [2, 5, 8],
		[0, 4, 8], [2, 4, 6]
		)

	outcomes = ('X-win', 'Draw', 'O-win')

	# Constructor of the class
	def __init__(self, squares = []):
		if len(squares) == 0:
			for i in range(9):
				self.squares[i] = None
		else:
			self.squares = squares

	# Shows the board
	def show(self):
		length = len(self.squares)
		for i in range(length):
			if i % 3 == 0:
				print '\n'
				print self.squares[i]
			else:
				print self.squares[i]

	# Gets the squares played by each player
	# Returns array of indices that belong to the player
	def get_squares(self, player):
		playedSquares = []
		for i in len(self.squares):
			if player == self.squares[i]:
				playedSquares.append(i)
		return playedSquares


	# All empty spaces available on the board
	# Returns an array of the indices where there is a free space
	def available_spaces(self):
		emptySpaces = []
		for i in range(len(self.squares)):
			if self.squares[i] == None:
				emptySpaces.append(i);

	# Space not taken by opponent
	def available_combos(self, opponent):
		return self.available_spaces() + self.get_squares(opponent)

	# Check if the game is complete
	# This mainly checks whether all spaces on the board have been taken
	def complete(self):
		if None not in [space for space in self.squares]:
			return True
		if self.winner():
			return True
		return False

	# Checks whether there is a winner
	# Compares the positions of squares with the winning combinations
	def winner(self):
		for player in ('X', 'O'):
			spots = self.get_squares(player)
			spots.sort()
			for combo in self.winning_combos:
				if spots == combo:
					return player
		return None

	# Allows a player to make a move
	# Places either a 'X' or an 'O' at the given position
	def make_move(self, player, position):
		self.spaces[position] = player
	
	# Returns the opponent of a given player
	# Simply returns the opposite of what is passed in as a parameter
	def get_enemy(player):
		if player == 'X':
			return 'O'
		elif player == 'O':
			return 'X'

	# Returns a boolean to notify whether or not X is the winner
	def X_won(self):
		return self.winner() == 'X'

	# Returns a boolean to notify whether or not O is the winner
	def O_won(self):
		return self.winner() == 'O'

	# Returns a boolean to notify whether or not the game is tied
	# A game is tied when the game is completed but there is no winner
	def tied(self):
		return self.complete() == True and self.winner() == None


	# The algorithm for the AI of this game
	# Alpha Beta Pruning is used to drastically improve the performance of the game
	# Each state of the game is a node. The algorithm is recursively iterated through the game states
	# With this algorithm, branches in this game tree can be ignored since the algorithm focuses on the "better"
	# parts of the tree.
	# alpha and beta are the upper and lower cutoff limits respectively
	def alphabeta(node, player, alpha, beta):
		if node.X_won():
			return -1
		elif node.tied():
			return 0
		elif node.0_won():
			return 1

		for space in node.available_spaces():
			node.make_move(player, space)
			enemy = get_enemy(player)
			value = self.alphabeta(node, enemy, alpha, beta)
			node.make_move(None, space)
			if player == 'O':
				if val > alpha:
					# upper bound increases when val is greater than alpha
					alpha = val
				if alpha >= beta:
					return beta
			else:
				if val < beta:
					# lower bound decreases when val is less than beta
					beta = val
				if beta <= alpha:
					return alpha

		if player == 'O':
			return alpha
		else:
			return beta


	def determine(board, player):
		a = -2
		choices = []
		if len(board.available_spaces()) == 9:
			return 4
		for space in board.available_spaces():
			board.make_move(player, space)
			enemy = self.get_enemy(player)
			value = self.alphabeta(board, enemy, -2, 2)
			board.make_move(None, space)
			print "move:", move + 1, "causes:", board.winners[value + 1]
			if value > a:
				a = val
				choices = [move]
			elif val == a:
				choices.append(move)
		return random.choice(choices)



