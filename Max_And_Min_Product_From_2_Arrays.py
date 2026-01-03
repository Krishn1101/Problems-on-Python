"""Given two arrays of arr1 and arr2, the task is to calculate the product of the maximum element of the first array arr1, and minimum element of the second array arr2.

Examples :

Input : arr1 = [5, 7, 9, 3, 6, 2],  arr2 = [1, 2, 6, 1, 9]
Output : 9
Explanation: The max in arr1 is 9. The min element in arr2 is 1. The product is 9*1 = 9.
Input : arr1 = [0, 0, 0, 0],  arr2 = [1, 1, 2]
Output : 0"""

                                                                #CODE HERE:-

class Solution:
    def find_multiplication(self, arr1, arr2):
        mx = max(arr1)
        mn = min(arr2)
        return mx*mn