"""Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets."""

                                                        #CODE HERE:-

class Solution:
    def rec(self,i,sm,nums,total,dp):
        if sm>(total//2):
            return False
        elif sm==(total//2):
            return True
        elif i == len(nums):
            return False
        
        if dp[i][sm]!=-1:
            return dp[i][sm]

        #take case:-
        take = self.rec(i+1,sm+nums[i],nums,total,dp)

        #not_take case:-
        not_take = self.rec(i+1,sm,nums,total,dp)

        dp[i][sm] = take or not_take
        return dp[i][sm]

    def canPartition(self,nums):
        n = len(nums)
        if n == 1:
            return False

        total = sum(nums)

        if total%2==1:
            return False
        
        dp = [[-1 for j in range((total//2)+1)] for i in range(n)]

        return self.rec(0,0,nums,total,dp)