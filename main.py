def countSmaller(arr):
    ret=[]
    for current in range(len(arr)-1):
        c=[]
        for next in range(current+1,len(arr)):
            if arr[current]>arr[next]:
                c.append(arr[next])
        ret.append(max(c)) if c else ret.append(0)
    return ret+[0]
arr=list(map(int,input().split()))
print(countSmaller(arr))