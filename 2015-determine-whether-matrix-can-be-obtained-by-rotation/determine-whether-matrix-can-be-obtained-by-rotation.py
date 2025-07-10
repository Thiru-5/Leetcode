class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n=len(mat)
            for i in range(n):
                for j in range(i,n):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            for k in mat:
                k.reverse()

        for i in range(4):
            if mat==target:
                return True
            rotate(mat)
        return False
        