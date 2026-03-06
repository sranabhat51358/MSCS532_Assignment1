def insertion_sort_desc(arr):
    """
    This program is used to sort a user provided list of elements in monotonically
    decreasing order using insertion sort algorithm.
    Args:
        arr- array to sort
    Returns:
        arr- sorted array in decreasing order
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
                
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr

if __name__ == "__main__":
    # Ask user for the length of array
    count = int(input("Please enter the number of elements you want to sort: "))

    #Initialize an empty list
    user_list = []

    # Ask user to input value till the length of array
    for i in range(count):
        value = int(input(f"Enter element {i+1}: "))
        user_list.append(value)

    print("Provided list for sorting: ", user_list)

    #sort the list in decreasing order
    output = insertion_sort_desc(user_list)
    print("Sorted List in Monotonically Decreasing Order: ",output)

    
