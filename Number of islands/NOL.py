# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
from functools import lru_cache

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        counter = 0
        m, n = len(grid), len(grid[0])
        total = m * n

        def find_neighbor(x, y, m, n):
            if not (-1 < x < m and  -1 < y < n): return
            if grid[x][y] == '#': return
            if grid[x][y] == '1':
                grid[x][y] = '#'
                find_neighbor(x - 1, y, m, n)
                find_neighbor(x + 1, y, m, n)
                find_neighbor(x, y - 1, m, n)
                find_neighbor(x, y + 1, m, n)
            grid[x][y] = '#'
        for i in range(m):
            for j in range(n):
                if grid[i][j]  == '#':continue
                if grid[i][j] == '1':
                    find_neighbor(i, j, m, n)
                    counter += 1
        return counter




if __name__ == '__main__':
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    solution =  Solution()
    print(solution.numIslands(grid))
