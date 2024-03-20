# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root==None:
            return ans
        if root.left==None and root.right==None:
            ans.append(root.val)
            return ans
        mover=root
        ls=[]
        ans=[]
        ls.append(mover)
        while(ls!=[]):
            temp=ls[-1]
            ls.pop()
            ans.append(temp.val)
            if temp.right!=None:
                ls.append(temp.right)
            
            if temp.left!=None:
                ls.append(temp.left)
        return ans