"""
据数字二进制下 1 的数目排序
"""


# 1
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        d = {}
        for i in arr:
            t = str(bin(i))
            n = t.count('1')
            if n not in d:
                d[n] =[]
            d[n].append(i)

        for i in sorted(d):
            res+=sorted(d[i])
        return res


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'),x))


# 2

