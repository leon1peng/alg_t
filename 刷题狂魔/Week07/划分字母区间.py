"""
划分字母区间
"""


# 1
# 哈希
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        max_index = {item: idx for idx, item in enumerate(S)}
        start, end, res = 0, 0, []
        for idx, char in enumerate(S):
            end = max(end, max_index[char])
            if idx == end:
                res.append(end - start + 1)
                start = idx + 1

        return res


# 2
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_map = {char: i for i, char in enumerate(S)}
        start, end, res = 0, 0, []
        for i, char in enumerate(S):
            end = max(end, char_map[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

