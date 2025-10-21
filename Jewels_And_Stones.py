"""You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0"""

                                                                #CODE HERE:-

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq1 = {}
        freq2 = {}
        cnt = 0
        for i in jewels:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        for i in stones:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1
        for key,value in freq1.items():
            if key in stones:
                cnt = cnt + freq2[key]
        return cnt