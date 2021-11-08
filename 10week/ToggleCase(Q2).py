def toggle_case(a):
    c = ''
    for i in a:
        i = chr(ord(i) ^ 32)
        c += i
    return c


if __name__ == "__main__":
    char = input()

    result = toggle_case(char)
    print("Toggle Case: " + result)

    result = toggle_case(result)
    print("Original String: " + result)
