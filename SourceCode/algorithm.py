import numpy as np


class Algorithm:
    def __init__(self):
        self.chessboard = np.array([
            [-1, -2, -3, -4, -5, -4, -3, -2, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, -6, 0, 0, 0, 0, 0, -6, 0],
            [-7, 0, -7, 0, -7, 0, -7, 0, -7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 7, 0, 7, 0, 7, 0, 7],
            [0, 6, 0, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 4, 3, 2, 1]
        ])

    # x指1维数组的元素
    # y指2维数组的1维数组

    # 車的走法
    def rook(self, x1, y1, x2, y2):
        # 红黑
        if (self.chessboard[y1, x1] > 0 >= self.chessboard[y2, x2] or
                self.chessboard[y1, x1] < 0 <= self.chessboard[y2, x2]):
            if x1 == x2 and y1 != y2:
                for i in range(min(y1, y2) + 1, max(y1, y2)):
                    if self.chessboard[i, x1] != 0:
                        return
                return True
            if y1 == y2 and x1 != x2:
                for i in range(min(x1, x2) + 1, max(x1, x2)):
                    if self.chessboard[y1, i] != 0:
                        return
                return True

    # 马的走法
    def knight(self, x1, y1, x2, y2):
        # 红黑
        if (self.chessboard[y1, x1] > 0 >= self.chessboard[y2, x2] or
                self.chessboard[y1, x1] < 0 <= self.chessboard[y2, x2]):
            if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
                if self.chessboard[y1, (x1 + x2) // 2] == 0:
                    return True
            if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
                if self.chessboard[(y1 + y2) // 2, x1] == 0:
                    return True

    # 炮的走法
    def cannon(self, x1, y1, x2, y2):
        __num = 0
        # 红黑
        if (self.chessboard[y1, x1] > 0 >= self.chessboard[y2, x2] or
                self.chessboard[y1, x1] < 0 <= self.chessboard[y2, x2]):
            if x1 == x2 and y1 != y2:
                for i in range(min(y1, y2) + 1, max(y1, y2)):
                    if self.chessboard[i, x1] != 0:
                        __num += 1
            elif y1 == y2 and x1 != x2:
                for i in range(min(x1, x2) + 1, max(x1, x2)):
                    if self.chessboard[y1, i] != 0:
                        __num += 1
            else:
                return
            if self.chessboard[y2, x2] != 0:
                if __num == 1:
                    return True
            else:
                if __num == 0:
                    return True

    # 士的走法
    def guard(self, x1, y1, x2, y2):
        if 3 <= x2 <= 5 and abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
            # 红
            if y1 >= 7 and y2 >= 7:
                if self.chessboard[y2, x2] <= 0:
                    return True
            # 黑
            if y1 <= 2 and y2 <= 2:
                if self.chessboard[y2, x2] >= 0:
                    return True

    # 象的走法
    def elephant(self, x1, y1, x2, y2):
        if abs(x2 - x1) == 2 and abs(y2 - y1) == 2:
            if self.chessboard[(y1+y2)//2, (x1+x2)//2] == 0:
                # 红
                if y1 >= 5 and y2 >= 5:
                    if self.chessboard[y2, x2] <= 0:
                        return True
                # 黑
                if y1 <= 4 and y2 <= 4:
                    if self.chessboard[y2, x2] >= 0:
                        return True

    # 将的走法
    def general(self, x1, y1, x2, y2):
        if 3 <= x2 <= 5:
            if x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2:
                # 红
                if y1 >= 7:
                    if self.chessboard[y2, x2] <= 0:
                        if y2 >= 7:
                            if abs(x1 - x2) == 1 or abs(y1 - y2) == 1:
                                return True
                        else:
                            if self.chessboard[y2, x2] == -5:
                                for i in range(y2 + 1, y1):
                                    if self.chessboard[i, x1] != 0:
                                        return
                                return True
                # 黑
                if y1 <= 2:
                    if self.chessboard[y2, x2] >= 0:
                        if y2 <= 2:
                            if abs(x1 - x2) == 1 or abs(y1 - y2) == 1:
                                return True
                        else:
                            if self.chessboard[y2, x2] == 5:
                                for i in range(y1 + 1, y2):
                                    if self.chessboard[i, x1] != 0:
                                        return
                                return True

    # 兵的走法
    def pawn(self, x1, y1, x2, y2):
        # 红
        if self.chessboard[y1, x1] > 0 >= self.chessboard[y2, x2]:
            if y1 >= 5 and x1 == x2:
                if y1 - y2 == 1:
                    return True
            if y1 < 5:
                if x1 == x2 and y1 - y2 == 1 or y1 == y2 and abs(x2 - x1) == 1:
                    return True
        # 黑
        if self.chessboard[y1, x1] < 0 <= self.chessboard[y2, x2]:
            if y1 <= 4 and x1 == x2:
                if y2 - y1 == 1:
                    return True
            if y1 > 4:
                if x1 == x2 and y2 - y1 == 1 or y1 == y2 and abs(x2 - x1) == 1:
                    return True
