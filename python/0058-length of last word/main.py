class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        s = s.rstrip()
        for i in range(len(s) - 1 ,-1, -1):
            if s[i] == ' ':
                break
            ans += 1
        return ans

a = Solution()
print(a.lengthOfLastWord("Hello World"))
print(a.lengthOfLastWord(" "))