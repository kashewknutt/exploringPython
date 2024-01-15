def selectionSort(data):
    for j in range(len(data)):
        swap = j
        for i in range(j,len(data)):
            if data[i]<data[swap]:
                swap = i
        data[swap],data[j]=data[j],data[swap]
        
    return data

data=[23,21,23,12,24]
print(selectionSort(data))
        
                
