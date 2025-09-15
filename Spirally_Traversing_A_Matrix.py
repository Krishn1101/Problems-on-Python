"""You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

Examples:

Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Explanation: 

Input: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
Explanation: Applying same technique as shown above.
Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]
Explanation: Applying same technique as shown above, output will be [32, 44, 27, 23, 62, 50, 28, 54]."""

                                                     #CODE HERE:-

class Solution:
    def spirallyTraverse(self, mat):
        n = len(mat)
        m = len(mat[0])
        total = n*m
        rowstart,colstart = 0,0
        rowend = n-1
        colend = m-1
        cnt=0
        arr=[]
        while(cnt<total):
            for i in range(colstart,colend+1):
              arr.append(mat[rowstart][i])
              cnt+=1
            rowstart+=1
            
            if cnt == total:
                break
            
            for i in range(rowstart,rowend+1):
                arr.append(mat[i][colend])
                cnt+=1
            colend-=1
            
            if cnt == total:
                break
            
            for i in range(colend,colstart-1,-1):
                arr.append(mat[rowend][i])
                cnt+=1
            rowend-=1
            
            if cnt == total:
                break
            
            for i in range(rowend,rowstart-1,-1):
                arr.append(mat[i][colstart])
                cnt+=1
            colstart+=1
            
            if cnt == total:
                break
        return arr