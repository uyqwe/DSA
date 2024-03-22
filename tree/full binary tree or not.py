#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
        
# Return True if the given Binary Tree is a Full Binary Tree. Else return False
def isFullTree(root):
    
    #code here
    if root == None:
        return True
    if root.left==None and root.right==None:
        return True
    mover=root
    def rec(mover):
        if mover.left == None and mover.right == None:
            return True
        elif mover.left!=None and mover.right==None:
            return False
        elif mover.right!=None and mover.left==None:
            return False
        else:
            left = rec(mover.left)
            right= rec(mover.right)
            if left==True and right==True:
                return True
            else:
                return False
    return rec(mover)