class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_sort = [ [] for _ in range(len(nums) + 1)]
        frequency = defaultdict(int)
        result = []

        for num in nums:
            frequency[num] += 1

        for element, freq in frequency.items():
            bucket_sort[freq].append(element)

        for freq in range(len(bucket_sort) - 1, 0, -1):
            for element in bucket_sort[freq]:
                result.append(element)

                if len(result) == k:
                    return result

  