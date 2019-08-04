class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        len1 = len(s)
        sum = 0
        for i in range(len1):
            if i < len1 - 1 and d[s[i]] < d[s[i+1]]:
                sum -= d[s[i]]
            else:
                sum += d[s[i]]
        return sum


a = Solution()
print(a.romanToInt("IX"))
print(a.romanToInt("LVIII"))