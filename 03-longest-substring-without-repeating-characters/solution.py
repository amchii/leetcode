from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """一路向北，直接跳跃"""
        if s == "":
            return 0
        count = 0
        start = -1
        hash_map = {}
        for i, e in enumerate(s):
            if e in hash_map and start < hash_map[e]:
                start = hash_map[e]
                hash_map[e] = i
            else:
                hash_map[e] = i
                if count < i - start:
                    count = i - start

        return count

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """滑动窗口"""
        l = 0
        ans = 0
        counter = defaultdict(lambda: 0)

        for r in range(len(s)):
            while counter[s[r]] != 0:
                counter[s[l]] = counter[s[l]] - 1
                l += 1
            counter[s[r]] += 1
            ans = max(ans, r - l + 1)

        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcdbef'))
