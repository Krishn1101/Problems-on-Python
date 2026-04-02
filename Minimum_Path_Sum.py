"""Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12"""

                                                            #CODE HERE:-

class Solution:
    def minPathSum(self,grid):
        n = len(grid)
        m = len(grid[0])

        for j in range(1,m):
            grid[0][j]+=grid[0][j-1]

        for j in range(1,n):
            grid[j][0]+=grid[j-1][0]

        for i in range(1,n):
            for j in range(1,m):
                top = grid[i-1][j]
                left = grid[i][j-1]

                grid[i][j] += min(top,left)
        
        return grid[n-1][m-1]