def func(arr, n):
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for i in range(j, n):
        arr[i] = 0
    return arr


if __name__ == "__main__":
    array = [6, 0, 8, 2, 0, 3, 0, 4, 0, 1]
    num = len(array)
    print(func(array, num))
