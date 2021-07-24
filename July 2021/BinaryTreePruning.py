'''This question was little tricky but easy'''

#method 1 
def pruning(root):
    def dfs(node,parent):
        if not node:
            return None

        if node.left: dfs(node.left,node)
        if node.right : dfs(node.right,node)

        if node.val == 0 and not node.left and not node.right and parent and parent.left == node:
            parent.left = None

        elif node.val == 0 and not node.right and node.right and parent and parent.right == node:
            parent.right = None

        elif not parent:
            return None

    dfs(root,None)
    
    if root.val == 0 and not root.left and not root.right:
        return None
    
    return root


#Method 2

def pruning2(root):
    if not root:
        return None


    root.left = pruning2(root.left)
    root.right = pruning2(root.right)

    if root.val == 1:
        return root
    
    if root.val ==0:
        if not root.left and not root.right : return None

    return root
