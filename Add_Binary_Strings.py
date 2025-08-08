"""Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110"""

                                                        #CODE HERE:-
                                                    
#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		a = int(s1,2)
		b = int(s2,2)
		ans = a+b
		ans = bin(ans)
		return ans[2:]