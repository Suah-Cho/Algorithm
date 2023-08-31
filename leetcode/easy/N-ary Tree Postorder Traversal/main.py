"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        arr = []

        def order(root) :
            if root is None : return None

            for i in root.children :
                order(i)

            arr.append(root.val)

        order(root)

        return arr