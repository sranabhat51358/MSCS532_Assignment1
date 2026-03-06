def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    array = [2,3,1,8,3,7,4,10,0]
    output = insertion_sort_desc(array)
    print(output)
