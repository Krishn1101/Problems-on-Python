"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]"""

                                                            #CODE HERE:-

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return ([-1,-1])
        ans1 = nums.index(target)
        cnt = nums.count(target)
        if len(nums)==1:
            return([0,0])
        else:
            return([ans1,ans1 + cnt-1])