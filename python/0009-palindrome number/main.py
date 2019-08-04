class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strx = str(x)
        lst = list(zip(list(strx), reversed(strx)))
        #print(lst)
        for a, b in lst:
            #print("a: {}, b: {}".format(a, b))
            if a != b :
                return False
        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        z = x
        while z:
            y = y * 10 + z % 10
            z //= 10
        if x == y:
            return True
        else:
            return False


a = Solution1()
print(a.isPalindrome(22))
b = Solution()
print(b.isPalindrome(36631))