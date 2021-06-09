'''
We have to construct a tree bu=y using inorder and preorder traversal
'''

def build(preorder,inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = build(preorder,inorder[:index])
        root.right = build(preorder,inorder[index+1:])
        return root
