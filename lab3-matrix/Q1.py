class Array2D:
    def __init__(self,nrows,ncols):
        self.rows = [0]*nrows 
        for i in range( nrows ) :
            self.rows[i] = [0]*( ncols )


    def numRows(self):
        return len(self.rows)
    
    def numCols(self):
        return len(self.rows[0])

    def clear(self,value):
        c = self.numCols()
        self.rows = [value]*self.numRows()
        for i in range( self.numRows() ) :
            self.rows[i] = [value]*(c)
        return self
    
    def getitem(self,i1,i2):
        if 0<=i1<self.numRows() and 0<=i2<self.numCols():
            g = self.rows[i1][i2]
            return g
        else:
            return print("Invalid idex numbers.")
    
    def setitem(self,i1,i2,value):
        if 0<=i1<self.numRows() and 0<=i2<self.numCols():
            self.rows[i1][i2] = value
            return ""
        else:
            return print("Invalid index numbers.")

    
    def print2d( self ):
        for i in range( len(self.rows )):
            for j in range( len(self.rows[0]) ):
                print(self.rows[i][j],end=" ")
            print("")
        return("")
        




arr1 = Array2D(3,5)
arr1.print2d()

