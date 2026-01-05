"""Given a string S, the task is to create a string with the first letter of every word in the string.
 

Example 1:

Input: 
S = "geeks for geeks"
Output: gfg

Example 2:

Input: 
S = "bad is good"
Output: big"""

                                            #CODE HERE:-

class Solution:
	def firstAlphabet(self, S):
		p = S.split()
		t = ""
		for i in p:
			t+=i[0]
		return t