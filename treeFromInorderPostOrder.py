# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.idx = len(postorder)-1

        def deepBuild(inStart, inEnd):
            if inStart > inEnd:
                return None
            root_node = TreeNode(postorder[self.idx])
            self.idx -= 1
            root_node.right = deepBuild(inorder.index(root_node.val)+1, inEnd)
            root_node.left = deepBuild(inStart, inorder.index(root_node.val)-1)
            return root_node
        return deepBuild(0, len(inorder)-1)
