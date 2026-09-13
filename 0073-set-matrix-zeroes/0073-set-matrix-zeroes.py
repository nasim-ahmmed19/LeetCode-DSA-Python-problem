class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        r_t=[0 for _ in range(row)]
        c_t=[0 for _ in range(col)]
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==0:
                    r_t[i]=-1
                    c_t[j]=-1
        for i in range(0,row):
            for j in range(0,col):
                if r_t[i]==-1 or c_t[j]==-1:
                    matrix[i][j]=0



        