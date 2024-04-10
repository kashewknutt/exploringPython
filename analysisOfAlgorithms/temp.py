def selction_sort(arr):
    n=len(arr)
    for i in range(n):
        mid_index=i
        for j in range (i+1,n):
            if arr[j]<arr[mid_index]:
                mid_index=j
            arr[i],arr[mid_index]=arr[mid_index],arr[i]
    return arr

arr=[64, 25, 12, 22, 11]
print(selction_sort(arr))