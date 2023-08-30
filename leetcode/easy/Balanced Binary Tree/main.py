# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # print(root)
        R = root
        def dfs(node = root) :
            
            if node == None :
                return 0
            else :
                left = dfs(node.left)
                right = dfs(node.right)
                if left == -1 or right == -1 : return -1
                elif abs(left - right) > 1 : return -1 #abs() : 절대값
            return abs(left - right)
        
        return dfs() >= 0


sol = Solution()

# print(sol.isBalanced([3,9,20,-1, -1,15,7]))
print(sol.isBalanced([]))

