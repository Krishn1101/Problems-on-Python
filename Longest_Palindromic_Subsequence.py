"""Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb"."""

                                                        #CODE HERE:-

class Solution:
    def longestPalindromeSubseq(self,s):
        text1 = s
        text2 = s[::-1]
        n = len(text1)
        m = len(text2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[n][m]