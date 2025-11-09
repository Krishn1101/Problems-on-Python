"""You are given an integer array nums.

Return the bitwise OR of all even numbers in the array.

If there are no even numbers in nums, return 0.

 

Example 1:

Input: nums = [1,2,3,4,5,6]

Output: 6

Explanation:

The even numbers are 2, 4, and 6. Their bitwise OR equals 6.

Example 2:

Input: nums = [7,9,11]

Output: 0

Explanation:

There are no even numbers, so the result is 0.

Example 3:

Input: nums = [1,8,16]

Output: 24

Explanation:

The even numbers are 8 and 16. Their bitwise OR equals 24."""

                        #CODE HERE:-

class Solution:
    def evenNumberBitwiseORs(self, nums: list[int]) -> int:
        ans = 0
        n = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                ans = nums[i]
                n = i
                break
        for i in range(n+1,len(nums)):
            if nums[i]%2==0:
                ans = ans|nums[i]
        return ans