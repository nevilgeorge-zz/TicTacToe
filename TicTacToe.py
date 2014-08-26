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