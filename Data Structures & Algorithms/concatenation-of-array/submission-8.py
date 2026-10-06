class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []

        while i < 2:
            for n in nums:
                ans.append(n)
            i += 1
        return ans
