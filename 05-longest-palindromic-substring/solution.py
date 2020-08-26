"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        t_str = s[0]

        def f(a):
            a1, a2 = index + a, index + 1
            nonlocal t_str
            while (a1 >= 0 and a2 < len(s)) and s[a1] == s[a2]:
                if a2 - a1 + 1 >= len(t_str):
                    t_str = s[a1:a2 + 1]
                a1 -= 1
                a2 += 1
        for index, e in enumerate(s):
            f(0)
            f(-1)
        return t_str

    def longestPalindrome_(self, s: str) -> str:
        if not s:
            return ''
        t_str = s[0]
        for index, e in enumerate(s):
            a0, a1, a2 = index - 1, index, index + 1
            a0_failed, a1_failed = False, False
            while (a1 >= 0 and a2 < len(s)) and (
                    (s[a0] == s[a2] and not a0_failed) or (s[a1] == s[a2] and not a1_failed)):
                if (a0 >= 0 and s[a0] == s[a2] and not a0_failed):
                    if a2 - a0 + 1 > len(t_str):
                        t_str = s[a0:a2 + 1]
                    a0 -= 1
                else:
                    a0_failed = True
                if (s[a1] == s[a2] and not a1_failed):
                    if a2 - a1 + 1 > len(t_str):
                        t_str = s[a1:a2 + 1]
                    a1 -= 1
                else:
                    a1_failed = True
                a2 += 1
        return t_str


if __name__ == '__main__':
    print(Solution().longestPalindrome("adam"))
    print(Solution().longestPalindrome("aabbbbaaaabcbadabcb"))
    print(Solution().longestPalindrome('a'))
    print(Solution().longestPalindrome_("aabcbadabcb"))
