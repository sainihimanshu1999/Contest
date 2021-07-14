'''This was an easy to think it out question'''
'''New thing i got to learn today is that the pow(x,y,z), z can be modulus parameter in this power function and also
the time complexity of the power function is O(logn)'''



def monsters(dist,speed):
    count = 0
    time = []
    for i in range(len(dist)):
        time.append(dist[i]/speed[i])

    time.sort()

    for i in range(len(dist)):
        if time[i]>i:
            count += 1
        else:
            break
    
    return count

