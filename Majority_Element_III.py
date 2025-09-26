"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]"""

                                        #CODE HERE:-

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq = {}
        arr=[]
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for key,value in freq.items():
            if value>len(nums)/3:
                arr.append(key)
        return arr