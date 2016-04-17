# coding=utf8
# 题目: N皇后问题, 给定N*N的棋盘,在上面放置N个皇后,这N个皇后不能同时在同一个行或者列且不同在同一条斜线上.问有多少种放置方法
# 思路: 回溯问题,依次确定每一行皇后的位置,利用一个数组记录每一行皇后放置的位置,在放置下一行时,判断当前行每个位置如果放置
# 皇后是否合法,如果合法则放置,并记录,然后继续判断下一行.这里利用了一个技巧,只利用一维向量,其中向量的下标表示行号,值表示
# 这一行皇后放置的列号.


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        mark = [0] * n
        Solution.ans = 0
        self.find_pos(mark,0, n)

        return Solution.ans

    def is_valid(self, mark, row, col):
        for i in range(row):
            if mark[i] == col or (abs(row - i) == abs(col - mark[i])):
                return False
        return True

    def find_pos(self, mark, row, n):
        if row == n:
            Solution.ans += 1
            return
        for col in range(n):
            if self.is_valid(mark, row, col):
                mark[row] = col
                self.find_pos(mark, row + 1, n)

print Solution().totalNQueens(4)
