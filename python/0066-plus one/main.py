class Solution:
    def plusOne(self, digits):
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1,-1,-1):
            if digits[i] > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i - 1] += 1
            else:
                break
        return digits




a = Solution()
print(a.plusOne([1,2,3,4]))
print(a.plusOne([9,9,9,9]))