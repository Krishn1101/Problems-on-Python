"""Check if the given string S is a Panagram or not. A pangram is a sentence containing every letter in the English Alphabet.

Example 1:

Input: S = "Pack mY box witH fIve dozen 
            liquor jugs"
Output: 1
Explanation: Given string contains all 
English Alphabets. 
Example 2:

Input: S = "geeksFORgeeks"
Output: 0
Explanation: Given string does not contain 
all English Alphabets."""

                                                        #CODE HERE:-

#User function Template for python3
class Solution:
	def isPanagram(self, S):
		S = S.lower()
		ans = "abcdefghijklmnopqrstuvwxyz"
		fin_ans = ""
		for i in S:
			if 97<=ord(i)<=122:
				if i not in fin_ans:
					fin_ans+=i
		for i in ans:
			if i not in fin_ans:
				return 0
		return 1