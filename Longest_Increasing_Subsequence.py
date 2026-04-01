"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1"""

                                        #CODE HERE:-

class Solution:
    def lowerBound(self,nums,target):
        n = len(nums)
        l = 0
        r = n-1
        ans = n

        while l<=r:
            mid = (l+r)//2

            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def lengthOfLIS(self,nums):
        n = len(nums)
        lis = []
        lis.append(nums[0])
        
        for i in range(1,n):
            if nums[i]>lis[-1]:
                lis.append(nums[i])
            else:
                lb = self.lowerBound(lis,nums[i])
                lis[lb] = nums[i]
        return len(lis)