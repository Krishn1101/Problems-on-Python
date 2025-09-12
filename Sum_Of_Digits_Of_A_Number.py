"""You are given a number n. You need to find the sum of digits of n.

Examples :

Input: n = 1
Output: 1
Explanation: Sum of digit of 1 is 1.
Input: n = 99999
Output: 45
Explanation: Sum of digit of 99999 is 45."""

                            #CODE HERE:-

class Solution:
    def sumOfDigits(self, n):
        n = str(n)
        m = 0
        for i in n:
            m+=int(i)
        return m