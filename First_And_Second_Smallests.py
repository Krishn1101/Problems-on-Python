"""Given an array, arr[] of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: [2, 3] 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: [-1]
Explanation: Only element is 1 which is smallest, so there is no second smallest element."""

                                                                #CODE HERE:-

class Solution:
    def minAnd2ndMin(self, arr):
        set1 = list(set(arr))
        
        if len(set1)<2:
            return [-1]
        set1.sort()
        return(set1[0],set1[1])