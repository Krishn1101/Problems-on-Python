"""Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

Example 1:


Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:


Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other."""

                                                            #CODE HERE:-

class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        arr = []
        j = 1
        for i in range(len(nums)):
            if nums[i] == 1:
                arr.append(i)
        for i in range(len(arr)-1):
            if arr[j] - arr[i] <= k:
                return False
            else:
                j+=1
        return True