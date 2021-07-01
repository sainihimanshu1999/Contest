'''
Gray Code of a specfic (i>>1)^1 
'''

def grayCode(n):
    return [(i>>1)^i for i in range(2**n)]