class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            length = 0

            if (num - 1) not in nums_set:
                length += 1

                while (num + 1) in nums_set:
                    length += 1
                    num += 1

                if (length >= longest):
                    longest = length

        return longest

            