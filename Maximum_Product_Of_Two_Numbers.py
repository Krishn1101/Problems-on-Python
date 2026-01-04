"""Given an array arr of non-negative integers, return the maximum product of two numbers possible.

Example:

Input: arr[] = [1, 4, 3, 6, 7, 0] 
Output: 42
Explanation: 6 and 7 have the maximum product.
Input: arr[] = [1, 100, 42, 4, 23]
Output: 4200
Explanation:  42 and 100 have the maximum product."""

                                            #CODE HERE:-

class Solution:
      def maxProduct(self,arr):
        mx1 = max(arr)
        arr.remove(mx1)
        mx2 = max(arr)
        return mx1 * mx2