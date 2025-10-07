"""Given a positive number n. Find the sum of all the digits of n.

Examples:

Input: n = 687
Output: 21
Explanation: Sum of 687's digits: 6 + 8 + 7 = 21
Input: n = 12
Output 3
Explanation: Sum of 12's digits: 1 + 2 = 3"""

                            #CODE HERE:-

class Solution:
    def sumOfDigits(self, n):
        s = str(n)
        sm = 0
        for i in s:
            sm+=int(i)
        return sm