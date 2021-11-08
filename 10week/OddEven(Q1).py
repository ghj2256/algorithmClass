def is_even(num):
    if num ^ 1 == num + 1:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n = int(input())

    if is_even(n) == 1:
        print("Even")
    else:
        print("Odd")
