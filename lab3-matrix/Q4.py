class game0fLife:

    def __init__(self,nrows,ncols):
        self.array=[0]*nrows
        for i in range(nrows):
            self.array[i]=[0]*ncols

    def numrows(self):
        return len(self.array)

    def numcols(self):
        return len(self.array[0])

    def print2d(self):
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                print(self.array[i][j],end=" ")
            print("")

    def configure(self,coordList):
        for p,q in coordList:
            self.array[p][q]=1
        self.print2d()

    def clearCell(self,rows,cols):
        if (rows <= len(self.array) and cols<= len(self.array[0])):
            self.array[rows][cols] = 0
        else:
            print("Enter a valid row/column value")

    def setCell(self,rows,cols):
        if (rows <= len(self.array) and cols<= len(self.array[0])):
            self.array[rows][cols] = 1
        else:
            print("Enter a valid row/column value")

    def isLiveCell(self,rows,cols):
        if (rows <= len(self.array) and cols<= len(self.array[0])):
            l=self.array[row][col] == 1
            return l
        else:
            print("Enter a valid row/column value")

    def numLiveNeighbors(self ,rows, cols):
        trav = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        count = 0
        for x,y in trav:
            if(0<=rows+x<len(self.array) and 0<=cols+y<len(self.array[0]) and self.array[rows+x][cols+y]==1):
                count=count+1
        return count

    def start(self,rows,cols):
        count = self.numLiveNeighbors(rows,cols)
        if(self.array[rows][cols]==1):
            if 2<=count<=3:
                return 1
            else:
                return 0
        else:
            if count == 3:
                return 1
            else:
                return 0

    def final_solution(self):
        c=0
        while c!=10:
            for i in range(len(self.array)):
                for j in range(len(self.array[0])):
                    self.array[i][j]=self.start(i,j)
            
            c = c + 1
        print("Final")
        self.print2d()       

tmp = game0fLife(3,4)
tmp.configure([(0,0),(0,1),(2,2),(1,0)])
tmp.final_solution()