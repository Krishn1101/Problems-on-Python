"""Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4"""

                                                #CODE HERE:-

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]<target):
                if(i!=len(nums)-1):
                    i+=1
                elif(i==len(nums)-1):
                    return i+1
            elif(nums[i]==target):
                return i
            else:
                if(nums[i]>target):
                    return i