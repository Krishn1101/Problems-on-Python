"""Given an array arr[] of size n consisting of distinct integers from 1 to n. Your task is to sort the array without using extra space
Challenge: Try to solve it using linear time complexity.

Examples: 

Input: [2, 1, 5, 4, 3]
Output: [1, 2, 3, 4, 5]
Input: [1, 2, 3, 4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]
Input: [1]
Output: [1]"""

                                                            #CODE HERE:-

class Solution:
    def sortArray(self, arr):
        arr.sort()
        return arr