from math import log2


def get_pos_of_rightmost_set_bit(n):
    return log2(~n & (n+1)) + 1


def set_rightmost_unset_bit(n):
    if n == 0:
        return 1
    if n & (n+1) == 0:
        return n
    pos = get_pos_of_rightmost_set_bit(n)
    return 1 << int((pos-1)) | n


if __name__ == "__main__":
    n = int(input())
    print(set_rightmost_unset_bit(n))
