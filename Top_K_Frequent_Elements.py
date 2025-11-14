"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]"""

                                                        #CODE HERE:-

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        arr = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        ans = list(freq.items())
        ans.sort(key = lambda x:x[1],reverse = True)
        for i in range(k):
            arr.append(ans[i][0])
        return arr