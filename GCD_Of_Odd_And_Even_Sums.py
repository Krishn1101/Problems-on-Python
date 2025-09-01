"""You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the first n odd numbers.

sumEven: the sum of the first n even numbers.

Return the GCD of sumOdd and sumEven.

 

Example 1:

Input: n = 4

Output: 4

Explanation:

Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

Example 2:

Input: n = 5

Output: 5

Explanation:

Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25
Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30
Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5."""

                                        #CODE HERE:-

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        i=0
        sm1 = n*(n+1)              #SUM OF EVEN NUMBERS UP TO 2N
        sm2 = n**2                 #SUM OF ODD NUMBERS UP TO 2N
        return self.gcd(sm1,sm2)
        #GCD(sm1,sm2):-
    def gcd(self,sm1,sm2):
        if sm2 == 0:
            return sm1
        return self.gcd(sm2,sm1%sm2)