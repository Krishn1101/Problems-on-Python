"""Given a sorted array arr consisting of 0s and 1s. The task is to find the index (0-based indexing) of the first 1 in the given array.

NOTE: If one is not present then, return -1.

Examples :

Input : arr[] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
Output : 6
Explanation: The index of first 1 in the array is 6.
Input : arr[] = [0, 0, 0, 0]
Output : -1
Explanation: 1's are not present in the array."""

                                                        #CODE HERE:-

class Solution:
    def firstIndex(self, arr):
        for i in range(len(arr)):
            if(arr[i]==1):
                return i
        return -1