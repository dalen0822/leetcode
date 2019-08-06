class Solution1:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        min_sub_len = min(len(a) for a in strs)
        comm_str = ''
        for j in range(min_sub_len):
            for i in range(len(strs)):
                if strs[0][j] != strs[i][j]:
                    return comm_str
            comm_str += strs[0][j]
        return comm_str

class Solution:
    def longestCommonPrefix(self, strs):
        comstr = ''
        for a in list(zip(*strs)):
            if len(set(a)) == 1:
                comstr += a[0]
            else:
                break;
        return comstr

a = Solution()
print(a.longestCommonPrefix(['flower', 'flow', 'flight']))
print(a.longestCommonPrefix(["dog","racecar","car"]))
print(a.longestCommonPrefix(["a","a"]))