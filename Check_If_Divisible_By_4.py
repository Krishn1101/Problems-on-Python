"""Given a number N. Check whether it is divisble by 4.

Example 1:

Input:
N = 1124
Output: 1
Explanation: The number is divisible by 4
as 1124 % 4 = 0.

â€‹Example 2:

Input: 
N = 7
Output: 0
Explanation: The number is not divisibly by
4 as 7 % 4 = 3."""

                #CODE HERE:-

class Solution:
	def divisibleBy4 (self, N):
		if int(N)%4==0:
			return 1
		else:
			return 0