"""Given a queue of persons represented by an array of integers, where each person is identified by a specific integer, find the minimum kilograms of apples that need to be distributed, ensuring that each person receives 1 kilogram of apples only once.

Examples:

Input: arr[] = [1, 1, 1, 1, 1]
Output: 1
Explanation: The person identified by '1' appears multiple times but will only receive 1 kilogram of apples once. Therefore, the minimum apples required is 1 kg.
Input: arr[] = [1, 2, 3, 1, 2]
Output: 3
Explanation: There are three distinct persons in the queue, so 3 kilograms of apples need to be distributed."""

                                                    #CODE HERE:-
                                                    
class Solution:
    def minimumApple(self, arr):
        set1 = set(arr)
        return len(set1)