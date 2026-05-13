# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:

            lvl = []
            
            for _ in range(len(queue)):

                node = queue.popleft()
                lvl.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            result.append(lvl)
        
        return result