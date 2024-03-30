# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left==None and root.right==None:
            return True
        mover=root
        def rec(mover):
            
            if mover==None:
                return 0
            left=rec(mover.left)
            if left==-1:
                return -1
            right=rec(mover.right)
            if right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return max(left,right)+1
            
            

        l=rec(mover)
        if l==-1:
            return False
        return True
        