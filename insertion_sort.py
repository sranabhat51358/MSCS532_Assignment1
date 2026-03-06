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
    count = int(input("Please enter the number of elements you want to sort: "))

    user_list = []

    for i in range(count):
        value = int(input(f"Enter element {i+1}: "))
        user_list.append(value)

    print("Provided list for sorting: ", user_list)

    output = insertion_sort_desc(user_list)
    print("Sorted List in Monotonically Decreasing Order: ",output)

    
