# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root==None:
            return ans
        if root.left==None and root.right==None:
            ans.append(root.val)
            return ans
        mover=root
        def rec(mover,ls):
            if mover==None:
                return 
            
            rec(mover.left,ls)
            ls.append(mover.val)
            rec(mover.right,ls)
            return ls
        return rec(mover,ans)