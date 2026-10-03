class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        windowSum = 0
        result = float('inf')

        for r in range(len(nums)):
            windowSum += nums[r]

            while windowSum >= target:
                result = min(result, r - l + 1)
                windowSum -= nums[l]
                l += 1
        return result if result != float('inf') else 0
                
                



        