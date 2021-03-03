"""
猜数字游戏
"""


# 1
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = B = 0
        dict1, dict2 = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                dict1[secret[i]] = 1 if secret[i] not in dict1 else dict1[secret[i]] + 1
                dict2[guess[i]] = 1 if guess[i] not in dict2 else dict2[guess[i]] + 1
        for x in dict1:
            if x in dict2:
                B += min(dict1[x], dict2[x])
        return str(A) + 'A' + str(B) + 'B'


# 2
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = B = 0
        dict1, dict2 = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                dict1[secret[i]] = 1 if secret[i] not in dict1 else dict1[secret[i]] + 1
                dict2[guess[i]] = 1 if guess[i] not in dict2 else dict2[guess[i]] + 1
        for x in dict1:
            if x in dict2:
                B += min(dict1[x], dict2[x])
        return str(A) + 'A' + str(B) + 'B'


# 3
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        dict1, dict2 = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                dict1[secret[i]] = 1 if secret[i] not in dict1 else dict1[secret[i]] + 1
                dict2[guess[i]] = 1 if guess[i] not in dict2 else dict2[guess[i]] + 1
        for x in dict1:
            if x in dict2:
                b += min(dict1[x], dict2[x])
        return str(a) + 'A' + str(b) + 'B'


# 4
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        dict1, dict2 = dict(), dict()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                dict1[secret[i]] = 1 if secret[i] not in dict1 else dict1[secret[i]] + 1
                dict2[guess[i]] = 1 if guess[i] not in dict2 else dict2[guess[i]] + 1
        for x in dict1:
            if x in dict2:
                b += min(dict1[x], dict2[x])
        return str(a) + "A" + str(b) + "B"


# 5
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        dict1, dict2 = dict(), dict()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                dict1[secret[i]] = 1 if secret[i] not in dict1 else dict1[secret[i]] + 1
                dict2[guess[i]] = 1 if guess[i] not in dict2 else dict2[guess[i]] + 1
        for x in dict1:
            if x in dict2:
                b += min(dict1[x], dict2[x])
        return str(a) + "A" + str(b) + "B"

