class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        len1 = len(s)
        sum = 0
        flag = False
        for i in range(len1 - 1):
            if flag == True:
                flag = False
                continue
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                flag = True
                sum += d[s[i+1]] - 1
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                flag = True
                sum += d[s[i+1]] - 10
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                flag = True
                sum += d[s[i+1]] - 100
            else:
                sum += d[s[i]]
        if flag == False:
            sum += d[s[len1-1]]
        return sum


a = Solution()
print(a.romanToInt("IX"))
print(a.romanToInt("LVIII"))