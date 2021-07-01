'''In this question we just do simple bactracking along the tree'''


def LCA(root,p,q):

    if root == p or root == q:
        return root

    l = r = None

    if root.left:
        l = LCA(root.left,p,q)

    if root.right:
        r = LCA(root.right,p,q)

    if l and r:
        return root

    else:
        return l or r

