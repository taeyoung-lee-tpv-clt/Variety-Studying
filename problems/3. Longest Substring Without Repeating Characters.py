class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len, start = 0, 0
        for i, j in enumerate(s):
            while j in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(j)
            max_len = max(max_len, i - start + 1)
        return max_len
