class Solution:
    def maxProfit(self, prices):
        minValue = float("inf")
        maxValue = 0
        for value in prices:
            minValue = min(value, minValue)
            maxValue = max(maxValue, value - minValue)
            #print("vlaue:{}, minValue:{}, maxPro:{}".format(value, minValue ,maxValue))
        return maxValue


a = Solution()
print(a.maxProfit([7,2,1,5,3,6,4]))
print(a.maxProfit([]))
