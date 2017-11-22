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
            
    def printEndState(self):
        winner = 'NONE'
        validlines = [(1,0), (0,1), (1,1), (-1, 0), (0,-1), (-1, -1), (-1, 1), (1, -1)]
        Owin, Xwin, Draw = 0,0,0

        Draw = 1
        for i in self.board:
            if '-' in i:
                Draw = 0

        #Check the X axis
        for i in self.board:
            for y in range(0,3):
                peice = i[y]
                if (peice != '-' and
                    peice == i[y+1] and
                    peice == i[y+2] and
                    peice == i[y+3]):
                    winner = peice
                    #print("left-right")


                    #Check the Y axis
        for y in range(2):
            for x in range(6):
                peice = self.board[y][x]
                if (peice != '-' and
                    peice == self.board[y+1][x] and
                    peice == self.board[y+2][x] and
                    peice == self.board[y+3][x]):
                    winner = peice
                    #print("up-down")


        for i in range(0,3):
            for y in range(0,4):
                peice = self.board[i][y]
                #print(peice, i, y)
                if (peice != '-' and
                    peice == self.board[i+1][y+1] and
                    peice == self.board[i+2][y+2] and
                    peice == self.board[i+3][y+3]):
                    winner = peice
                    #print("down-right")

        for i in range(3,6):
            for y in range(0,3):
                peice = self.board[i][y]
                if (peice != '-' and
                    peice == self.board[i-1][y+1] and
                    peice == self.board[i-2][y+2] and
                    peice == self.board[i-3][y+3]):
                    winner = peice
                    #print("up-right")

        if (winner != 'NONE'):
            if winner == 'X': Xwin = 1
            else: Owin = 1


            
            
        
        



        print('has4 O : {0}\nhas4 X : {1}\nfull : {2}'.format(Owin, Xwin, Draw))
            
                


def main():
    game = ConnectFour()
    game.read()
    #game.write()
    game.printEndState()
        



if __name__ == "__main__":
    main()
        
