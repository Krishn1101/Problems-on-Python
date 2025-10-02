"""Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.
Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. 
Input: s1 = "listen", s2 = "lists" 
Output: false 
Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams."""

                                                            #CODE HERE:-

class Solution:
    def areAnagrams(self, s1, s2):
        freq1 = {}
        freq2 = {}
        for i in s1:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        for i in s2:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1
        if len(freq1) == len(freq2):
            for key,value in freq1.items():
                if key not in freq2:
                    return False
                if freq2[key] != value:
                    return False
            return True
        return False