**Daily Coding Test**

Solutions (almost all) I put here may not prefect, just a reference.

Have fun!

[LeetCode Link](https://leetcode.com/problemset/all/)

## Number of islands

[Link](https://leetcode.com/problems/number-of-islands/)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


```python
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
```

## Binary Tree Level Order Traversal

[Link](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

To solve this question, I also write a code to generate tree in **level order**.
You can see this code in `LevelOeder.py`

```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, current, leaf = [], [root], []
        while root and current:
            ans.append([node.val for node in current])
            [[leaf.append(n)for n in (node.left, node.right) if n] for node in current]
            current, leaf = leaf, []
        return ans
```