class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        bucket_sort = [[] for _ in range(len(nums) + 1)]
        result = []

        for i in nums:
            frequency[i] += 1

        for element, freq in frequency.items():
            bucket_sort[freq].append(element)

        for i in range(len(bucket_sort) - 1, 0, -1):
            for element in bucket_sort[i]:
                result.append(element)

                if len(result) == k:
                    return result
        