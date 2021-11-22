class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        left = root.left
        right = root.right
        if root.val == key:
            if right is None:
                root = left
                return root
            elif left is None:
                root = right
                return root
            temp = left
            while temp.right:
                temp = temp.right
            temp.right = right
            root = left
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
