"""Given two strings denoting non-negative numbers s1 and s2. Calculate the sum of s1 and s2.

Examples:

Input: s1 = "25", s2 = "23"
Output: "48"
Explanation: The sum of 25 and 23 is 48.
Input: s1 = "2500", s2 = "23"
Output: "2523"
Explanation: The sum of 2500 and 23 is 2523.
Input: s1 = "2", s2 = "3"
Output: "5"
Explanation: The sum of 2 and 3 is 5."""

                                        #CODE HERE:-

class Solution:
	def findSum(self, s1, s2):
		import sys
		sys.set_int_max_str_digits(10000)
		a = int(s1)
		b = int(s2)
		return(a+b)