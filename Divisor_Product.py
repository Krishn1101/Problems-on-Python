"""Given a number N, find the product of all the divisors of N (including N).

 

Example 1:

Input : 
N = 6
Output:
36
Explanation:
Divisors of 6 : 1, 2, 3, 6
Product = 1*2*3*6 = 36 

Example 2:

Input : 
N = 5
Output:
5
Explanation:
Divisors of 5 : 1, 5
Product = 1*5 = 5 """

                                    #CODE HERE:-

#User function Template for python3

class Solution:
    def divisorProduct(self, N):
        prod = 1
        i = 1
    
        while i * i <= N:
            if N % i == 0:
                prod *= i
                
                if i != N // i:
                    prod *= (N // i)
            i += 1
        
        return prod%((10**9)+7)