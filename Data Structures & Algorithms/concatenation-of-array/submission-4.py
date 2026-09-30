class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0

        while i < 2:
            for num in range(len(nums)):
                ans.append(nums[num])

            i += 1

        return ans
        