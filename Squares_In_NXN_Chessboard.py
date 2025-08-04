"""Find the total number of Squares in a N*N chessboard.

 

Example 1:

Input:
N = 1
Output:
1
Explanation:
A 1*1 chessboard has only 1 square.
Example 2:

Input:
N = 2
Output:
5
Explanation:
A 2*2 chessboard has 5 squares.
4 1*1 squares and a 2*2 square."""

                    #CODE HERE:-

class Solution:
    def squaresInChessBoard(self, N):
        cnt = 1
        sm = 0
        i=1
        while(cnt!=N+1):
            sm+=i*i
            i+=1
            cnt+=1
        return sm