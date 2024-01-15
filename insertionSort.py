def insertionSort(data):
    for a in range(1,len(data)):
        compare = data[a]
        prev = a - 1
        while prev >= 0 and data[prev]>compare:
            data[prev+1]=data[prev]
            prev = prev -1
        data[prev+1] = compare
    return data

data=[16,2,34,20,3,50,3,1]
print(insertionSort(data))
