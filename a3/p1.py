


class Puzzle:
    def __init__(self):
        # create the data that we want to store.
        self.puzzleName = ''
        self.puzzleState = [] #List of a bunch of lists. So accessing the data will be puzzleState[i][j]
                              #where i is the row, and j is the column
        
    def read(self):
        #First line containes the Puzzle Name, Width, Height, ID of marked, Offset
        #eg puzzle1 4 5 X 1
        #Exit width is the width of the marked block
        line = raw_input().split()
        self.puzzleName = line[0]
        self.dims = (int(line[1]), int(line[2]))
        self.marked = line[3]
        self.offset = int(line[4])
        
        #Next is a series of lines that represent other blocks in the puzzle [a-z]
        #eg a X X b
        #eg a X X b
        #eg c d d e
        #eg c f g e
        #eg h - - i
        for i in range(self.dims[1]):
            self.puzzleState.append(map(str, list(raw_input())))
            
        
        #Empty cells are marked with '-'
    def write(self):
        print(self.puzzleName + ' '+ str(self.dims[0]) +' '+ str(self.dims[1]) +' '+ self.marked +' '+ str(self.offset))
        for i in range(self.dims[1]):
            print(''.join(self.puzzleState[i]))
        
        #output to stdout the current state of the puzzle in the above format


def main():
    puzzle = Puzzle()
    puzzle.read()
    puzzle.write()



if __name__ == '__main__':
    main()
    
