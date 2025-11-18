"""You are given a string s , the task is to reverse the string using stack.

Examples:

Input: s ="GeeksforGeeks"
Output:  skeeGrofskeeG
Input: s ="Geek"
Output: keeG"""

                                #CODE HERE:-

class Solution:
    def reverse(self, s: str) -> str:
        arr = []
        for i in range(len(s)-1,-1,-1):
            arr.append(s[i])
        return "".join(arr)