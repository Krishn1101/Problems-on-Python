"""Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.
NOTE: Add the whole string if other string is empty.

Example 1:

Input:
S1 = "Hello" S2 = "Bye"
Output: HBeylelo
Explanation: The characters of both the 
given strings are arranged alternatlively.
â€‹Example 2:

Input: 
S1 = "abc", S2 = "def"
Output: adbecf
Explanation: The characters of both the
given strings are arranged alternatlively."""

                                                            #CODE HERE:-

class Solution:
    def merge(self, S1, S2):
        ans = ""
        if len(S1)>len(S2):
            left = len(S1)-len(S2)
            for i in range(len(S2)):
                ans+=S1[i]
                ans+=S2[i]
            ans = ans + S1[-left:]
        elif len(S1)<len(S2):
            left = len(S2) - len(S1)
            for i in range(len(S1)):
                ans+=S1[i]
                ans+=S2[i]
            ans = ans + S2[-left:]
        else:
            for i in range(len(S1)):
                ans+=S1[i]
                ans+=S2[i]
        return ans