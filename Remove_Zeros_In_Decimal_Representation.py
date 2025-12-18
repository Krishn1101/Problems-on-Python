"""You are given a positive integer n.

Return the integer obtained by removing all zeros from the decimal representation of n.

 

Example 1:

Input: n = 1020030

Output: 123

Explanation:

After removing all zeros from 1020030, we get 123.

Example 2:

Input: n = 1

Output: 1

Explanation:

1 has no zero in its decimal representation. Therefore, the answer is 1."""

                                    #CODE HERE:-

class Solution:
    def removeZeros(self, n: int) -> int:
        n = str(n)
        if "0" not in n:
            return int(n)
        else:
            str1 = ""
            for i in n:
                if i!="0":
                    str1+=i
            return int(str1)