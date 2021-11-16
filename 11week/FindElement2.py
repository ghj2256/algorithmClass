def find_element(arr, n):
    left_max = [0 for i in range(n)]
    right_min = [0 for i in range(n)]
    left_max[0] = float('-inf')

    for i in range(1, n):
        if left_max[i-1] > arr[i-1]:
            left_max[i] = left_max[i-1]
        else:
            left_max[i] = arr[i-1]

    right_min[n-1] = float('inf')

    for i in range(n-2, -1, -1):
        if right_min[i+1] > arr[i+1]:
            right_min[i] = arr[i+1]
        else:
            right_min[i] = right_min[i+1]

    sts = 0

    for i in range(n):
        if left_max[i] < arr[i] < right_min[i]:
            print(i)
            sts = 1

    if sts == 0:
        print(-1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    find_element(arr, len(arr))
