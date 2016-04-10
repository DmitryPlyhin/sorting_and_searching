def Merge(series):
    lengths = []
    indexes = []
    numberofsteps = 0
    merging = []
    for s in series:
        numberofsteps+=len(s)
        lengths.append(len(s))
        indexes.append(0)
    for i in range(numberofsteps):
        minimum = 0
        isminimumset = 0
        for j in range(len(series)):
            if (indexes[j] < lengths[j]):
                if (isminimumset == 0):
                    isminimumset = 1
                    minimum = series[j][indexes[j]]
                    jmin = j
                elif (series[j][indexes[j]] < minimum):
                    minimum = series[j][indexes[j]]
                    jmin = j
        indexes[jmin]+=1
        merging.append(minimum)
    return merging

def DMergeSort(a,d):
    if len(a)<=1:
        return a
    series = []
    for i in range(d):
        series.append(DMergeSort(a[i*len(a)//d:(i+1)*len(a)//d],d))
    return Merge(series)

k = [1,223,1223,1231,223,12,65,345,234,765,2333333,456]
k = DMergeSort(k,5)
print(k)
    
