"""Given a number S. Check whether it is divisble by 11 or not.

Example 1:

Input:
S = 76945
Output: 1
Explanation: The number is divisible by 11
as 76945 % 11 = 0.

â€‹Example 2:

Input: 
S = 12
Output: 0
Explanation: The number is not divisible
by 11 as 12 % 11 = 1."""

                        #CODE HERE:-

class Solution:
	def divisibleBy11(self, S):
		if int(S)%11==0:
			return 1
		else:
			return 0