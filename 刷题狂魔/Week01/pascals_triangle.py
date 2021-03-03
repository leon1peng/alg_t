"""
杨辉三角
"""


# 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        angle = []
        for i in range(numRows):
            angle.append([1])
        for i in range(1, numRows):
            for x in range(1, i):
                angle[i].append(angle[i - 1][x - 1] + angle[i - 1][x])
            angle[i].append(1)
        return angle


# 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        angle = []
        for i in range(numRows):
            angle.append([1])
        for i in range(1, numRows):
            for x in range(1, i):
                angle[i].append(angle[i - 1][x - 1] + angle[i - 1][x])
            angle[i].append(1)
        return angle


# 3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        angle = []
        for i in range(numRows):
            angle.append([1])
        for i in range(1, numRows):
            for x in range(1, i):
                angle[i].append(angle[i - 1][x - 1] + angle[i - 1][x])
            angle[i].append(1)
        return angle


# 4
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        angle = []
        for i in range(numRows):
            angle.append([1])
        for i in range(1, numRows):
            for x in range(1, i):
                angle[i].append(angle[i - 1][x - 1] + angle[i - 1][x])
            angle[i].append(1)
        return angle


# 5
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        angle = []
        for i in range(numRows):
            angle.append([1])
        for i in range(1, numRows):
            for x in range(1, i):
                angle[i].append(angle[i - 1][x - 1] + angle[i - 1][x])
            angle[i].append(1)
        return angle


def angles(n):
    l = [[1]]
    for i in range(n):
        l.append([1])
    for i in range(1, n):
        for x in range(1, i):
            l[i].append(l[i - 1][x - 1] + l[i - 1][x])
            print(l[i])
        l[i].append(1)


if __name__ == '__main__':
    angles(5)
