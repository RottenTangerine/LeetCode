# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # make it easier to debug
    def __repr__(self):
        return f'Node({self.val})'


def create_tree(x):
    if not x: return TreeNode(None)

    x = x[::-1]

    current = [root:=TreeNode(x.pop())]
    leaf = []

    while x and current:
        for node in current:
            node.left = (_node:=TreeNode(x.pop()), leaf.append(_node))[0] if x and x[-1] else x.pop()
            node.right = (_node:=TreeNode(x.pop()), leaf.append(_node))[0] if x and x[-1] else x.pop()
        current, leaf = leaf, []
    return root

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

if __name__ == '__main__':
    node_list = [3, 9, 20, None, None, 15, 7]
    tree = create_tree(node_list)
    print(tree.right.right)

    solution = Solution()
    print(solution.levelOrder(tree))
