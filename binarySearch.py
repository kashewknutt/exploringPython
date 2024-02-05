def insertionSort(array):
    print("Array to be sorted:",array)
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            array[j + 1] = key
    return array

index = 0
def binarySearch(num,array):
    mid=int(len(array)/2)
    print(mid)
    if num==array[mid]:
        return mid
    elif num<array[mid]:
        print(array[0:mid])
        binarySearch(num,array[0:mid])
    else:
        print(array[mid::])
        binarySearch(num,array[mid::])
        index += mid46t
array = []
entry = '0'
print("Hello, Please enter your array (Any letter else when done to exit)")
while True:
    entry = input(":-->")
    if entry.lstrip('-').isdigit() == False:
        break
    else:
        array.append(int(entry))

print("Your array is ", array)
array = insertionSort(array)
print("The sorted array is ",array)
num = int(input("Enter which number:"))
print("The index is", binarySearch(num,array))