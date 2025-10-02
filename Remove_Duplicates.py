"""Given a string s without spaces, the task is to remove all duplicate characters from it, keeping only the first occurrence.

Note: The original order of characters must be kept the same. 

Examples :

Input: s = "zvvo"
Output: "zvo"
Explanation: Only keep the first occurrence
Input: s = "gfg"
Output: "gf"
Explanation: Only keep the first occurrence"""

                                                                #CODE HERE:-

class Solution:
	def removeDups(self, s):
		s1 = s
		s2 = ""
		s1 = set(s1)
		for i in s:
			if (i in s1) and (i not in s2):
				s2 += i
		return s2