class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1]) if len(a) > 0 else 0


a = Solution()
print(a.lengthOfLastWord("Hello World"))
print(a.lengthOfLastWord(" "))