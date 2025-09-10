"""You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

Note : A subarray is a continuous part of an array.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.
Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25."""

                                                            #CODE HERE:-

class Solution:
    def maxSubarraySum(self, arr):
        curr_sum = 0
        max_sum = arr[0]
        for i in range(len(arr)):
            curr_sum+=arr[i]
            if curr_sum>max_sum:
                max_sum = curr_sum
            if curr_sum<0:
                curr_sum = 0
        return max_sum