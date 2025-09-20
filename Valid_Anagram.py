"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false"""

                                #CODE HERE:-

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for i in t:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] -= 1
        
        for i in freq.values():
            if i!=0:
                return False
        
        return True