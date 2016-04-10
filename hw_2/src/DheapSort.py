def SiftDown(a,n,i,d):
    while (i <= (n-2)//d):
        child = i*d + 1
        maxChild = a[child]
        for j in range(1,d):
            nextChild = i*d+1+j
            if (nextChild <= n-1):
                if (a[nextChild]>a[child]):
                    child = nextChild
                    maxChild = a[child]
        if (a[child] < a[i]):
            break;
        a[child],a[i] = a[i],a[child]
        i = maxChild

def DHeapSort(a,d):
    if d<2:
        return
    for i in reversed(range(0,(len(a)-2)//d+1)):
        SiftDown(a,len(a),i,d)
    for i in reversed(range(0,len(a))):
        a[0],a[i] = a[i],a[0]
        SiftDown(a,i,0,d)

k = [1,223,1223,1231,223,12,65,345,234,765,2333333,456]
DHeapSort(k,5)
print(k)

