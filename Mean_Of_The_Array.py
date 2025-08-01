"""Given an unsorted array arr[], the task is to find the mean of the array. 

Note: Return the floor value of the mean.

Examples:


Input: arr[] = [1, 3, 4, 2, 6, 5, 8, 7]
Output: 4
Explanation: Sum of the elements is 1 + 3 + 4 + 2 + 6 + 5 + 8 + 7 = 36, Mean = 36/8 = 4

Input: arr[] = [4, 4, 4, 4, 4]
Output: 4
Explanation: Sum of the elements is 4 + 4 + 4 + 4 + 4 = 20, Mean = 20/5 = 4"""

                                #CODE HERE:-

class Solution:
    def findMean(self, arr):
        sm = sum(arr)
        ans = sm//len(arr)
        return ans