# Since they are anagrams, sorting each string must be the same
# so we use that as the key in a hashMap and the values is the list of the anagram

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            group["".join(sorted(s))].append(s)
        
        return [w for w in group.values()]

