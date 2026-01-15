"""Given a string S, remove all consonants and print the modified string that contains vowels only.

Example 1:

Input
S = "abEkipo"
Output
aEio
Explanation : a, E, i, o are only vowels in the string.
Example 2:

Input
S = "rrty"
Output
No Vowel
Explanation: There are no vowels."""

                                            #CODE HERE:-

class Solution:
    def removeConsonants(self, s):
        ans = ""
        cnt = 0
        for i in s:
            if i in "AEIOU" or i in "aeiou":
                ans+=i
            else:
                cnt+=1
        if cnt == len(s):
            return 'No Vowel'
        else:
            return ans