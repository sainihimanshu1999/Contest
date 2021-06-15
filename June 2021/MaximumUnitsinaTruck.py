def maxunits(boxTypes,truckSize):
    boxTypes = sorted(boxTypes,key=lambda x:-x[1])
    total = 0
    size = truckSize
    
    for i in range(len(boxTypes)):
        size -= boxTypes[i][0]
        total += boxTypes[i][0]*boxTypes[i][1]
        # print(size)
        
        if size == 0:
            return total
        
        elif size<0:
            total -= abs(size)*boxTypes[i][1]
            return total
        
        
    return total