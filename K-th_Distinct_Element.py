"""Given an array of n integers. Find the kth distinct element.

Example 1:

Input: 
n = 6, k = 2
arr = {1, 2, 1, 3, 4, 2}
Output:
4
Explanation: 1st distinct element will be 3
and the 2nd distinct element will be 4. As 
both the elements present in the array only 1 
times.
Example 2:

Input: 
n = 6, k = 3
arr = {1, 2, 50, 10, 20, 2}
Output:
10"""

                        #CODE HERE:-

class Solution:
    def KthDistinct(self, nums, k):
        freq = {}
        cnt = 0
        ans = 0
        if k>len(nums):
            return -1
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for key, value in freq.items():
            if value == 1:
                cnt+=1
                ans = key
            if cnt == k:
                return key
        return -1
        