class Solution:
    def groupAnagrams(self, strs: List[str]) :
        seen = {}
        for word in strs:
            current_count = frozenset(Counter(word).items())
            if current_count in seen:
                seen[current_count].append(word)
            else:
                seen[current_count] = [word]
        return list(seen.values())