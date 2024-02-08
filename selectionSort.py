def selectionSort(data):
    for j in range(len(data)):
        swap = j
        for i in range(j,len(data)):
            if data[i]<data[swap]:
                swap = i
        data[swap],data[j]=data[j],data[swap]
        
    return data


print("Enter your array: [any character for exit]")
data = []
while True:
    a = input("::->")
    if a.lstrip('-').isdigit() == True:
        break
    data.append(int(a))
print(selectionSort(data))
        
                
