"""Given N, find s such that sum of first s natural number is N.
 

Example 1:

Input: N = 10
Output: 4
Explanation: Sum of first 4 natural
number is 1 + 2 + 3 + 4 = 10.     
Example 2:

Input: N = 17
Output: -1
Explanaion: There is no such number."""

                        #CODE HERE:-

#User function Template for python3

class Solution:
	def find(self, n):
		sm=0
		cnt = 0
		i = 1
		while(sm<=n):
			sm += i
			cnt+=1
			if sm == n:
				return cnt
			else:
				i+=1
		return -1