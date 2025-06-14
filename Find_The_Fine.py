"""Given an array of car numbers car[], an array of penalties fine[], and an integer value date. The task is to find the total fine which will be collected on the given date. The fine is collected from odd-numbered cars on even dates and vice versa.

Examples:

Input: date = 12, car[] = [2375, 7682, 2325, 2352], fine[] = [250, 500, 350, 200]
Output: 600
Explanation: The date is 12 (even), so we collect the fine from odd-numbered cars. The odd-numbered cars and the fines associated with them are as follows:
2375 -> 250
2325 -> 350
The sum of the fines is 250+350 = 600
Input: date = 8, car[] = [2222, 2223, 2224], fine[] = [200, 300, 400]
Output: 300"""

                                                            #CODE HERE:-

class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        ar1=[]
        ar2=[]
        if(date%2==0):
            for i in range(len(car)):
                if(car[i]%2!=0):
                    ar1.append(fine[i])
                else:
                    i+=1
        elif(date%2!=0):
            for j in range(len(car)):
                if(car[j]%2==0):
                    ar2.append(fine[j])
                else:
                    j+=1
        if(date%2==0):
            return (sum(ar1))
        elif(date%2!=0):
            return (sum(ar2))