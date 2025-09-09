"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome."""

                                                #CODE HERE:-

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for i in s:
            if 48<=ord(i)<=57 or 97<=ord(i)<=122:
                ans+=i
        ans1 = ans[::-1]
        if ans1 == ans:
            return True
        else:
            return False