# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        # check root/node if it is  equal to val
        # if val is less than the node value check the left sub tree
        # if val is greater than node value than check the right sub tree

        if not root:
            return None

        if val > root.val:
            return self.searchBST(root.right, val)
            # search the rigth sub tree
        elif val < root.val:
            return self.searchBST(root.left, val)
            # search left sub tree
        else:
            return root
