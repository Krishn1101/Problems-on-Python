"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0."""

                                                                #CODE HERE:-

class Solution:
    def rec(self,i,j,text1,text2,dp):
        if i>=len(text1) or j>=len(text2):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        
        ans = 0
        if text1[i] == text2[j]:
            ans = 1 + self.rec(i+1,j+1,text1,text2,dp)
        else:
            ans = max(self.rec(i,j+1,text1,text2,dp),self.rec(i+1,j,text1,text2,dp))
        
        dp[i][j] = ans
        return dp[i][j]

    def longestCommonSubsequence(self,text1,text2):
        dp = [[-1 for i in range(len(text2))] for j in range(len(text1))]
        return self.rec(0,0,text1,text2,dp)