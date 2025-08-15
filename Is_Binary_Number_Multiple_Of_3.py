"""You are given a binary number as a string of characters ('0' and '1'). Your task is to determine whether this binary number is divisible by 3. 
Note: Try to accomplish this using a single traversal of the input binary string.

Examples:

Input: s = "100"
Output: false
Explanation: "100"'s decimal equivalent is 4, which is not divisible by 3.
Input: s = "0011"
Output: true
Explanation: "0011" is 3, which is divisible by 3.
Input: s = "110"
Output: true
Explanation: The decimal equivalent of "110" is 6, which is divisible by 3."""

                                                            #CODE HERE:-

#User function Template for python3
class Solution:
	def isDivisible(self, s):
		ans = int(s,2)
		if(ans%3==0):
			return True
		else:
			return False