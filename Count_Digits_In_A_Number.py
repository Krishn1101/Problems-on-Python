"""You are given a number n. You need to find the count of digits in n.

Examples :

Input: n = 1
Output: 1
Explanation: Number of digit in 1 is 1.
Input: n = 99999
Output: 5
Explanation: Number of digit in 99999 is 5"""

                        #CODE HERE:-

class Solution:
    def countDigits(self, n):
        n = str(n)
        return (len(n))