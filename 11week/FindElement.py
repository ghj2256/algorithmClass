def find_element(arr, n):
    left_max = [0 for i in range(n)]
    left_max[0] = float('-inf')

    for i in range(1, n):
        if left_max[i - 1] > arr[i - 1]:
            left_max[i] = left_max[i - 1]
        else:
            left_max[i] = arr[i - 1]

    right_min = float('inf')

    for i in range(n-1, 0, -1):
        if left_max[i] < arr[i] < right_min:
            return i
        if right_min > arr[i]:
            right_min = arr[i]

    return -1


if __name__ == "__main__":
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    idx = find_element(arr, len(arr))

    print(idx)
