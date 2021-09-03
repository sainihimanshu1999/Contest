'''Unique binary tree can be easily done using catalan's number or using dynamic programming approach'''
'''Unique binary tee 2 is done by using dfs and basic logical concepts'''

def uniqueBst(n):

    if n == 0:
        return []


    def dfs(start,end):
        if start == end:
            return [None]

        result = []

        for i in range(start,end):
            for leftSub in dfs(start,i) or [None]:
                for rightSub in dfs(i+1,end) or [None]:
                    node = TreeNode(i)
                    node.left = leftSub
                    node.right = rightSub

                    result.append(node)



        return node


    return dfs(1,n+1)