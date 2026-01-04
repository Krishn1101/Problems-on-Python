"""Given a string s. Your task is to remove the vowels from the string.

Examples:

Input: s = "welcome to geeksforgeeks"
Output: "wlcm t gksfrgks"
Explanation: Vowels were ignored only consonents were returned in the same order.
Input: s = "what is your name ?"
Output: wht s yr nm ?"""

                                #CODE HERE:-

#User function Template for python3
class Solution:
	def removeVowels(self, s):
		ans = ""
		for i in s:
			if i not in "aeiou":
				ans+=i
		return ans