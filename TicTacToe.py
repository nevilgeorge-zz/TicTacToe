class TicTacToe(object):
	winning_combos = (
		[0, 1, 2], [3, 4, 5], [6, 7, 8],
		[0, 3, 6], [1, 4, 7], [2, 5, 8],
		[0, 4, 8], [2, 4, 6]
		)

	outcomes = ('X-win', 'Draw', 'O-win')

	# Constructor of the class
	def __init__(self, squares = []):
		if (len(squares) == 0):
			for i in range(9):
				self.squares[i] = None
		else:
			self.squares = squares

	# Shows the board
	def show(self):
		length = len(self.squares)
		for i in range(length):
			if (i % 3 == 0):
				print '\n'
				print self.squares[i]
			else:
				print self.squares[i]

	# All empty spaces available on the board
	# Returns an array of the indices where there is a free space
	def available_spaces(self):
		emptySpaces = []
		for i in range(len(self.squares)):
			if (self.squares[i] == None):
				emptySpaces.append(i);

	