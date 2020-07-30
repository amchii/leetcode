"""

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
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
