class Solution:
    def groupAnagrams(self, strs: List[str]) :
        seen = {}
        for i in range(len(strs)):
            current_count = frozenset(Counter(strs[i]).items())
            if current_count in seen:
                seen[current_count].append(strs[i])
            else:
                seen[current_count] = [strs[i]]
        return list(seen.values())