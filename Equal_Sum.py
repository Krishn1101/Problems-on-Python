"""Given an array arr. Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 

Example:

Input: arr[] = [1, 2, 3, 3]
Output: true
Explanation: Consider 1-based indexing i = 3, for [1, 2] sum is 3 and for [3] sum is also 3.
Input: arr[] = [1, 5]
Output: false
Explanation: No such index present."""

                                                            #CODE HERE:-

class Solution:
    def equilibrium(self,arr):
        total_sm = sum(arr)
        left_sm = 0
        
        for j in range(len(arr)):
            right_sm = total_sm - left_sm - arr[j]
            if left_sm == right_sm:
                 return ("true")
            left_sm += arr[j]
        return ("false")