if __name__ == "__main__":
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    for i in range(len(arr1)):
        row = arr1[i] | arr2[i]

        for j in range(len(arr1), -1, -1):
            if ((row >> j) & 1) == 1:
                print("#", end=' ')
            else:
                print(" ", end=' ')
        print('')
