#inorder iterative method
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
        ls=[]
        ans=[]
        ls.append(mover)
        while(ls!=[None]):
            temp=ls[-1]
            if temp==None:
                ls.pop()
                temp=ls[-1]
                ans.append(temp.val)
                ls.pop()
                ls.append(temp.right)
            else:
                ls.append(temp.left)
        return ans
        