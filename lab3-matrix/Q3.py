class Matrix():

    def __init__(self,nrows,ncols):
        self.rows = nrows
        self.cols = ncols
        matrix = list()
        for i in range(nrows):
            matrix.append([2]*ncols)

        self.matrix = matrix

    def numRows(self):
        return self.rows

    def numCols(self):
        return self.cols

    def getitem(self,i,j):
        if(i in range(self.rows) and j in range(self.cols)):
            g=self.array2d[i][j]
            return g

    def setitem(self,i,j,scalar):
        if(i in range(self.rows) and j in range(self.cols)):
            self.array2d[i][j] = scalar

    def scaleBy(self,scalar):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = self.matrix[i][j]*scalar

    def transpose(self):
        transpose = list()
        for i in range(self.cols):
            newRow = list()
            for j in self.matrix:
                newRow.append(j[i])
            transpose.append(newRow)
        
        return transpose

    def add(self,rhsMatrix):
        if(len(rhsMatrix)==self.rows and len(rhsMatrix[0])==self.cols):
            newMatrix = list([[0]*self.cols]*self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    newMatrix[i][j] = self.matrix[i][j] + rhsMatrix[i][j]
            return newMatrix

    def subtract(self,rhsMatrix):
        if(len(rhsMatrix)==self.rows and len(rhsMatrix[0])==self.cols):
            newMatrix = list([[0]*self.cols]*self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    newMatrix[i][j] = self.matrix[i][j] - rhsMatrix[i][j]
            return newMatrix    

    def multiply(self,rhsMatrix):
        if(self.cols==len(rhsMatrix)):
            newMatrix = list([[0]*len(rhsMatrix[0])]*self.rows)
            
            for i in range(self.rows):
                curr_row = self.matrix[i]

                for j in range(len(rhsMatrix[0])):
                    
                    summ = 0
                    for k in range(self.rows):
                        summ = summ + (curr_row[k]*rhsMatrix[k][j])
                    newMatrix[i][j] = summ

            return newMatrix

a = Matrix(2, 2)
b = Matrix(2, 2)

print(a.multiply(b.matrix))

print(a.add(b.matrix))

print(a.subtract(b.matrix))

print(a.scaleBy(2))

print(b.transpose())
