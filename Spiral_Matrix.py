"""Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]"""

                    #CODE HERE:-

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        total = n*m
        ans = []
        cnt = 0

        rowstart = 0
        colstart = 0
        rowend = n-1
        colend = m-1

        while cnt<total:
            #rowstart, colstart->colend
            for i in range(colstart,colend+1):
                ans.append(matrix[rowstart][i])
                cnt+=1
            rowstart+=1

            if cnt == total:
                break
            
            #colend, rowstart->rowend
            for i in range(rowstart,rowend+1):
                ans.append(matrix[i][colend])
                cnt+=1
            colend-=1

            if cnt == total:
                break
            
            #rowend, colend->colstart
            for i in range(colend,colstart-1,-1):
                ans.append(matrix[rowend][i])
                cnt+=1
            rowend-=1

            if cnt == total:
                break

            #colstart, rowend->rowstart
            for i in range(rowend,rowstart-1,-1):
                ans.append(matrix[i][colstart])
                cnt+=1
            colstart+=1

        return ans