"""Given a non-negative integer N. Check whether the Binary Representation of the number is Palindrome or not. 
Note: No leading 0's are being considered.

Example 1:

Input:
N = 5
Output: 1
Explanation: The Binary Representation of
5 is 101 which is a Palindrome.

Example 2:

Input: 
N = 10
Output: 0
Explanation: The Binary Representation of
10 is 1010 which is not a Palindrome."""

                                            #CODE HERE:-

#User function Template for python3
class Solution:
	def binaryPalin (self, N):
		s = bin(N)
		s = s[2:]
		k = s
		k = k[::-1]
		if s==k:
			return 1
		else:
			return 0