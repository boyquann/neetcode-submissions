class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        idx = 0

        for num in nums:
            if (target - num) in hash:
                return [hash[target - num], idx]

            hash[num] = idx

            idx += 1