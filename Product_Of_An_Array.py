"""Given an array, arr[] of positive integers. Your task is to return the product of array elements under the given modulo, mod with the value of 1000000007.

Note: The modulo operation finds the remainder after the division of one number by another. For example, k(mod(m))=k%m= remainder obtained when k is divided by m

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 24
Explanation: The product of the elements in the array is 1×2×3×4=24. Since 24 is less than 1000000007, the output is simply 24.
Input: arr[] = [100000, 100000, 100000]
Output: 993000007
Explanation:  The product of the array elements is 100000 × 100000 × 100000 = 1000000000000000. Taking modulo 1000000007, the result is 1000000000000000 % 1000000007 = 993000007"""

                                                            #CODE HERE:-

class Solution:
    def product(self, arr):
        pd = 1
        for i in arr:
            pd*=i
            pd = pd%1000000007
        return pd