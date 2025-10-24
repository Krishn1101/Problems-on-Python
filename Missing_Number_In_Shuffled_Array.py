"""Given an array arr1. The contents of arr are copied into another array arr2 and numbers are shuffled. Also, one element is removed from arr2. The task is to find the missing element.

Examples:
Input: arr1[] = [4, 8, 1, 3, 7] and arr2[] = [7, 4, 3, 1]
Output: 8
Explanation: 8 is the only element missing from arr2.
Input: arr1[] = [12, 10, 15, 23, 11, 30] and arr2[] = [15, 12, 23, 11, 30]
Output: 10
Explanation: 10 is the only element missing from arr2."""

                                                        #CODE HERE:-

class Solution:
    def findMissing(self, arr1,arr2):
        arr1.sort()
        arr2.sort()
        arr2.append(-1)
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return arr1[i]