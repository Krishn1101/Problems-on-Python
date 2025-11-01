"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"""

                                                                    #CODE HERE:-

class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        m = ""
        for i in range(len(a)):
            b=a[i]
            c=b[::-1]
            a[i]=c
        
        for i in range(len(a)):
            m = m + a[i]
            m = m + " "
        return m.strip()