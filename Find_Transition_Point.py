"""Given a sorted array, arr[] containing only 0s and 1s, find the transition point,
i.e., the first index where 1 was observed, and before that, only 0 was observed.
If arr does not have any 1, return -1. If array does not have any 0, return 0.

Examples:

Input: arr[] = [0, 0, 0, 1, 1]
Output: 3
Explanation: index 3 is the transition point where 1 begins.
Input: arr[] = [0, 0, 0, 0]
Output: -1
Explanation: Since, there is no "1", the answer is -1.
Input: arr[] = [1, 1, 1]
Output: 0
Explanation: There are no 0s in the array, so the transition point is 0,
indicating that the first index (which contains 1) is also the first position of the array."""

                                        #CODE HERE:-

class Solution:
    def transitionPoint(self, arr):
        if not arr:
            return -1
        if 1 not in arr:
            return -1
        for i in range(len(arr)):
            if arr[i] == 1:
                return i
        return -1