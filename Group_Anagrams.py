"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]"""

                                        #CODE HERE:-

class Solution:
    def sortString(self,s):
            s1 = list(s)
            s1.sort()
            return "".join(s1)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict1 = {}

        for s in strs:
            key = self.sortString(s)
            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key] = [s]
        
        return list(dict1.values())