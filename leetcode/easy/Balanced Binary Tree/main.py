# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node = root) :
            if node == None : # 서브트리(노드)가 비어있을 때 return 0
                return 0
            else :
                left = dfs(node.left)
                right = dfs(node.right)
                if left == -1 or right == -1 : 
                    return -1
                elif abs(right - left) > 1 : #left, rigth 높이 차이가 1 초과로 나는지 확인
                    return -1 #abs() : 절대값
                
            return max(left, right) + 1 # max(left, right) -> 깊은 노드의 높이를 알아야해서
                                        # +1 -> 부모 노드로 올라가며 현재 깊이 +1
        
        return dfs() >= 0



# class Solution(object):
#     def isBalanced(self, root):
#         return (self.Height(root) >= 0)
    
#     def Height(self, root):
#         if root is None:  return 0
#         leftheight, rightheight = self.Height(root.left), self.Height(root.right)
#         if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
#         return max(leftheight, rightheight) + 1