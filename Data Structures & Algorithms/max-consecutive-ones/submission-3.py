class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        result = 0

        for i in nums:
            if i == 0 and len(freq) == 0:
                continue

            elif i == 0:
                result = max(result, freq[1])
                freq[1] = 0

            else:
                freq[i] += 1
        return result if result > freq[1] else freq[1]

        