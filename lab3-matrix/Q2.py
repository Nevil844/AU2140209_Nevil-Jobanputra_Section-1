class Sparse2D():

    def __init__(self, nrows, ncols):
        self.rows = nrows
        self.cols = ncols
        self.sparse = list()
        arr = list()
        for i in range(nrows):
            arr.append([0]*ncols)
        self.matrix = arr
        self.normal()

    def setNonZeroes(self,nzList): 
        self.sparse = nzList
        self.normal()

    def normal(self):
        if(len(self.sparse)>=1):
            for i in self.sparse:
                self.matrix[i[0]][i[1]] = i[2]
    
    
    def numRows(self):
        return self.rows

    def numCols(self):
        return self.cols

    def clear(self,value):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = value

    def getitem(self,i,j):
        if(i in range(self.rows) and j in range(self.cols)):
            g= self.matrix[i][j]
            return g

    def setitem(self,i,j,value):
        if(i in range(self.rows) and j in range(self.cols)):
            self.matrix[i][j] = value

    def showMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end = " ")
            print()
    
    def showSparse(self):
        if (len(self.sparse)>=1):
            for i in self.sparse:
                print(i[0],i[1],i[2])
        else:
            print("No non-zero values present")

arr2d = Sparse2D(4,6)
arr2d.setNonZeroes([[0,0,1],[1,1,7],[2,4,8],[3,0,4]])

print("Sparse Version:")
arr2d.showSparse()
print()
print("Original Version:")
arr2d.showMatrix()