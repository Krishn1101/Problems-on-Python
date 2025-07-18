"""Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

Examples:

Input: n = 3
Output: 6
Explanation: For n = 3, the sum will be 6. 1 + 2 + 3 = 6.
Input: n = 5
Output: 15
Explanation: For n = 5, the sum will be 15. 1 + 2 + 3 + 4 + 5 = 15."""

                                                                #CODE HERE:-

class Solution:
    def findSum(self, n):
        sm=0
        for i in range(n+1):
            sm+=i
        return sm