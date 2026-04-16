"""Given two strings, s1 and s2. The task is to remove all characters that are common in both strings and then combine the remaining characters from each string to form a new string. The characters that are not shared between the two strings should appear in the result in the same order as they appear in their respective original strings. If, after removing the common characters, no characters are left to form the result, return "-1"

Examples:

Input: s1 = aacdb, s2 = gafd
Output: cbgf
Explanation: The common characters of s1 and s2 are: a, d. The uncommon characters of s1 and s2 are c, b, g and f. Thus the modified string with uncommon characters concatenated is cbgf.
Input: s1 = abcs, s2 = cxzca
Output: bsxz
Explanation: The common characters of s1 and s2 are: a,c. The uncommon characters of s1 and s2 are b,s,x and z. Thus the modified string with uncommon characters concatenated is bsxz."""

                                                            #CODE HERE:-

class Solution:
    def concatenatedString(self,s1,s2):
        s = s1+s2
        ans = ""
        for i in s:
            if (i in s1) and (i not in s2) or (i in s2) and (i not in s1):
                ans+=i
        if len(ans) == 0:
            return -1
        else:
            return ans