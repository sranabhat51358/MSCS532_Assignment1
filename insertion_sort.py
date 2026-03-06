def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        
        print("i:",i)
        print("Key:", key)
        
        j = i - 1
        
        print("J", j)
        
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
            
        print("arr[j]:",arr[j])
        print("arr[j + 1]:",arr[j + 1])
        print("Array:", arr)

        arr[j + 1] = key
        
        print("arr[j + 1] after replacing:", arr[j + 1])
        print("Array aftter replacing:", arr)

    print("Length of List:", len(arr))

    return arr

if __name__ == "__main__":
    array = [2,3,1,8,3,7,4,10,0]
    print("Provided List:", array)
    output = insertion_sort_desc(array)
    print("Sorted List in Monotonically Decreasing Order:",output)
