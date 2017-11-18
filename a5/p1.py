class ConnectFour:
	def __init__(self):
		self.players = {'X':1,'O':2}
		#Make and array of arrays. Format = board[x][y] starting from top left
		self.board = []
		

	def read(self):
		self.gamename, self.currentPlayer = input().split() #Fill the first two lines
		#Fill up the board
		for y in range(6):
			line = input()
			self.board.append(list(line.strip()))
		
	def write(self):
		#Format and Output
		print('{0} {1}'.format(self.gamename, self.currentPlayer))
		for i in range(len(self.board)):
			print(''.join(self.board[i]))
		
		
		


def main():
	game = ConnectFour()
	game.read()
	game.write()



if __name__ == "__main__":
	main()
	