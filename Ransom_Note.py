"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true"""

                                                            #CODE HERE:-

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = {}
        freq2 = {}
        for i in ransomNote:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        for i in magazine:
            if i in freq1:
                if i not in freq2:
                    freq2[i] = 1
                else:
                    freq2[i] += 1
        for key in freq1.keys():
            if key not in freq2.keys():
                return False
            else:
                if freq1[key] > freq2[key]:
                    return False
        return True