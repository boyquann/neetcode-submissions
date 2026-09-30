class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        
        for idx in range(1, len(arr)):
            result.append(max(arr[idx : len(arr)]))
        
        result.append(-1)

        return result