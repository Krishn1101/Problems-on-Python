"""You have been given a String S. You need to find
and print whether this string is a palindrome or not.
If yes, print "YES" (without quotes), else print "NO" (without quotes).



Example 1:
Input: s = aba
Output: YES

Example 2:
Input: s = good
Output: NO"""

                            #CODE HERE:-

class Solution:
    def PalindromicStringg(self, s: list[str]) -> None:
        s = input()
        if(s==s[::-1]):
            print("YES")
        else:
            print("NO")