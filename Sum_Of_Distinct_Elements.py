"""You are given an array arr. Find the sum of distinct elements in an array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: 15
Explanation: Distinct elements are 1, 2, 3, 4, 5. So sum is 15.
Input: arr[] = [5, 5, 5, 5, 5]
Output: 5
Explanation: Only Distinct element is 5. So sum is 5."""
    
                                #CODE HERE:-

class Solution:
	def findSum(self,arr):
		freq = {}
		for i in arr:
			if i not in freq:
				freq[i] = 1
			else:
				freq[i] += 1
		return(sum(freq.keys()))