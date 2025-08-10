"""Given three integers x, n, and M, compute (x^n) % M, i.e., the remainder when x raised to the power n is divided by M.

Examples:

Input: x = 3, n = 2, M = 4
Output: 1
Explanation: 32 % 4 = 9 % 4 = 1.
Input: x = 2, n = 6, M = 10
Output: 4
Explanation: 26 % 10 = 64 % 10 = 4."""

                                                            #CODE HERE:-

class Solution:
	def powMod(self, x, n, M):
	    return(pow(x,n,M))