"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"""

                                            #CODE HERE:-

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        i = 0
        j = len(s)-1

        while i<j:
            if s[i] not in vowels:
                i+=1
                continue
            if s[j] not in vowels:
                j-=1
                continue
            else:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        return ''.join(s)