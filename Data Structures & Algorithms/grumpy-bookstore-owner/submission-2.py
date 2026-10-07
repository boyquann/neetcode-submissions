[0, ]
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        windowSum = 0
        maxSum = 0

        for R in range(minutes):
            if grumpy[R] == 1:
                windowSum += customers[R]
        maxSum = windowSum

        for R in range(minutes, len(customers)):
            if grumpy[R] == 1:
                windowSum += customers[R]
            
            if grumpy[R - minutes] == 1:
                windowSum -= customers[R - minutes]
            maxSum = max(maxSum, windowSum)
        
        for R in range(len(customers)):
            if grumpy[R] == 0:
                maxSum += customers[R]
        return maxSum
            

            


