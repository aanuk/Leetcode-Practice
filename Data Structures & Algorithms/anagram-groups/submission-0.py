class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = {}
        for i in strs:
            key = "".join(sorted(i))

            if key not in new:
                new[key] = []

            new[key].append(i)
        return list(new.values())
