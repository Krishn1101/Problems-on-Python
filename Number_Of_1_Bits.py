"""Given a positive integer n. Your task is to return the count of set bits.

Examples:

Input: n = 6
Output: 2
Explanation: Binary representation is '110', so the count of the set bit is 2.
Input: n = 8
Output: 1
Explanation: Binary representation is '1000', so the count of the set bit is 1.
Input: n = 3
Output: 2"""

                                        #CODE HERE:-

class Solution:
	def setBits(self, n):
		s = bin(n)[2:]
		cnt = 0
		for i in s:
			if i == '1':
				cnt+=1
		return cnt