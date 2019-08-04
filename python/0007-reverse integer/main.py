class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        y = ""
        str_x = str(x)
        if str_x[0] == '-':
            y += '-'
        y += str_x[len(str_x)::-1].lstrip('0').rstrip('-')
        y = int(y)
        if -2**31 < y and y < 2**31 - 1:
            return y
        else:
            return 0

a = Solution()
print(a.reverse(0))
print(a.reverse(1230))
print(a.reverse(-12340))
print(a.reverse(2147483647))



