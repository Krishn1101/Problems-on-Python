"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false"""

                        #CODE HERE:-

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        l = 0
        r = rows*cols - 1
        
        while l<=r:
            mid = (l+r)//2
            i = mid//cols
            j = mid%cols
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                r = mid - 1
            else:
                l = mid + 1
        return False