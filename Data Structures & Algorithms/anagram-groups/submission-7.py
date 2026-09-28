class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list) # str : [ ]

        for s in strs:
            hash["".join(sorted(s))].append(s)

        return list(hash.values())