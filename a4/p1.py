class NxNGrid:
	def __init__(self):
		self.grid = []	#[y][x] map of coords
		self.obs = [] #List of Tuples representing each block. 
		self.dim = 0
		
	def read(self):
		self.dim = int(raw_input())
		
		for i in range(self.dim):
			insertion = list(raw_input().strip())
			for y in range(len(insertion)):
				if (insertion[y] == "*"):
					self.obs.append((i,y))
			self.grid.append(insertion)
	
	def write(self):
		for i in self.grid:
			print(''.join(i))
		
		print(self.obs)
	
def main():
	p = NxNGrid()
	p.read()
	p.write()

	
	
if __name__ == "__main__":
	main()
