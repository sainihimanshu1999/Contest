'''
This question does seem a bit hard first but it's more solvable by the simple maths
'''

def cake(h,w,hcuts,vcuts):
    hcuts.sort()
    vcuts.sort()

    maxH = max(hcuts[0],h-hcuts[-1])
    maxV = max(vcuts[0],w-vcuts[-1])

    for i in range(1,len(hcuts)):
        maxH = max(maxH,hcuts[i]-hcuts[i-1])
    
    for i in range(1,len(vcuts)):
        maxV = max(maxV,vcuts[i]-vcuts[i-1])

    return (maxH*maxV)%(10**9+7)


h = 50
v = 15
hcuts = [37,40,41,30,27,10,31]
vcuts =[2,1,9,5,4,12,6,13,11]

print(cake(h,v,hcuts,vcuts))
