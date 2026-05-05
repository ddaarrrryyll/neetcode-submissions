class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        seen = defaultdict(lambda: False)
        while r < len(s):
            char = s[r]
            # print(f"{l=} {r=} {s[l:r+1]=} {seen=}")
            if not seen[char]:
                seen[char] = True
                max_len = max(max_len, r-l+1)
                r += 1
            else:
                while seen[s[l]] and l < r:
                    seen[s[l]] = False
                    l += 1
                    if not seen[char]:
                        break
        return max_len