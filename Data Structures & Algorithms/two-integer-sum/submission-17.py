# Since the the difference from the target and one of the sum must equal the other, we can check if we have seen the difference, if we have, we return both indices, else we place them in a map and keep looking

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx in range(len(nums)):
            if target - nums[idx] not in hashMap:
                hashMap[nums[idx]] = idx
            else:
                return [hashMap[target - nums[idx]], idx]

                