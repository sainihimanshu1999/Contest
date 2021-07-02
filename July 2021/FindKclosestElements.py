'''We ue binary search in this question, the answerr will be arr[start:start+k], we just have to find the starting
element'''


def kclosestelement(arr,k,x):
    left = 0
    right = len(arr)-k

    while left<right:
        mid = left+(right-left)//2

        if x<=arr[mid]:
            right = mid

        elif x>=arr[mid+k]:
            left = mid+1

        else:
            mid_dist = abs(x - arr[mid])
            mid_kdist = abs(x- arr[mid+k])

            if mid_dist<=mid_kdist:
                right = mid
            else:
                left = mid+1

    return arr[left:left+k]



arr = [1,2,3,4,5]
k = 4
x = -1

print(kclosestelement(arr,k,x))