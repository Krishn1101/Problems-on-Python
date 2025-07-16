"""Given a number n, find the value of n raised to the power of its own reverse.
Note: The result will always fit into a 32-bit signed integer.

Examples:

Input: n = 2
Output: 4
Explanation: The reverse of 2 is 2, and 22 = 4.
Input: n = 10
Output: 10
Explanation: The reverse of 10 is 1 (leading zero is discarded), and 101 = 10."""

                                    #CODE HERE:-

class Solution:
    def reverse_exponentiation(self, n):
        pwr = str(n)
        pwr = pwr[::-1]
        pwr = int(pwr)
        return(n**pwr)