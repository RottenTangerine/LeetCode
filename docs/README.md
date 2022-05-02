<h1>Daily Coding Test</h1>

Solutions (almost all) I put here may not prefect, just a reference.

Have fun!

[LeetCode Link](https://leetcode.com/problemset/all/)

<hr/>

# BFS

## Number of islands

[Link](https://leetcode.com/problems/number-of-islands/)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


```python
class Solution(object):
    def numIslands(self, grid):
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
        ans, current, leaf = [], [root], []
        while root and current:
            ans.append([node.val for node in current])
            [[leaf.append(n)for n in (node.left, node.right) if n] for node in current]
            current, leaf = leaf, []
        return ans
```

## Clone Graph

[Link](https://leetcode.com/problems/clone-graph/)

Given a reference of a node in a **connected** undirected graph.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

To solve this question, I also write a code to generate and show graph.
You can see this code in `CloneGraph.py`


```python
class Solution(object):
    def cloneGraph(self, node):
        if not node: return node
        visited, queue = set(), collections.deque([node])
        copy_dict = {}

        while queue:
            current_node = queue.popleft()
            if current_node in visited: continue
            visited.add(current_node)

            if current_node not in copy_dict:
                copy_dict[current_node] = Node(current_node.val)

            for neighbor in current_node.neighbors:
                if neighbor not in copy_dict:
                    copy_dict[neighbor] = Node(neighbor.val)
                copy_dict[current_node].neighbors.append(copy_dict[neighbor])

                queue.append(neighbor)

        return copy_dict[node]
```

## Word Ladder

[Link](https://leetcode.com/problems/word-ladder/)

Given two words, beginWord and endWord, and a dictionary wordList

Return the **number of words** in the **shortest transformation sequence** from beginWord to endWord, 
or 0 if no such sequence exists.

**Stupid solution (Exceeded time limit)**
```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def list2dict(word_list):
            word_dict = {}
            for word in word_list:
                word_dict[word] = [i for i in word_list if (len([1 for x, y in zip(word, i) if x != y]) == 1)]
            return word_dict

        visited = set()
        queue = collections.deque([[i] for i in wordList if (len([1 for x, y in zip(beginWord, i) if x != y]) == 1)])
        word_dict = list2dict(wordList)

        while queue:
            current_path = queue.popleft()
            current_word = current_path[-1]

            if current_word == endWord: return len(current_path) + 1

            if current_word in visited: continue
            visited.add(current_word)

            for value in word_dict[current_word]:
                new_path = current_path + [value]
                queue.append(new_path)
        return 0
```

**Better solution from community**

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord: return length

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
```
**Hint:** check value in set takes constant-time to lookup. While loop through the list to check for a word resulting in O(N)