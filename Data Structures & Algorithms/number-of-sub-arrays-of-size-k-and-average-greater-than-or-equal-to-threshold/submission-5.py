# We want the NUMBER of subarrays of size k such that their average is greater than or equal to threshold

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = []
        L = 0

        windowSum = sum(arr[ : k])
        result.append(windowSum)

        for R in range(k, len(arr)):
            windowSum += arr[R] - arr[R - k]
            result.append(windowSum)
        
        good = [s for s in result if s / k >= threshold]
        return len(good)




    

        