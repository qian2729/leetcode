# coding=utf8
# 题目: N皇后问题,给定一个N*N大小的棋盘,在上面放N个皇后,N个皇后不同同时出现在同一行和同一列或同一斜线上,问有哪些不同的摆法
# 思路: 一行一行的放置N个皇后,利用一个数组记录每个位置是否放置皇后,利用回溯法遍历所有放置的可能

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        mark_arr = [0] * n
        DOTS = '.' * n
        
        def is_valid(mark_arr, row, col):
            for i in range(row):
                if mark_arr[i] == col or (abs(col - mark_arr[i]) == abs(row - i)):
                    return False
            return True
            

        def dfs(mark_arr, row, sol):
            if row == n:
                Solution.ans.append(sol)
                return
            for col in range(n):
                if is_valid(mark_arr,row, col):
                    mark_arr[row] = col
                    dfs(mark_arr, row + 1, sol + [DOTS[:col] + 'Q' + DOTS[col + 1:]])
        Solution.ans = []
        dfs(mark_arr, 0, [])
        return Solution.ans
# for debug
# for sol in Solution().solveNQueens(4):
#     print '******'
#     for s in sol:
#         print '\t'.join(list(s))